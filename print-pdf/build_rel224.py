# -*- coding: utf-8 -*-
# Exact verbatim text from the live REL 224 site. Same compact system as
# FYW 1323 and REL 320, restyled in REL 224's own saffron/maroon/gold
# palette and display serif. No cover photo exists for this course, so the
# cover uses a line-art mandala motif matching the live site's own
# decorative SVGs instead of a photograph.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_schedule import sched_table
from rel224_data import rows as sched_rows, ashoka_sessions

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "rel224-syllabus.html")

TOKENS = """
:root {
  --paper: #ffffff;
  --ink: #2b1a15;
  --ink-soft: #7a5c47;
  --dark: #2b1a15;
  --on-dark: #f3e9d8;
  --on-dark-soft: #d9c4a8;
  --accent-a: #d9822b;
  --accent-strong: #9c2a38;
  --accent-b: #9c742f;
  --line: #e6d9c7;
  --callout-bg: #faf1e2;
  --photo-bg: #fbf5ea;
  --accent-mark: #e0b954;
  --font-display: "Cormorant Garamond", serif;
  --font-body: "Work Sans", sans-serif;
}
body { background: #ffffff; }
mark { background: var(--accent-mark); color: var(--ink) !important; padding: 0 3px; border-radius: 2px; font-weight: 700; }
a { color: var(--accent-strong); }
table.sched { font-size: 8.7px; }
table.sched td { padding: 4px 4px; line-height: 1.3; }
table.sched td ul { padding-left: 0.95em; }
.mandala-mark { color: var(--accent-a); }
"""

HEAD = f"""<!doctype html>
<html><head><meta charset="utf-8">
<title>REL 224 Syllabus</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Work+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="print-system.css">
<style>{TOKENS}</style>
</head><body>
"""

RUNHEAD = '<div class="runhead">Fall 2026 &middot; Furman University &middot; REL 224</div>'

def item(heading, body_html, accent=False):
    return f'<div class="item"><h4>{heading}</h4><div class="prose">{body_html}</div></div>'

# Small reproduction of the site's own line-art mandala (lotus-petal ring,
# gated square, concentric circles) for the cover, standing in for a photo.
MANDALA_SVG = """
<svg class="mandala-mark" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-width="1.1" style="width:2.6in; height:2.6in; margin:0 auto; display:block;">
  <circle cx="100" cy="100" r="88"/>
  <circle cx="100" cy="100" r="80"/>
  <g>
    <path d="M90.30 38.76 Q100.00 22.00 109.70 38.76"/>
    <path d="M114.47 39.71 Q129.85 27.94 132.39 47.14"/>
    <path d="M136.44 49.84 Q155.15 44.85 150.16 63.56"/>
    <path d="M152.86 67.61 Q172.06 70.15 160.29 85.53"/>
    <path d="M161.24 90.30 Q178.00 100.00 161.24 109.70"/>
    <path d="M160.29 114.47 Q172.06 129.85 152.86 132.39"/>
    <path d="M150.16 136.44 Q155.15 155.15 136.44 150.16"/>
    <path d="M132.39 152.86 Q129.85 172.06 114.47 160.29"/>
    <path d="M109.70 161.24 Q100.00 178.00 90.30 161.24"/>
    <path d="M85.53 160.29 Q70.15 172.06 67.61 152.86"/>
    <path d="M63.56 150.16 Q44.85 155.15 49.84 136.44"/>
    <path d="M47.14 132.39 Q27.94 129.85 39.71 114.47"/>
    <path d="M38.76 109.70 Q22.00 100.00 38.76 90.30"/>
    <path d="M39.71 85.53 Q27.94 70.15 47.14 67.61"/>
    <path d="M49.84 63.56 Q44.85 44.85 63.56 49.84"/>
    <path d="M67.61 47.14 Q70.15 27.94 85.53 39.71"/>
  </g>
  <rect x="52" y="52" width="96" height="96"/>
  <g id="rel224-gate">
    <rect x="94" y="30" width="12" height="22"/>
    <rect x="88" y="30" width="24" height="8"/>
  </g>
  <use href="#rel224-gate" transform="rotate(90 100 100)"/>
  <use href="#rel224-gate" transform="rotate(180 100 100)"/>
  <use href="#rel224-gate" transform="rotate(270 100 100)"/>
  <circle cx="100" cy="100" r="44"/>
  <circle cx="100" cy="100" r="30"/>
  <circle cx="100" cy="100" r="16"/>
  <circle cx="100" cy="100" r="2.5" fill="currentColor"/>
</svg>
"""

pages = []

# ---------------- PAGE 1: COVER ----------------
pages.append(f"""
<div class="page">
  <div class="cover-hero">
    <div class="cover-eyebrow">Fall 2026 &middot; Furman University</div>
    <h1 class="cover-title" style="font-size:54px;">INTRODUCTION TO<br>BUDDHISM</h1>
    <p class="cover-subtitle">Origins, transformations, and the study of Buddhism across Asia and the globe &mdash; REL 224</p>
  </div>
  <div class="pad" style="margin-top:0.34in;">
    {MANDALA_SVG}
    <div class="cols2" style="margin-top:0.32in;">
      <div class="side-head" style="grid-template-columns:1.1in 3px 1fr;">
        <div class="label" style="font-size:15px;">Course<br>Info</div>
        <div class="rule"></div>
        <div class="body prose">
          <p><strong>Meets:</strong> Tue / Thu, 1:00&ndash;2:15 PM &middot; Hipp Hall 104</p>
          <p><strong>Instructor:</strong> Dr. Tori Montrose<br>victoria.montrose@furman.edu</p>
          <p><strong>Office:</strong> Furman Hall 206J &middot; Office hours by appointment</p>
        </div>
      </div>
      <div class="prose">
        <p style="font-size:10.8px;"><strong>Response Time:</strong> I try to respond to emails within 48 hours, Monday&ndash;Friday. If a matter is urgent or I haven&rsquo;t responded within 2 business days, please don&rsquo;t hesitate to send a follow-up email or book an appointment using the link in the Office Hours box.</p>
      </div>
    </div>
  </div>
</div>
""")

# ---------------- PAGE 2: DESCRIPTION, TEXTS, OUTCOMES ----------------
pages.append(f"""
<div class="page">
  {RUNHEAD}
  <div class="pad" style="margin-top:0.3in;">
    <div class="sec-title">Course Description &amp; Learning Outcomes</div>
    <div class="prose">
      <p>This course serves as an introduction to the diversity of Buddhist traditions. Engaging with primary texts and secondary scholarship, we will study the origins of Buddhism and trace its development across Asia and the globe. We use an interdisciplinary lens to cover major themes in the history, thought, and practice of Buddhism. This course also examines and critiques the complicated colonial and orientalist history of Buddhism as an object of study.</p>
    </div>

    <h4 class="block-title" style="margin-top:0.2in;">Course Texts</h4>
    <ul class="prose" style="font-size:11.5px; line-height:1.5;">
      <li>C. Pierce Salguero. <a href="https://www.penguinrandomhouse.com/books/691081/buddhish-by-c-pierce-salguero/"><em>Buddhish: A Guide to the 20 Most Important Buddhist Ideas for the Curious and Skeptical</em></a>. Beacon Press, 2022.</li>
      <li>J. Noel Hubler. <a href="https://uncpress.org/9781469695471/ashoka/"><em>Ashoka: Becoming the Dharma King</em></a>. University of North Carolina Press (Reacting to the Past), 2026.</li>
    </ul>
    <p class="prose" style="font-size:11.5px;"><strong>All other readings will be posted to Moodle.</strong></p>

    <h4 class="block-title" style="margin-top:0.2in;">Learning Outcomes</h4>
    <div class="cols2">
      <div class="prose">
        <ul>
          <li>We will explain foundational aspects of Buddhism and discuss the diversity of Buddhist communities, expressions, and traditions.</li>
          <li>We will engage in critical self-reflection on our understanding and perception of Buddhism and Buddhist cultures and identify changes to that understanding over time.</li>
          <li>We will deconstruct and evaluate the historical development, predominant assumptions, and popular methods in the field of Buddhist Studies.</li>
        </ul>
      </div>
      <div class="prose">
        <ul>
          <li>We will be able to analyze, summarize, and relate Buddhist works and ideas.</li>
          <li>We will grow in our capacity to empathize with others by developing the ability to visit/inhabit their worldviews.</li>
        </ul>
      </div>
    </div>
  </div>
</div>
""")

# ---------------- GRADED ELEMENTS ----------------
attendance = item("Attendance and Engagement &mdash; 20%",
  '<p>Every version of this course is unique to the combination of students that comprise it. Your presence is an essential part of the learning experience for yourself and all of us in the room with you. This course requires you to come prepared to share your questions, struggles, and ideas surrounding the readings and content we cover. Each student is expected to actively participate in all activities and discussions. There are several ways to demonstrate engagement including small group discussions, taking notes, large group discussions, polls. See <a href="#rubrics">Engagement Rubric</a>.</p>')

rrj = item("Reading and Reflection Journal (RRJ) &mdash; 25%",
  '<p>A mix of in-class and at-home short written responses to a prompt about the readings. They will frame your thinking about the readings and help prepare you for in-class discussion or reflect on your learning. Unless you have an accommodation, these journals will be handwritten. There will be 21 entries in total. Journals will be collected every few weeks to check for completion. <strong>To be considered complete, each entry must be a minimum of 6 sentences long and must address the prompt.</strong> RRJs missed due to absence can be made up upon return to class.</p>'
  '<p><strong>Midterm submission (10%)</strong> &mdash; <mark>due Thu. 10/15: submit RRJs 1&ndash;11</mark>:</p>'
  '<ul>'
  '<li>5% is graded for <strong>completion</strong>: RRJ #1 is mandatory but you can skip 1 other RRJ of your choice without penalty.</li>'
  '<li>5% is graded for <strong>quality</strong> &mdash; select your 3 strongest entries from RRJ #1&ndash;11. See the <a href="#rrj-rubric">RRJ grading rubric</a> to help you determine your 3 strongest entries.</li>'
  '</ul>'
  '<p><strong>Final submission (15%):</strong></p>'
  '<ul>'
  '<li>5% is graded for <strong>completion</strong>: RRJs #12, 18, 21 are mandatory but you can skip 1 other RRJ of your choice without penalty.</li>'
  '<li>10% is graded for <strong>quality</strong> &mdash; RRJs #12, 18, 21 will be graded, then select your other strongest entry from the remaining RRJs. See the <a href="#rrj-rubric">RRJ grading rubric</a>.</li>'
  '</ul>')

exams = item("Exams &mdash; 25%",
  '<p>There will be 2 exams in this class (each worth 12.5%): a midterm (see the <a href="#schedule">Weekly Schedule</a>) and a final exam on <mark>Friday, December 11, 12:00&ndash;2:30 PM in Hipp Hall 104</mark>. They will be cumulative, but with a greater emphasis on the material taught since the midterm. Since we will be learning a lot of new terms in multiple global languages, a single 3x5-inch handwritten note card may be used during each exam. Exams will be a combination of multiple choice, short answer, and textual/image analysis.</p>')

ashoka_paper = item("<em>Ashoka</em> Position Paper &mdash; 15%",
  '<p>This is an in-class assignment: students will write a position paper from the perspective of their character. See the <a href="#ashoka">Ashoka Game tab</a> for more information. <strong>More details forthcoming.</strong></p>')

ashoka_speeches = item("<em>Ashoka</em> Speeches (&times;2) &mdash; 10%",
  '<p>Based on your position paper, you will give 2 short in-class speeches taking the position assigned to your role in the <em>Ashoka</em> game. Since the content of your speeches should largely match the content of your position paper, this part of the grade primarily assesses the quality of your delivery and adherence to the allotted time.</p>')

ashoka_engagement = item("<em>Ashoka</em> Engagement &mdash; 5%",
  '<p>This is a separate engagement grade from your overall course engagement grade. It captures all the ways you might engage with this game, including (but not limited to): consistently demonstrating preparation for each council session (not only the ones in which you are giving a speech); active coordination, collaboration, and communication with your faction (or across factions if the need arises); asking questions and/or commenting on others&rsquo; speeches; actions within the game that are consistent with your assigned role (liberally interpreted); and taking notes during sessions while avoiding non-game-related distractions.</p>')

pages.append(f"""
<div class="page">
  {RUNHEAD}
  <div class="pad" style="margin-top:0.3in;">
    <div class="sec-title" id="graded">Graded Elements</div>
    <div class="sec-kicker">How your final grade is calculated, and what each element involves.</div>
    <table class="weights">
      <thead><tr><th>Component</th><th class="num">Weight</th></tr></thead>
      <tbody>
        <tr><td>Attendance and Engagement</td><td class="num">20%</td></tr>
        <tr><td>Reading and Reflection Journal (RRJ)</td><td class="num">25%</td></tr>
        <tr><td>Exams (2, 12.5% each)</td><td class="num">25%</td></tr>
        <tr><td><em>Ashoka</em> Speeches (&times;2)</td><td class="num">10%</td></tr>
        <tr><td><em>Ashoka</em> Engagement</td><td class="num">5%</td></tr>
        <tr><td><em>Ashoka</em> Position Paper</td><td class="num">15%</td></tr>
      </tbody>
    </table>
    <h4 class="block-title" style="margin-top:0.15in;">Element Descriptions</h4>
    {attendance}
    {rrj}
  </div>
</div>
""")

pages.append(f"""
<div class="page">
  {RUNHEAD}
  <div class="pad" style="margin-top:0.32in;">
    {exams}
    {ashoka_speeches}
    {ashoka_engagement}
    {ashoka_paper}
  </div>
</div>
""")

# ---------------- SCHEDULE PAGES ----------------
headers = ["#", "Date", "Topic", "Pre-class Activity/Assignment", "RRJ #", "Notes"]
widths = ["0.3in", "0.82in", "1.28in", None, "0.62in", "1.28in"]

def sched_page(title, rows_slice, first=False):
    tb = sched_table(headers, rows_slice, ["topic", "preclass", "rrj", "notes"], widths)
    tbar = f'<div class="title-bar" id="schedule">{title}</div>' if first else RUNHEAD
    return f"""
<div class="page">
  {tbar}
  <div class="pad" style="margin-top:0.14in;">{tb}</div>
</div>
"""

# Row chunks tuned by height-measurement pass (see verify.py).
SCHED_CHUNKS = [(0, 16), (16, 30)]

first = True
for start, end in SCHED_CHUNKS:
    title = "CLASS SCHEDULE" if first else ""
    pages.append(sched_page(title, sched_rows[start:end], first=first))
    first = False

# ---------------- ASHOKA GAME ----------------
ashoka_rows = "\n".join(f'<tr><td>{d}</td><td>{s}</td></tr>' for d, s in ashoka_sessions)

pages.append(f"""
<div class="page">
  {RUNHEAD}
  <div class="pad" style="margin-top:0.28in;">
    <div class="sec-title" id="ashoka" style="font-size:22px;">The <em>Ashoka</em> Game</div>
    <div class="sec-kicker">A role-playing simulation of King Ashoka&rsquo;s council, staged in place of several regular class sessions.</div>
    <div class="prose">
      <p style="font-size:10.8px;">In place of several regular class sessions, we will run <em>Ashoka</em>, a role-playing game in which each student represents a tradition or faction advising King Ashoka&rsquo;s council. You will prepare position papers and deliver speeches in character, drawing on primary texts from the traditions active in Ashoka&rsquo;s era. See the <a href="#policies">Policies tab</a> for the game-specific attendance exception, and the <a href="#graded">Graded Elements tab</a> for how the Position Paper, Speeches, and Engagement components are weighted.</p>
    </div>
    <h4 class="block-title" style="margin-top:0.1in; font-size:13px;">Game Schedule</h4>
    <table class="weights" style="font-size:9.8px; margin:0.05in 0 0.14in;">
      <thead><tr><th>Date</th><th>Session</th></tr></thead>
      <tbody>
        {ashoka_rows}
      </tbody>
    </table>

    <h4 class="block-title" style="font-size:13px;">Position Paper Guidelines</h4>
    <div class="prose">
      <p style="font-size:11px; line-height:1.5;">This is an in-class assignment: students will write a position paper from the perspective of their character. <strong>More details forthcoming.</strong></p>
    </div>

    <h4 class="block-title" style="font-size:13px; margin-top:0.15in;">Position Paper Grading Rubric</h4>
    <p class="prose" style="font-size:11px; font-style:italic; color:var(--ink-soft);">Forthcoming.</p>
  </div>
</div>
""")

# ---------------- POLICIES ----------------
accessibility = item("Statement on Accessibility and Inclusivity",
  '<p>In the spirit of Universal Design for Learning, I will strive to provide an environment that is equitable and conducive to achievement and learning for all students. I recognize and value the many perspectives students bring to the classroom. Many factors&mdash;social identities, visible and invisible disabilities, family circumstances, physical location, mental health, access to the internet&mdash;all influence the experiences that every individual can have in this course. I am committed to building an environment to support your learning. I ask that we all be respectful of diverse opinions and of all class members, regardless of personal attribute, and that we all use inclusive language in written and oral work. I encourage persons with Student Office for Accessibility Resources (SOAR) accommodations or other needs that may impact your performance to meet with me promptly to make a plan for the semester.</p>')

pronoun = item("Name/Pronoun Use",
  '<p>I am committed to an environment that affirms people of all gender expressions and gender identities. I will gladly honor the name or gender pronouns that are correct for you. I will never require you to disclose this information, as I view it as your choice to share if and when you desire. If you choose to share this information, please advise me early in the semester so that I may make appropriate changes to my records.</p>')

absences = item("Policies on Absences and Late Submissions",
  '<p>Students are allowed <strong>3 free absences</strong> (roughly 10% of the total number of classes) regardless of the reason. I do not need you to email me or provide an explanation for these absences. These include absences due to illnesses, personal loss, athletics, religious observances, or any other reason. After 3 absences, your attendance and participation grade will be negatively impacted.</p>'
  '<p><strong>The only exception to this policy is during the <em>Ashoka</em> role-playing game</strong> (see the <a href="#ashoka">Ashoka Game tab</a> for dates), when students who are absent during the game will need prior professor permission or a valid excuse with documentation from the health center or the academic dean&rsquo;s office. Unexcused absences during the game will immediately have a negative impact on your attendance and engagement grade.</p>'
  '<p><strong>Late submissions</strong> following absences must be submitted on the day of return to class. Otherwise, late submissions of assignments may be accepted for partial credit depending on the circumstances.</p>')

integrity = item("Statement on Academic Integrity",
  '<p>Per <a href="https://policies.furman.edu//view.php?policy=584">Section 121.5 of Furman&rsquo;s University Policy</a>, &ldquo;All forms of academic misconduct including cheating, plagiarism, misrepresentation, and unacceptable collaboration are violations of Furman&rsquo;s academic integrity standard. Examples and explanations may be found elsewhere in official university documents (e.g., The Student Handbook and the academic integrity portion of the Furman University website).&rdquo;</p>'
  '<p>Please note: Students who are suspected of submitting writing produced in any part by an AI system will be subjected to review by the Academic Discipline Committee. For more information on Generative Artificial Intelligence use in this class, see the Use of Generative Artificial Intelligence (AI) policy below.</p>'
  '<p>It is always better to get a zero on an assignment rather than submitting something that violates the university&rsquo;s academic integrity policy, which usually results in far worse consequences.</p>')

recordings = item("Course Activity Recordings",
  '<p>Furman University prohibits the recording of classes by students without obtaining prior, written permission of the instructor, except in cases where Furman permits a qualified student with a documented disability to record classes as a reasonable accommodation. Students are advised of this policy in the Student Handbook. Under no circumstances should recorded classes be used in any way that denigrates and/or decontextualizes the instructor or any student whose class remarks are recorded. Unauthorized dissemination of any recorded classroom proceedings, including distribution for compensation, is strictly prohibited. The improper sharing of recorded material by students or others may constitute a violation of U.S. copyright law and is a violation of campus policy.</p>')

nondiscrim = item("Nondiscrimination Policy and Sexual Misconduct",
  '<p>Furman University and its faculty are committed to supporting our students and seeking an environment that is free of bias, discrimination, and harassment. Furman does not unlawfully discriminate on the basis of race, color, national origin, sex, sexual orientation, gender identity, pregnancy, disability, age, religion, veteran status, or any other characteristic or status protected by applicable local, state, or federal law in admission, treatment, or access to, or employment in, its programs and activities.</p>'
  '<p>If you have encountered any form of discrimination or harassment, including sexual misconduct (e.g. sexual assault, sexual harassment or gender-based harassment, sexual exploitation or intimidation, stalking, intimate partner violence), we encourage you to report this to the institution. If you wish to report such an incident of misconduct, you may contact Furman&rsquo;s Title IX Coordinator, Melissa Nichols (Trone Center, Suite 215; Melissa.nichols@furman.edu; 864.294.2221).</p>'
  '<p>If you would like to speak with someone who can advise you but maintain complete confidentiality, you can talk with a counselor, a professional in the Student Health Center, or someone in the Office of Spiritual Life. If you speak with a faculty member, understand that as a mandated reporter of the University, the faculty member MUST report to the University&rsquo;s Title IX Coordinator what you share to help ensure that your safety and welfare are being addressed, consistent with the requirements of the law. However, unless there is an ongoing safety risk to you or to the Furman community, you will determine whether the university initiates any formal process. You are entitled to supportive measures (such as a no contact order or academic accommodations) regardless of whether you decide to initiate a formal process.</p>'
  '<p>Additional information about Furman&rsquo;s Sexual Misconduct Policy, how to report sexual misconduct, and your rights can be found at the Furman Title IX webpage at <a href="https://www.furman.edu/titleix">www.furman.edu/titleix</a>. You do not have to go through the experience alone.</p>')

ai_policy = item("Use of Generative Artificial Intelligence (AI)",
  '<p>This is a &ldquo;No, But&rdquo; course. This means that generative AI tools are <strong>generally prohibited</strong> unless explicitly permitted for specific assignments or activities.</p>'
  '<ul>'
  '<li>AI tools cannot be used to generate anything, in part or in whole, that is submitted with a student&rsquo;s name on it for credit, unless the instructor explicitly permits it for an assignment.</li>'
  '<li>Specific assignments may incorporate AI tools for specific learning objectives.</li>'
  '<li>When AI use is allowed, assignment instructions will identify which tools are allowed and to what extent they may be used.</li>'
  '<li>In cases of uncertainty, students should assume that no AI tool is allowed.</li>'
  '</ul>'
  '<p><strong>When AI is NOT Permitted:</strong></p>'
  '<p>A key learning goal in this course is engaging in reflection on your own development. Reflective exercises require you to think about what you have experienced, critically evaluate that experience, and articulate your learning from that experience.</p>'
  '<p>Generative AI tools that write text for you (such as ChatGPT, Microsoft Copilot, and Canva) are prohibited for these assignments. Violations will be considered academic misconduct.</p>'
  '<p><strong>When AI IS Permitted:</strong></p>'
  '<p>If AI use is permitted for a specific assignment or activity, it will be clearly stated in the assignment or activity instructions. These instructions will specify:</p>'
  '<ul><li>What AI tools you may use</li><li>How you may use them</li><li>How you must acknowledge your use</li></ul>'
  '<p>Even when AI is permitted:</p>'
  '<ul>'
  '<li>You are responsible for verifying the accuracy of any AI-generated content</li>'
  '<li>You must acknowledge your use of AI as instructed</li>'
  '<li>You cannot upload copyrighted materials (textbooks, instructor notes, slides) to AI without express permission</li>'
  '</ul>'
  '<p><strong>Grammar and Spell Check Tools:</strong></p>'
  '<ul>'
  '<li>You may use your word processor&rsquo;s native spelling and grammar checker (e.g., built-in tools in Word or Google Docs that are not LLM-based) only to identify sentence-level issues. Allowing these tools to rewrite parts of sentences, whole sentences, or paragraphs is not acceptable. You do not need to cite the use of these standard tools.</li>'
  '<li>You may not use Grammarly or similar third-party writing assistants, as these tools often provide more intervention than is appropriate for this course.</li>'
  '</ul>'
  '<p><strong>When in Doubt, Ask!</strong></p>'
  '<p>If you are uncertain whether AI use is permitted for a specific assignment or activity, ask me before you use it. If you have questions about what constitutes plagiarism or academic misconduct, consult me before it&rsquo;s too late!</p>'
  '<p>The penalty for academic integrity violations is an F for the assignment or, in case of multiple violations, an F for the course.</p>')

pages.append(f"""
<div class="page">
  {RUNHEAD}
  <div class="pad" style="margin-top:0.32in;">
    <div class="sec-title" id="policies">Course Policies</div>
    <div class="sec-kicker">Please read these carefully &mdash; they explain how the class runs day to day.</div>
    {accessibility}
    {pronoun}
    {absences}
    {recordings}
  </div>
</div>
""")

pages.append(f"""
<div class="page">
  {RUNHEAD}
  <div class="pad" style="margin-top:0.32in;">
    {integrity}
    {nondiscrim}
  </div>
</div>
""")

pages.append(f"""
<div class="page">
  {RUNHEAD}
  <div class="pad" style="margin-top:0.32in;">
    {ai_policy}
  </div>
</div>
""")

# ---------------- RUBRICS ----------------
pages.append(f"""
<div class="page">
  {RUNHEAD}
  <div class="pad" style="margin-top:0.2in;">
    <div class="sec-title" id="rubrics" style="font-size:22px;">Engagement &amp; RRJ Rubrics</div>
    <div class="sec-kicker" style="margin-bottom:0.1in;">General rubrics that apply across the semester. The <em>Ashoka</em> Position Paper has its own rubric on the Ashoka Game tab.</div>
    <h4 class="block-title" style="margin-bottom:0.06in;">Engagement Rubric</h4>
    <p class="prose" style="font-size:10.5px; margin:0 0 0.08in;">Each class, your engagement will be assessed using the following scale:</p>
    <div class="cols3" style="font-size:10px;">
      <div class="prose">
        <h4 class="block-title" style="font-size:13px;">A-level</h4>
        <ul style="font-size:9.6px; line-height:1.3;">
          <li>Prepared to ask and answer questions, in writing or orally, based on assigned readings;</li>
          <li>Prepared with any required assignments;</li>
          <li>Focused on classroom discussions and activities (i.e., not using technology unless it aids in classroom discussion or activities, not conducting side conversations, not engaging in behaviors that disrupt the focus of others);</li>
          <li>Fully engaged in all in-class activities;</li>
          <li>Fully attentive when others are speaking; and</li>
          <li>Fully attentive to your own contributions, which includes&hellip;
            <ul style="font-size:9.6px; line-height:1.3;">
              <li>giving others the space and time to contribute;</li>
              <li>understanding that others come to our classroom with different experiences than your own; and</li>
              <li>being open to learning, including learning from your own mistakes.</li>
            </ul>
          </li>
        </ul>
      </div>
      <div class="prose">
        <h4 class="block-title" style="font-size:13px;">B-level</h4>
        <ul style="font-size:9.6px; line-height:1.3;">
          <li>Mostly prepared to ask and answer questions, in writing or orally, based on assigned readings;</li>
          <li>Prepared with any required assignments;</li>
          <li>Mostly focused on classroom discussions and activities (i.e., not using technology unless it aids in classroom discussion or activities, not conducting side conversations, not engaging in behaviors that disrupt the focus of others);</li>
          <li>Mostly engaged in all in-class activities;</li>
          <li>Mostly attentive when others are speaking; and</li>
          <li>Mostly attentive to your own contributions, which includes&hellip;
            <ul style="font-size:9.6px; line-height:1.3;">
              <li>giving others the space and time to contribute;</li>
              <li>understanding that others come to our classroom with different experiences than your own; and</li>
              <li>being open to learning, including learning from your own mistakes.</li>
            </ul>
          </li>
        </ul>
      </div>
      <div class="prose">
        <h4 class="block-title" style="font-size:13px;">C&ndash;D level</h4>
        <ul style="font-size:9.6px; line-height:1.3;">
          <li>Arrived more than 5 minutes late and/or left before the end of class;</li>
          <li>Not prepared to ask and answer questions, in writing or orally, based on assigned readings;</li>
          <li>Not prepared with some or any required assignments;</li>
          <li>Not focused on classroom discussions and activities (i.e., using technology in ways other than for use in classroom discussion or activities, conducting side conversations, engaging in behaviors that disrupt the focus of others);</li>
          <li>Not engaged in all in-class activities;</li>
          <li>Not attentive when others are speaking; OR</li>
          <li>Not attentive to your own contributions, which includes&hellip;
            <ul style="font-size:9.6px; line-height:1.3;">
              <li>Not giving others the space and time to contribute;</li>
              <li>Not understanding that others come to our classroom with different experiences than your own; and</li>
              <li>Not being open to learning, including learning from your own mistakes.</li>
            </ul>
          </li>
        </ul>
      </div>
    </div>

    <h4 class="block-title" style="margin-top:0.12in;" id="rrj-rubric">Reading and Reflection Journal (RRJ) Rubric</h4>
    <table class="weights">
      <thead><tr><th>Element</th><th>Aspects</th><th class="num">Points</th></tr></thead>
      <tbody>
        <tr><td>1. Comprehension</td><td>Demonstrates clear understanding of the assigned readings; accurately represents key concepts and ideas</td><td class="num">0&ndash;2</td></tr>
        <tr><td>2. Analysis</td><td>Goes beyond summary to provide insightful analysis; applies relevant analytical frameworks when appropriate</td><td class="num">0&ndash;2</td></tr>
        <tr><td>3. Depth of Reflection</td><td>Engages in meaningful personal reflection; connects ideas to own experiences or perspectives</td><td class="num">0&ndash;1</td></tr>
        <tr><td>4. Creativity</td><td>Responds imaginatively to creative prompts; demonstrates original thinking</td><td class="num">0&ndash;1</td></tr>
        <tr><td>5. Critical Thinking</td><td>Evaluates ideas critically; considers multiple perspectives</td><td class="num">0&ndash;1</td></tr>
        <tr><td>6. Connection-Making</td><td>Links concepts across different readings or topics; identifies broader implications or applications</td><td class="num">0&ndash;1</td></tr>
        <tr><td>7. Intellectual Curiosity</td><td>Raises thought-provoking questions; explores ideas beyond the immediate scope of the prompt</td><td class="num">0&ndash;1</td></tr>
        <tr><td>8. Evidence of Preparation</td><td>References specific details from assigned readings; shows thorough engagement with course materials</td><td class="num">0&ndash;1</td></tr>
        <tr><td><strong>Total</strong></td><td></td><td class="num"><strong>/10</strong></td></tr>
      </tbody>
    </table>
  </div>
</div>
""")

with open(OUT, "w") as f:
    f.write(HEAD)
    f.write("\n".join(pages))
    f.write("</body></html>")

print("wrote", OUT, "pages so far:", len(pages))
