import html

def esc(s):
    return s

def sched_rows_html(rows, cols_after_date, unit_col_is_divider=False):
    """rows: list of dicts with keys matching column set."""
    out = []
    for r in rows:
        if r.get('unit'):
            colspan = 2 + len(cols_after_date)
            out.append(f'<tr class="unit-row"><td colspan="{colspan}">{r["unit"]}</td></tr>')
            continue
        if r.get('noclass'):
            colspan = 2 + len(cols_after_date)
            out.append(f'<tr class="noclass-row"><td>{r.get("num","&mdash;")}</td><td>{r["date"]}</td><td colspan="{colspan-2}">{r["noclass"]}</td></tr>')
            continue
        cells = [f'<td class="num-col">{r.get("num","&mdash;")}</td>', f'<td class="date-col">{r["date"]}</td>']
        for c in cols_after_date:
            cells.append(f'<td>{r.get(c,"")}</td>')
        out.append('<tr>' + ''.join(cells) + '</tr>')
    return '\n'.join(out)

def sched_table(headers, rows, cols_after_date, col_widths=None):
    widths = col_widths or [None] * len(headers)
    th_parts = []
    for h, w in zip(headers, widths):
        style_attr = ' style="width:{}"'.format(w) if w else ""
        th_parts.append('<th{}>{}</th>'.format(style_attr, h))
    ths = ''.join(th_parts)
    body = sched_rows_html(rows, cols_after_date)
    return f'<table class="sched"><thead><tr>{ths}</tr></thead><tbody>{body}</tbody></table>'
