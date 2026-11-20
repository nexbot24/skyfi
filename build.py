"""Static site generator for the SKYi redesign.

Content is carried over from skyi.co.uk (same pages, URLs and copy),
with only typos and obvious copy-paste errors corrected.
Run:  python3 build.py   -> writes HTML files next to this script.
"""
import os
from html import escape

ROOT = os.path.dirname(os.path.abspath(__file__))

PHONE = "07990 487677"
PHONE_HREF = "tel:+447990487677"
EMAIL = "info@skyi.co.uk"
ADDRESS = ["St Helens", "Lancashire", "WA10 3EQ"]

# ------------------------------------------------------------------ icons
ARROW = '<svg viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M1 8h13M9 3l5 5-5 5" stroke="currentColor" stroke-width="1.6"/></svg>'
ARROW_L = '<svg viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M15 8H2M7 3 2 8l5 5" stroke="currentColor" stroke-width="1.6"/></svg>'
CHEV = '<svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="m2 4 4 4 4-4" stroke="currentColor" stroke-width="1.6"/></svg>'
I_PHONE = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>'
I_MAIL = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2" stroke="currentColor" stroke-width="1.7"/><path d="m3 7 9 6 9-6" stroke="currentColor" stroke-width="1.7"/></svg>'
I_PIN = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 21s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12Z" stroke="currentColor" stroke-width="1.7"/><circle cx="12" cy="9" r="2.5" stroke="currentColor" stroke-width="1.7"/></svg>'
RINGS = ('<svg class="cta-rings" viewBox="0 0 560 560" fill="none" aria-hidden="true">'
         + "".join(f'<circle cx="280" cy="280" r="{r}" stroke="#fff" stroke-width="1"/>' for r in (60, 120, 180, 240, 278))
         + '<path d="M280 0v560M0 280h560" stroke="#fff" stroke-width="1"/></svg>')

# ------------------------------------------------------------------ services
SERVICES = [
    dict(slug="roof-inspections", name="Roof Inspections", short="Roof Inspection",
         tag="Roof inspection drone services", img="roof.jpg",
         blurb="Safe, fast aerial roof assessments with full reporting."),
    dict(slug="property-drone-services", name="Property", short="Property",
         tag="Property drone services", img="property.jpg",
         blurb="Inspections, aerial photography and walkthrough video."),
    dict(slug="drone-construction-survey", name="Construction", short="Construction",
         tag="Construction drone services", img="construction.jpg",
         blurb="Surveys, mapping and progress monitoring on site."),
    dict(slug="events-hospitality", name="Events & Hospitality", short="Events & Hospitality",
         tag="Drone services for hospitality & events", img="events.jpg",
         blurb="Aerial event coverage and venue showcases."),
    dict(slug="drone-filming-videography-north-west", name="Marketing Videography", short="Marketing Videography",
         tag="Marketing videography services", img="dji-site.jpg",
         blurb="Brand films and aerial content that sells."),
    dict(slug="weddings", name="Weddings", short="Weddings",
         tag="A wedding day to remember!", img="wedding-champagne.jpg",
         blurb="Cinematic aerial films of your special day."),
]
SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}


# ------------------------------------------------------------------ chrome
def head(title, desc, prefix):
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta name="theme-color" content="#0c1016">
<link rel="icon" href="{prefix}assets/logo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}assets/site.css">
</head>
"""


def header(prefix, current):
    in_services = current in SERVICE_BY_SLUG
    items = "".join(
        f'<a href="{prefix}{s["slug"]}/"{" aria-current=page" if s["slug"] == current else ""}>'
        f'<span class="n">0{i}</span><strong>{escape(s["name"])}</strong><small>{escape(s["blurb"])}</small></a>'
        for i, s in enumerate(SERVICES, 1))

    def cur(slug):
        return ' aria-current="page"' if current == slug else ""

    return f"""<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap bar">
    <a class="brand" href="{prefix}" aria-label="SKYi Drone Photography — home">
      <img src="{prefix}assets/logo.svg" alt="SKYi" width="60" height="60">
    </a>
    <nav class="nav" aria-label="Main">
      <a href="{prefix}"{cur("home")}>Home</a>
      <div class="drop{" current" if in_services else ""}">
        <button type="button" aria-expanded="false" aria-haspopup="true">What We Do {CHEV}</button>
        <div class="drop-panel">{items}</div>
      </div>
      <a href="{prefix}about-us-drone-photography/"{cur("about")}>About Us</a>
      <a href="{prefix}aerial-drone-photgraphy-north-west/"{cur("contact")}>Contact</a>
      <div class="mobile-cta">
        <a class="btn" href="{prefix}aerial-drone-photgraphy-north-west/">Get a Quote {ARROW}</a>
        <a class="btn ghost" href="{PHONE_HREF}">Call {PHONE}</a>
      </div>
    </nav>
    <div class="header-cta">
      <a class="phone" href="{PHONE_HREF}">{PHONE}</a>
      <a class="btn" href="{prefix}aerial-drone-photgraphy-north-west/">Contact Us {ARROW}</a>
      <button class="menu-toggle" type="button" aria-label="Menu" aria-expanded="false"><span></span></button>
    </div>
  </div>
</header>
<main id="main">
"""


def footer(prefix):
    svc = "".join(f'<li><a href="{prefix}{s["slug"]}/">{escape(s["name"])}</a></li>' for s in SERVICES)
    return f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-top">
      <div>
        <img src="{prefix}assets/logo.svg" alt="SKYi" width="72" height="72">
        <p>The North West's premier drone services. Certified pilots, professional equipment and fully insured aerial photography, videography and inspections.</p>
      </div>
      <div><h4>What we do</h4><ul>{svc}</ul></div>
      <div><h4>Company</h4><ul>
        <li><a href="{prefix}">Home</a></li>
        <li><a href="{prefix}about-us-drone-photography/">About Us</a></li>
        <li><a href="{prefix}aerial-drone-photgraphy-north-west/">Contact</a></li>
      </ul></div>
      <div><h4>Get in touch</h4><ul>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="{PHONE_HREF}">{PHONE}</a></li>
        <li><a href="{prefix}aerial-drone-photgraphy-north-west/">{", ".join(ADDRESS)}</a></li>
      </ul></div>
    </div>
    <div class="foot-bottom">
      <span>&copy; 2026 SKYi Drone Photography</span>
      <nav aria-label="Legal">
        <a href="{prefix}terms-of-use/">Terms of Use</a>
        <a href="{prefix}privacy-policy/">Privacy Policy</a>
        <a href="{prefix}cookie-privacy-policy/">Cookie Policy</a>
      </nav>
    </div>
  </div>
</footer>
<script src="{prefix}assets/site.js"></script>
</body>
</html>
"""


def hero(prefix, img, title_html, intro_html, crumbs=None, actions=True, short=False, label="REC"):
    crumb = ""
    if crumbs:
        crumb = '<div class="crumbs">' + ' <span aria-hidden="true">/</span> '.join(crumbs) + '</div>'
    act = ""
    if actions:
        act = f"""<div class="hero-actions">
        <a class="btn" href="#contact">Get a Quote {ARROW}</a>
        <a class="btn ghost" href="{PHONE_HREF}">{PHONE}</a>
      </div>"""
    return f"""
<section class="hero{" short" if short else ""}">
  <div class="hero-media"><img src="{prefix}assets/img/{img}" alt="" fetchpriority="high"></div>
  <div class="wrap hero-inner">
    <h1>{title_html}</h1>
    <div class="hero-foot">
      <p>{intro_html}</p>
      {act}
    </div>
  </div>
</section>
"""


def strip(items):
    lis = "".join(f"<li><b>{i:02d}</b>{escape(t)}</li>" for i, t in enumerate(items, 1))
    return f'<div class="strip"><div class="wrap"><ul>{lis}</ul></div></div>'


def paras(ps):
    if isinstance(ps, str):
        ps = [ps]
    return "".join(f"<p>{p}</p>" for p in ps)


def faq_section(items, title="Frequently Asked Questions", intro="Can't see your question here? Our team is happy to help — just get in touch."):
    rows = ""
    for i, (q, a) in enumerate(items, 1):
        rows += f"""<details{" open" if i == 1 else ""}>
  <summary><span class="n">{i:02d}</span><span>{escape(q)}</span><span class="pm" aria-hidden="true"></span></summary>
  <div class="ans"><p>{escape(a)}</p></div>
</details>"""
    return f"""
<section class="section">
  <div class="wrap faq-wrap">
    <div class="head-col reveal">
      <h2>{escape(title)}</h2>
      <p>{intro}</p>
    </div>
    <div class="faq reveal">{rows}</div>
  </div>
</section>
"""


def contact_section(heading="Contact Us", intro="Here’s how you can contact us for any questions or concerns.", selected=None, white=True):
    chips = "".join(
        f'<label><input type="radio" name="service" value="{escape(s["short"])}"'
        f'{" checked" if s["slug"] == selected else ""} required><span>{escape(s["short"])}</span></label>'
        for s in SERVICES)
    return f"""
<section class="section{" white" if white else ""}" id="contact">
  <div class="wrap contact">
    <div class="info reveal">
      <h2>{escape(heading)}</h2>
      <p>{escape(intro)}</p>
      <ul class="details">
        <li><a href="mailto:{EMAIL}"><span class="ic">{I_MAIL}</span><span><small>Email</small>{EMAIL}</span></a></li>
        <li><a href="{PHONE_HREF}"><span class="ic">{I_PHONE}</span><span><small>Phone</small>{PHONE}</span></a></li>
        <li><div><span class="ic">{I_PIN}</span><span><small>Based in</small>{", ".join(ADDRESS)}</span></div></li>
      </ul>
    </div>
    <form class="form reveal" data-contact novalidate>
      <h3>Contact Form</h3>
      <p>Tell us a little about your project and we’ll get back to you.</p>
      <div class="fields">
        <div class="field"><label for="fn">First Name</label><input id="fn" name="first_name" autocomplete="given-name"></div>
        <div class="field"><label for="ln">Last Name</label><input id="ln" name="last_name" autocomplete="family-name"></div>
        <div class="field full"><label for="em">Email</label><input id="em" name="email" type="email" autocomplete="email"></div>
        <fieldset class="field full"><legend>What Service Are You Interested In? *</legend><div class="chips">{chips}</div></fieldset>
        <div class="field full"><label for="msg">Your Message</label><textarea id="msg" name="message"></textarea></div>
      </div>
      <div class="submit">
        <button class="btn" type="submit">Submit Form {ARROW}</button>
        <span class="note">We usually reply within one working day.</span>
      </div>
      <div class="form-msg" role="status" aria-live="polite"></div>
    </form>
  </div>
</section>
"""


def cta(prefix, title, text, label="Get Started"):
    return f"""
<section class="cta">
  {RINGS}
  <div class="wrap">
    <div class="reveal">
      <h2>{escape(title)}</h2>
      <p>{escape(text)}</p>
    </div>
    <a class="btn reveal" href="{prefix}aerial-drone-photgraphy-north-west/">{escape(label)} {ARROW}</a>
  </div>
</section>
"""


def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path)


# ------------------------------------------------------------------ service template
def service_page(d):
    p = "../"
    s = SERVICE_BY_SLUG[d["slug"]]
    out = head(d["title"], d["desc"], p) + header(p, d["slug"])
    out += hero(p, d["hero"], d["h1"], d["intro"],
                crumbs=[f'<a href="{p}">Home</a>', "What we do", escape(s["name"])])
    out += strip(d["strip"])

    # intro (optional)
    if d.get("lead"):
        out += f"""
<section class="section">
  <div class="wrap split">
    <div class="body reveal">
      <h2>{escape(d["lead"]["h2"])}</h2>
      <p class="big">{d["lead"]["big"]}</p>
      {paras(d["lead"].get("more", []))}
    </div>
    <figure class="frame ratio-43 reveal" style="margin:0"><img src="{p}assets/img/{d["lead"]["img"]}" alt="{escape(d["lead"].get("alt", ""))}" loading="lazy"></figure>
  </div>
</section>
"""

    # expertise blocks
    blocks = ""
    for i, (h, ps) in enumerate(d["expertise"], 1):
        blocks += f'<div class="block reveal"><span class="n">{i:02d}</span><div><h3>{escape(h)}</h3>{paras(ps)}</div></div>'
    out += f"""
<section class="section{" white" if not d.get("lead") else ""}">
  <div class="wrap expertise">
    <div class="sticky reveal">
      <h2>{escape(d["exp_title"])}</h2>
      <p class="lede">{escape(d["exp_lede"])}</p>
      <figure class="frame ratio-45" style="margin-top:36px;margin-bottom:0"><img src="{p}assets/img/{d["exp_img"]}" alt="" loading="lazy"></figure>
    </div>
    <div class="blocks">{blocks}</div>
  </div>
</section>
"""

    # what we do cards (optional)
    if d.get("cards"):
        cards = ""
        for i, (h, img, ps) in enumerate(d["cards"], 1):
            cards += f"""<article class="card reveal">
  <div class="img"><img src="{p}assets/img/{img}" alt="" loading="lazy"><span>{i:02d}</span></div>
  <div class="txt"><h3>{escape(h)}</h3>{paras(ps)}</div>
</article>"""
        out += f"""
<section class="section{" white" if d.get("lead") else ""}">
  <div class="wrap">
    <div class="head reveal">
      <div><h2>{escape(d["cards_title"])}</h2></div>
      <p class="lede">{escape(d["cards_lede"])}</p>
    </div>
    <div class="cards">{cards}</div>
  </div>
</section>
"""

    # benefits
    bens = ""
    for i, (h, ps) in enumerate(d["benefits"], 1):
        bens += f'<div class="benefit reveal"><span class="n">{i:02d} —</span><h3>{escape(h)}</h3>{paras(ps)}</div>'
    out += f"""
<section class="section dark">
  <div class="wrap">
    <div class="head reveal">
      <div><h2>{escape(d.get("ben_title", "Benefits of Working with SKYi"))}</h2></div>
      <p class="lede">CAA-qualified pilots, professional equipment and fully insured operations on every flight.</p>
    </div>
    <div class="benefits">{bens}</div>
  </div>
</section>
"""
    out += faq_section(d["faq"])
    out += contact_section(selected=d["slug"])
    out += cta(p, d["cta"][0], d["cta"][1])
    out += footer(p)
    write(f'{d["slug"]}/index.html', out)


# ------------------------------------------------------------------ pages
ROOF = dict(
    slug="roof-inspections",
    title="Revolutionize Roof Maintenance with SKYi's Drone Inspection Services",
    desc="Revolutionize your roof maintenance with SKYi's Roof Inspection Drone Services. Safe, efficient, and accurate assessments providing detailed reports for proactive maintenance.",
    hero="roof.jpg",
    h1="Roof Inspection <em>Drone</em> Services",
    intro="Where innovation meets roof maintenance. Say goodbye to risky manual inspections and hello to efficient aerial assessments.",
    strip=["No scaffolding or ladders", "High-resolution imagery", "Fast, low-disruption flights", "Detailed written reports"],
    exp_title="A bird’s eye view of your roof",
    exp_lede="With our advanced drone solutions, we provide you with a bird’s eye view of your roof, ensuring thorough inspections and timely maintenance.",
    exp_img="roof-detail.jpg",
    expertise=[
        ("Detailed Roof Assessments", ["Experience detailed roof assessments with SKYi’s Roof Inspection Drone Services.",
                                       "Our drones capture high-resolution imagery, allowing for close-up views of your roof’s surface, identifying potential issues such as cracks, leaks, and wear and tear."]),
        ("Enhanced Safety Measures", ["Prioritise safety with our aerial inspections.",
                                      "SKYi’s drones eliminate the need for personnel to access elevated areas, reducing the risk of accidents and injuries associated with traditional manual inspections."]),
        ("Swift Inspection Process", ["Benefit from a swift inspection process with our drone solutions.",
                                      "Our drones navigate efficiently across your roof, completing inspections in a fraction of the time it would take using traditional methods, minimising disruption to your operations."]),
        ("Comprehensive Reporting", ["Receive comprehensive reporting from SKYi’s Roof Inspection Drone Services.",
                                     "Our detailed reports include imagery, data, and recommendations for maintenance and repair, empowering you to take proactive steps to prolong the lifespan of your roof."]),
    ],
    benefits=[
        ("Expert Guidance and Support", "Receive expert guidance and support from our team of professionals throughout the inspection process, ensuring that you have the assistance you need every step of the way."),
        ("Enhanced Safety Measures", "Prioritise safety with our aerial inspections, minimising the risk of accidents and injuries associated with traditional manual inspections while ensuring the well-being of your personnel and property."),
        ("Actionable Insights", ["Gain actionable insights from our comprehensive reporting, including detailed imagery, data, and recommendations.",
                                 "This empowers you to make informed decisions about maintenance and repairs, optimising the performance and longevity of your roof."]),
        ("Efficiency and Convenience", ["Enjoy the efficiency and convenience of our drone solutions, which provide swift inspections with minimal disruption to your operations.",
                                        "This allows for timely maintenance and repairs, ensuring the continued integrity and functionality of your roof."]),
    ],
    faq=[
        ("How long does it take to inspect a roof using drones?", "The duration of a roof inspection depends on factors such as the size and complexity of the roof. SKYi works efficiently to complete inspections in a timely manner, minimising disruption to your operations."),
        ("Can drones detect leaks and other roof issues?", "Yes, SKYi’s drones are equipped with high-resolution cameras and sensors capable of detecting leaks, cracks, and other roof issues during inspections."),
        ("Are your drone operations compliant with regulations?", "Yes, SKYi adheres to all regulations and guidelines governing drone operations, ensuring compliance and safety at all times. Our team plans flights with minimal disruption, and we ensure that our operations integrate seamlessly with your project."),
        ("How soon can I receive inspection reports after a drone inspection?", "SKYi strives to deliver inspection reports promptly following the completion of drone inspections. The timeframe may vary depending on the scope of the inspection and the level of analysis required."),
        ("Can I request specific areas of focus for the roof inspection?", "Absolutely! SKYi tailors our roof inspection services to meet your specific needs and priorities. You can discuss your requirements with our team, and we’ll ensure that the inspection covers the areas of interest."),
        ("How do I get started with SKYi’s Roof Inspection Drone Services?", "Simply contact our team, and we’ll guide you through the process of scheduling a roof inspection. We’ll discuss your needs, arrange a convenient time for the inspection, and ensure that you receive comprehensive reporting and analysis afterward."),
    ],
    cta=("Ready To Elevate Your Roof Maintenance?", "Contact SKYi now to schedule your Roof Inspection Drone Services and ensure the longevity and integrity of your roof."),
)

PROPERTY = dict(
    slug="property-drone-services",
    title="Expert Property Drone Services for Optimal Management | SKYi",
    desc="Maximize property potential with SKYi's advanced drone solutions. Aerial inspections, photography, security monitoring & more. Elevate property management today.",
    hero="property.jpg",
    h1="Property <em>Drone</em> Services",
    intro="Where innovation meets property management. Maximise the potential of your properties with our advanced drone solutions.",
    strip=["CAA qualified pilots", "HNC in Construction", "Gold CSCS card holders", "Detailed reports, not just video"],
    lead=dict(label="Discover our expertise", h2="Discover Our Expertise in our Property Drone Services",
              big="From comprehensive inspections to stunning aerial photography, SKYi empowers you to manage your properties with efficiency and precision.",
              img="home-drone.jpg", alt="Aerial view of a detached house and garden", cap="SKYi · residential survey"),
    exp_title="Aerial insight for every property",
    exp_lede="Inspections, imagery and monitoring that help you manage, market and protect your properties.",
    exp_img="property-1.jpg",
    expertise=[
        ("Aerial Inspections. Facade Inspections.", ["Experience comprehensive aerial inspections of your properties with SKYi’s Drone Services. We are CAA qualified, and our pilots are also construction professionals with an HNC in Construction and Gold CSCS cards. So we don’t just take nice videos — we give you detailed reports.",
                                                     "Our drones capture high-resolution imagery, allowing for detailed assessments of property conditions, structural integrity, and potential maintenance needs."]),
        ("Stunning Aerial Drone Photography", ["Showcase your properties from a unique perspective with our stunning aerial photography services.",
                                               "Our drones capture breathtaking aerial views, perfect for marketing materials, property listings, and promotional purposes."]),
        ("Enhanced Security Monitoring", ["Ensure the security of your properties with our enhanced monitoring capabilities.",
                                          "SKYi’s drones provide real-time surveillance, monitoring property perimeters, identifying potential security breaches, and deterring unauthorised access."]),
        ("Efficient Property Management", ["Streamline your property management processes with our efficient drone solutions.",
                                           "From land surveying to construction progress monitoring, SKYi’s drones provide valuable insights to optimise property operations and decision-making."]),
    ],
    cards_title="Services for property owners, agents and managers",
    cards_lede="From marketing imagery to insurance documentation — everything you need, captured from above.",
    cards=[
        ("Drone Photography and Video Services", "dji-site.jpg", ["Where innovation meets visual storytelling. Elevate your property marketing efforts with breathtaking aerial views captured by our advanced drone technology.",
                                                                "From stunning photography to captivating videos, SKYi empowers you to showcase your property in its best light."]),
        ("Walkthrough Video Services", "property-2.jpg", ["Where virtual exploration meets property showcasing. Immerse potential buyers or tenants in your property with captivating walkthrough videos captured by our skilled drone pilots.",
                                                         "Experience the convenience of showcasing your property virtually, allowing viewers to explore every corner from anywhere in the world."]),
        ("Extensions Timelapse Services", "property-3.jpg", ["Every moment of your project’s evolution is captured in stunning detail.",
                                                            "From groundbreaking to completion, our timelapse videos provide a mesmerising visual journey, allowing you to witness progress unfold in real-time."]),
        ("Insurance Damage Drone Services", "c-damage.jpg", ["Your partner in efficiently assessing and documenting property damage for insurance claims.",
                                                            "With our advanced drone technology, we provide comprehensive aerial inspections and detailed documentation to streamline the insurance claims process and ensure that your assets are protected."]),
    ],
    benefits=[
        ("Expert Guidance and Support", "Access expert guidance and support from our experienced team throughout the property drone service process, ensuring that you receive personalised assistance every step of the way."),
        ("Enhanced Safety Measures", "Prioritise safety with our aerial inspections, reducing the need for personnel to access elevated areas and minimising the risk of accidents associated with traditional methods."),
        ("Actionable Insights", "Receive actionable insights from our comprehensive reports, including detailed imagery, data, and recommendations. This empowers you to make informed decisions about property maintenance, repairs, and optimisation."),
        ("Efficiency and Convenience", "Enjoy the efficiency and convenience of our drone solutions, which provide swift inspections with minimal disruption to your operations. This allows for timely property management decisions and optimisations."),
    ],
    faq=[
        ("Can drones be used for property inspections in all weather conditions?", "SKYi’s drones are equipped to operate in a variety of weather conditions, including light rain and moderate wind. However, severe weather conditions may impact drone operations and require rescheduling of inspections."),
        ("How far in advance should I schedule property drone services?", "It is recommended to schedule property drone services at least a few weeks in advance to ensure availability and accommodate any specific requirements or preferences."),
        ("Can I request specific areas of focus for property inspections?", "Absolutely! SKYi tailors property drone services to meet your specific needs and priorities. You can discuss your requirements with our team, and we’ll ensure that the inspection covers the areas of interest."),
        ("Are your drone operations compliant with regulations?", "Yes, SKYi adheres to all regulations and guidelines governing drone operations, ensuring compliance and safety at all times."),
        ("How quickly can I receive inspection reports after a property drone service?", "SKYi strives to deliver inspection reports promptly following the completion of drone services. The timeframe may vary depending on the scope of the service and the level of analysis required."),
        ("Can property drone services be customised for commercial and residential properties?", "Yes, SKYi offers property drone services tailored to both commercial and residential properties, providing customised solutions to meet the unique needs of each property type."),
    ],
    cta=("Ready to elevate your property management?", "Contact SKYi now to schedule your Property Drone Services and unlock the full potential of your properties."),
)

CONSTRUCTION = dict(
    slug="drone-construction-survey",
    title="Boost Efficiency with SKYi Precision Construction Drone Services",
    desc="Elevate your construction project with SKYi aerial insights for precision and efficiency. Capture high-res imagery, monitor progress, and ensure site safety with ease.",
    hero="construction.jpg",
    h1="Construction <em>Drone</em> Services",
    intro="Aerial Insights for Every Phase of Your Project.",
    strip=["Qualified site managers", "Experienced surveyors", "Mapping & progress monitoring", "Detailed inspection reports"],
    lead=dict(label="Discover our aerial flying expertise", h2="Build with confidence, clarity, and control",
              big="Welcome to SKYi’s Construction Drone Services – where innovation meets construction. Elevate your project with aerial insights that redefine precision and efficiency. From groundbreaking to completion, SKYi empowers you to build with confidence, clarity, and control.",
              more=["Our surveyors are vastly experienced in all stages of development and construction, so we know what to look for and compile detailed reports and inspections. All are qualified site managers and surveyors."],
              img="c-waste.jpg", alt="Aerial view of a waste transfer site captured by SKYi", cap="SKYi · site survey"),
    exp_title="From groundbreaking to completion",
    exp_lede="Survey, monitor, inspect and showcase your site — all from a single flight programme.",
    exp_img="c-tall.jpg",
    expertise=[
        ("Site Drone Surveying and Mapping", "Gain a comprehensive overview of your construction site with SKYi’s precise surveying and mapping capabilities. Our drones capture high-resolution imagery and generate detailed maps, providing invaluable insights for planning and decision-making."),
        ("Progress Monitoring", "Track the progress of your construction project with real-time aerial footage. SKYi’s drones offer regular updates and detailed visual documentation, allowing you to monitor milestones, identify potential issues, and optimise workflow efficiency."),
        ("Safety and Compliance", "Ensure safety and compliance on your construction site with SKYi’s aerial inspections. Our drones conduct thorough inspections of hard-to-reach areas, minimising risk and ensuring adherence to regulations."),
        ("Marketing and Showcase", "Showcase your construction projects in stunning detail with SKYi’s drone aerial photography and videography services. From promotional materials to client presentations, our aerial perspectives enhance your marketing efforts and elevate your brand image."),
    ],
    cards_title="Specialist construction services",
    cards_lede="Seven ways SKYi supports developers, contractors and site teams.",
    cards=[
        ("Site Inspections", "c-site.jpg", ["Site Inspection Drone Services – where precision meets perspective.",
                                           "Empower your site inspections with aerial insights that redefine safety, efficiency, and decision-making. From remote areas to hard-to-reach locations, SKYi delivers clarity from above, ensuring comprehensive assessments and actionable insights."]),
        ("Safety/Security Surveys", "c-security.jpg", ["Protect your assets, enhance security measures, and mitigate risks with our advanced drone solutions.",
                                                      "From perimeter monitoring to hazard detection, SKYi empowers you to safeguard your future from above."]),
        ("Time Lapse Photos", "dji-site.jpg", ["Step into the realm of time with SKYi’s Drone Time-Lapse Photography. Witness the world unfolding before your eyes, captured in mesmerising detail from above.",
                                              "Let SKYi redefine your perception of time with our unparalleled aerial perspectives."]),
        ("Facade Surveys", "construction.jpg", "Transform the facade of your building with our advanced drone surveys, capturing detailed insights to enhance aesthetics, safety, and structural integrity."),
        ("Tall Structures", "c-tall.jpg", ["Take your inspection and maintenance efforts to new heights with our specialised drone solutions.",
                                          "From towering skyscrapers to expansive bridges, SKYi empowers you to ensure the safety and integrity of tall structures with precision and efficiency."]),
        ("Damage Surveys", "c-damage.jpg", "When disaster strikes, time is of the essence. SKYi’s advanced drone solutions enable swift and comprehensive damage assessment, empowering you to assess, address, and recover with efficiency and precision."),
        ("Insurance", "c-insurance.jpg", ["Drone Insurance Services – Safeguard your investment and mitigate risks with our comprehensive insurance coverage tailored specifically for drone operators.",
                                         "With SKYi, fly with confidence knowing that your drones are protected against unforeseen accidents and incidents."]),
    ],
    benefits=[
        ("Precision and Accuracy", "SKYi’s drones provide precise data and insights, empowering you to make informed decisions and optimise project efficiency."),
        ("Efficiency and Cost Savings", "Streamline your construction processes and reduce costs with SKYi’s efficient aerial solutions. From surveying to monitoring, our services save time and resources."),
        ("Safety and Compliance Assurance", "Prioritise safety on your construction site with SKYi’s aerial inspections. Identify potential hazards and ensure compliance with regulations, minimising risk and liability."),
        ("Enhanced Marketing and Branding", "Showcase your projects with captivating aerial photography and videography. SKYi’s aerial perspectives help you stand out in a competitive market and attract clients with visually compelling content."),
    ],
    faq=[
        ("How often do you provide progress updates?", "We offer flexible scheduling for progress updates based on your project timeline and requirements. Our team works closely with you to establish a monitoring frequency that aligns with your needs."),
        ("Can I choose the intervals between time-lapse frames?", "Yes, SKYi provides customisable options for interval timing, allowing you to tailor the time-lapse sequence to your preferences."),
        ("How long does it take to generate maps and survey data?", "The time required to generate maps and survey data depends on the size and complexity of the site. We strive to deliver results promptly while maintaining accuracy and quality."),
        ("Are your drone operations compliant with regulations?", "Yes, SKYi adheres to all regulations and guidelines governing drone operations. Our pilots are certified and trained to ensure compliance and safety at all times."),
        ("Can I use aerial footage for marketing purposes?", "Absolutely! SKYi’s aerial photography and videography services provide stunning visuals that can be used for marketing, presentations, and promotional materials."),
        ("How do I get started with SKYi’s Construction Drone Services?", "Simply contact our team, and we’ll guide you through the process of assessing your needs, planning the scope of work, and scheduling drone operations for your construction project."),
    ],
    cta=("Do you have a construction project?", "Contact SKYi now to explore our Construction Drone Services and unlock the power of aerial insights."),
)

EVENTS = dict(
    slug="events-hospitality",
    title="Elevate Special Events with SKYi Drone Photography Services",
    desc="Elevate events with SKYi drone photos. We plan, capture and film the event, showcase venues, and create unforgettable memories with stunning aerial footage.",
    hero="events.jpg",
    h1="Drone Photography for <em>Hospitality</em> &amp; Events",
    intro="We capture stunning aerial footage and photography to create unforgettable memories for your guests and showcase your venue in its best light.",
    strip=["Licensed & insured pilots", "Indoor & outdoor coverage", "Customisable packages", "Professional editing"],
    lead=dict(label="Discover our expertise", h2="Plan it. Capture it. Film it.",
              big="We plan, capture and film your event, showcase your venue, and create unforgettable memories with stunning aerial footage.",
              more=["From celebrations to corporate gatherings, SKYi brings a new perspective to every occasion."],
              img="e-stadium.jpg", alt="Aerial view of a stadium event", cap="SKYi · event coverage"),
    exp_title="Events seen from a new angle",
    exp_lede="Coverage, venue showcases and finished films — tailored to your event and budget.",
    exp_img="e-field.jpg",
    expertise=[
        ("Aerial Event Coverage", ["Experience comprehensive aerial coverage of your events with our drone services.",
                                   "From celebrations to corporate gatherings, our drones capture dynamic footage that highlights the excitement and atmosphere of your event from unique perspectives."]),
        ("Stunning Venue Showcases", ["Showcase your venue in all its glory with stunning aerial photography.",
                                      "Our drones capture breathtaking views of your venue’s architecture, landscaping, and surroundings, allowing potential clients to envision their events in your space."]),
        ("Customisable Packages", ["Choose from a range of customisable packages to suit your event’s specific needs and budget.",
                                   "Whether you’re hosting an intimate gathering or a grand celebration, SKYi offers flexible solutions tailored to your requirements."]),
        ("Professional Editing and Production", ["Benefit from professional editing and production services for your aerial footage and photography.",
                                                 "Our skilled team enhances and refines the captured content to ensure that it perfectly reflects the ambience and essence of your event and venue."]),
    ],
    cards_title="Events we cover",
    cards_lede="From the pitch to the boardroom — dynamic aerial coverage for every kind of event.",
    cards=[
        ("Drone Services for Sporting Activities", "e-sports.jpg", ["Thrilling moments, captured from breathtaking aerial perspectives.",
                                                                    "With our advanced drone technology, we provide dynamic coverage of sporting events, showcasing the excitement and energy of the action like never before."]),
        ("Corporate Events", "e-corporate.jpg", ["Where professionalism meets innovation.",
                                                 "With our cutting-edge drone technology, we elevate corporate events to new heights, providing dynamic coverage and captivating visuals that impress clients, partners, and attendees alike."]),
        ("Shows/Markets", "e-markets.jpg", ["Vibrant atmospheres are captured from breathtaking aerial perspectives.",
                                           "With our advanced drone technology, we bring a new dimension to your shows and markets, providing dynamic coverage and immersive visuals that captivate attendees and viewers alike."]),
        ("Charity Events", "e-charity.jpg", ["Meaningful moments are captured from inspiring perspectives.",
                                             "With our innovative drone technology, we bring a new dimension to your charity events, providing captivating coverage that elevates awareness and support for your cause."]),
        ("Field Events", "e-field.jpg", ["Outdoor excitement is captured from breathtaking aerial perspectives.",
                                         "With our cutting-edge drone technology, we bring a new dimension to your field events, providing dynamic coverage that showcases the energy and enthusiasm of participants."]),
        ("Stadium Events", "e-stadium.jpg", ["The excitement of the stadium comes to life from breathtaking aerial perspectives.",
                                             "With our state-of-the-art drone technology, we provide dynamic coverage that enhances the spectacle of stadium events, captivating audiences and elevating the overall experience."]),
    ],
    benefits=[
        ("Unforgettable Memories", "SKYi’s Drone Services for Hospitality create unforgettable memories for your guests, capturing the excitement and atmosphere of your events from breathtaking aerial perspectives."),
        ("Venue Showcase", "Showcase your venue in its best light with stunning aerial photography, highlighting its unique features and surroundings to attract potential clients and set your venue apart from the competition."),
        ("Customisation", "Customise your drone service packages to meet your event’s specific needs and budget, ensuring that you receive the perfect solution for capturing your event and showcasing your venue."),
        ("Professional Production", "Benefit from professional editing and production services for your aerial footage and photography, ensuring that it is refined and polished to perfection to reflect the ambience and essence of your event and venue."),
    ],
    faq=[
        ("Can drones be used indoors for event coverage?", "Yes, SKYi’s drones can be used indoors for event coverage, provided that the venue’s layout and regulations allow for safe drone operations."),
        ("Can I request specific shots or angles for my event coverage?", "Absolutely! SKYi accommodates specific requests for shots or angles to ensure that your event coverage captures the key moments and perspectives that are important to you."),
        ("How long does it take to receive the edited footage and photography after an event?", "The timeframe for receiving edited footage and photography depends on factors such as the duration of the event and any specific editing requests. However, we strive to deliver the final content promptly to meet your needs."),
        ("Can I use the aerial footage and photography for marketing purposes?", "Yes, the aerial footage and photography captured by SKYi’s drones are perfect for marketing purposes, including promotional materials, social media, websites, and advertising campaigns."),
        ("Are your drone pilots licensed and insured?", "Yes, all of SKYi’s drone pilots are licensed and insured, ensuring compliance with regulations and safety standards for aerial operations."),
        ("How do I get started with scheduling Drone Services for Hospitality with SKYi?", "Simply contact us to discuss your event coverage and venue showcasing needs, and we’ll work with you to customise a drone service package that meets your requirements and exceeds your expectations."),
    ],
    cta=("Planning an event?", "Contact SKYi to discuss your event coverage and venue showcase, and we’ll build a drone package around your plans."),
)

MARKETING = dict(
    slug="drone-filming-videography-north-west",
    title="Elevate Your Brand with SKYi's Expert Marketing Videography Services",
    desc="Capture your brand's essence with SKYi's professional videography. Elevate your marketing with high-quality videos, creative concepts, and strategic content distribution.",
    hero="dji-site.jpg",
    h1="Marketing <em>Videography</em>",
    intro="The essence of your brand comes to life through captivating visuals.",
    strip=["Product demos & brand stories", "Concept & storyboarding", "Content for every channel", "Measurable results"],
    lead=dict(label="Visual storytelling", h2="Show what makes your business different",
              big="With our professional videography expertise, we help businesses showcase their products, services, and values in a way that resonates with their target audience and elevates their marketing efforts.",
              img="marketing-2.jpg", alt="", cap="SKYi · brand film"),
    exp_title="From concept to camera to campaign",
    exp_lede="A complete video service — planned around your brand and measured against your goals.",
    exp_img="marketing.jpg",
    expertise=[
        ("High-Quality Video Production", ["Experience high-quality video production with SKYi’s professional videography services.",
                                           "From product demos to brand stories, we deliver visually stunning content that captures the attention of your audience and effectively communicates your message."]),
        ("Creative Concept Development", ["Collaborate with our team to develop creative concepts for your marketing videos.",
                                          "Whether you’re launching a new product or promoting a special offer, we work closely with you to brainstorm ideas that align with your brand identity and marketing objectives."]),
        ("Strategic Content Distribution", ["Strategically distribute your marketing videos across various platforms and channels.",
                                            "We help you reach your target audience effectively by optimising your video content for social media, websites, email campaigns, and other marketing channels."]),
        ("Measurable Results and ROI", ["Track the performance of your marketing videos and measure their impact on your business.",
                                        "With analytics and reporting tools, we provide valuable insights into viewer engagement, conversion rates, and return on investment, allowing you to refine your marketing strategies for maximum effectiveness."]),
    ],
    benefits=[
        ("Expertise and Experience", ["Benefit from the expertise and experience of SKYi’s videography team.",
                                      "Our skilled professionals have years of experience in crafting compelling visual content that resonates with audiences and drives engagement, ensuring that your marketing videos are of the highest quality."]),
        ("Customisation and Personalisation", ["Enjoy customised and personalised service tailored to your specific needs and preferences.",
                                               "At SKYi, we understand that every brand is unique, and we work closely with you to create videos that reflect your brand’s personality, values, and goals."]),
        ("Efficiency and Timeliness", ["Experience efficient and timely delivery of your marketing videos.",
                                       "Our streamlined production process and dedicated project management ensure that your videos are completed on schedule and within budget, allowing you to meet your marketing deadlines and objectives effectively."]),
        ("Strategic Guidance and Support", ["Receive strategic guidance and support throughout the video production process.",
                                            "From initial concept development to final distribution, our team provides valuable insights and recommendations to optimise your video marketing strategy and maximise the ROI of your investment in videography services."]),
    ],
    faq=[
        ("What types of marketing videos can SKYi produce?", "SKYi can produce a wide range of marketing videos, including product demos, brand stories, promotional videos, explainer videos, testimonial videos, and more."),
        ("How long does it take to produce a marketing video?", "The production timeline for a marketing video depends on factors such as the complexity of the project, the length of the video, and any specific requirements. Our team works efficiently to deliver high-quality videos within agreed-upon timelines."),
        ("Can I provide input and feedback during the video production process?", "Absolutely! We value your input and feedback throughout the video production process and strive to collaborate closely with you to achieve your vision for the final product."),
        ("Can SKYi help with scriptwriting and storyboarding for marketing videos?", "Yes, our team can assist with scriptwriting and storyboarding to ensure that your marketing videos effectively communicate your message and resonate with your target audience."),
        ("How can I track the performance of my marketing videos?", "SKYi provides analytics and reporting tools to track the performance of your marketing videos, including metrics such as viewer engagement, conversion rates, and return on investment."),
        ("How do I get started with scheduling Videography Services with SKYi?", "Simply contact us to discuss your videography needs, and we’ll work with you to develop a customised plan that meets your requirements and exceeds your expectations."),
    ],
    cta=("Ready to bring your brand to life?", "Contact SKYi to discuss your videography needs and we’ll develop a customised plan for your next campaign."),
)

WEDDINGS = dict(
    slug="weddings",
    title="Capture Love & Laughter with SKYi's Cinematic Wedding Videography",
    desc="Transform your special day into a cinematic masterpiece! Experience professional editing, personalised wedding film packages, and seamless delivery with SKYi's wedding videography services.",
    hero="wedding-champagne.jpg",
    h1="Make Your Wedding <em>Unforgettable!</em>",
    intro="Every moment of your special day is captured with care and precision.",
    strip=["Cinematic aerial storytelling", "Personalised packages", "Professional editing", "Delivered in your format"],
    lead=dict(label="Wedding drone videography", h2="A timeless cinematic masterpiece",
              big="With our professional drone videography expertise, we turn your wedding day into a timeless cinematic masterpiece, preserving the love, laughter, and cherished memories for years to come.",
              img="wedding-ceremony.jpg", alt="Outdoor wedding ceremony", cap="SKYi · weddings"),
    exp_title="Your love story, from above",
    exp_lede="From the vows to the first dance — a different view of the day you’ll want to relive forever.",
    exp_img="about-3.jpg",
    expertise=[
        ("Cinematic Storytelling", ["Experience cinematic storytelling with SKYi’s wedding videography services. Forget any preconceptions of drones being toy planes for adults. Drone wedding photography is on the rise and it’s not exactly hard to see why.",
                                    "Thanks to the ever-changing world of technology, today’s drones can capture truly spectacular aerial wedding photographs that you’ll want to treasure forever. However, just as you would ask a wedding photographer questions, there are certain things you need to know about hiring a wedding drone.",
                                    "Just send our form or give us a call any time to speak personally to our expert team at SKYi, who can tell you everything you need to know about hiring a drone for your wedding.",
                                    "From the emotional exchange of vows to the joyous celebration with friends and family, we craft a different, aerial view of the narrative that captures the essence of your love story, creating a keepsake forever."]),
        ("Personalised Packages", ["Choose from a range of personalised packages tailored to your unique needs and preferences.",
                                   "Whether you prefer a highlight reel of the day’s highlights or full-length coverage of every moment, we offer customisable options to suit your vision and budget."]),
        ("Professional Editing", ["Enjoy professional editing that enhances the beauty and emotion of your wedding footage.",
                                  "Our skilled editors work their magic to create a polished and seamless final product, incorporating special effects, music, and personalised touches to elevate the viewing experience."]),
        ("Seamless Delivery", ["Receive your wedding videos with ease and convenience.",
                               "We ensure seamless delivery of your final videos in the format of your choice, allowing you to relive the magic of your special day whenever and wherever you desire."]),
    ],
    ben_title="Benefits of Working with SKYi Drone Services",
    benefits=[
        ("Memorable Storytelling", ["SKYi’s Wedding Drone Videography Services offer more than just footage; we craft a narrative that captures the essence of your love story.",
                                    "With skilled storytelling techniques, we ensure that every moment of your special day is portrayed in a way that evokes emotion and creates lasting memories."]),
        ("Tailored Experience", ["Experience personalised service tailored to your unique vision and preferences.",
                                 "From the style of coverage to the final editing touches, we collaborate closely with you to ensure that your wedding videos reflect your individuality and showcase what matters most to you."]),
        ("Professional Expertise", ["Benefit from the expertise of our professional videography team.",
                                    "With years of experience in the industry, we know how to capture the beauty and emotion of your wedding day with precision and artistry, delivering high-quality videos that exceed your expectations."]),
        ("Peace of Mind", ["Enjoy peace of mind knowing that your wedding memories are in good hands.",
                           "From the moment you book our services to the delivery of your final videos, we handle every aspect of the process with care and attention to detail, ensuring a seamless and stress-free experience for you."]),
    ],
    faq=[
        ("How far in advance should I book SKYi’s Wedding Videography Services?", "We recommend booking as early as possible to secure your date, as our availability can fill up quickly, especially during peak wedding seasons."),
        ("Can I customise my wedding videography package?", "Absolutely! We offer personalised packages tailored to your unique needs and preferences, allowing you to choose the coverage, style, and additional services that best suit your vision and budget."),
        ("Will there be multiple videographers at my wedding?", "Depending on the package you choose and the size of your wedding, we may provide multiple videographers to ensure comprehensive coverage of your special day."),
        ("How long will it take to receive my wedding videos after the event?", "The editing process typically takes 4-8 weeks, depending on the complexity of the project and our current workload. We strive to deliver your final videos as quickly as possible without compromising quality."),
        ("Can I request specific shots or moments to be captured during my wedding?", "Absolutely! We welcome your input and will work closely with you to capture the moments and details that are most important to you, ensuring that your wedding videos reflect your vision and preferences."),
    ],
    cta=("Planning your big day?", "Send us your date and we’ll tell you everything you need to know about having a drone at your wedding."),
)


# ------------------------------------------------------------------ home
def home():
    p = ""
    out = head("Drone Photography & Videography Services NORTH WEST",
               "Professional drone services in the North West and Cheshire. Certified pilots. Pro equipment. Stunning aerial footage, roof inspections, event coverage and more!", p)
    out += header(p, "home")
    out += hero(p, "home-why.jpg",
                "Welcome to SKYi — The North West’s Premier <em>Drone</em> Services",
                "Discover top-notch aerial solutions tailored for your needs. Precision, safety, and expertise.",
                crumbs=["Skyi Drone Videography"])
    out += strip(["Certified & experienced pilots", "Top-of-the-line equipment", "Safe & fully insured", "North West & Cheshire"])

    tiles = f"""<div class="tile intro">
  <span class="n">SKYi</span>
  <div><h3>Elevate Your Perspective with SKYi</h3><a class="text-link" href="#services">Discover how we can help {ARROW}</a></div>
</div>"""
    for i, s in enumerate(SERVICES, 1):
        tiles += f"""<a class="tile" href="{s["slug"]}/">
  <img src="assets/img/{s["img"]}" alt="" loading="lazy">
  <span class="n">0{i}</span>
  <div><h3>{escape(s["name"])}</h3><small>{escape(s["tag"])}</small></div>
  <span class="go">{ARROW}</span>
</a>"""
    out += f"""
<section class="section">
  <div class="wrap">
    <div class="rail-head reveal">
      <div><h2>What We Do</h2></div>
      <div class="rail-ctrl" data-rail="rail">
        <button type="button" data-dir="prev" aria-label="Previous">{ARROW_L}</button>
        <button type="button" data-dir="next" aria-label="Next">{ARROW}</button>
      </div>
    </div>
    <div class="rail" id="rail">{tiles}</div>
  </div>
</section>

<section class="section white">
  <div class="wrap split">
    <div class="body reveal">
      <h2>Drone Photography &amp; Videography Experts</h2>
      <p class="big">At SKYi, we pride ourselves on attention to detail and capturing the essence of any event or location from above.</p>
      <p>With our top-of-the-line equipment and certified pilots, we offer safe and fully insured services for surveying, filming, and documenting.</p>
      <p>We started with a passion for capturing stunning aerial footage and have grown into a trusted name in the industry.</p>
      <p>Our expertise and commitment to excellence have made us the go-to choice for bringing visions to life.</p>
    </div>
    <figure class="frame ratio-43 reveal" style="margin:0"><img src="assets/img/home-drone.jpg" alt="Aerial photograph of a house captured by SKYi" loading="lazy"></figure>
  </div>
  <div class="wrap" style="margin-top:clamp(56px,7vw,96px)">
    <ul class="features reveal" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));column-gap:40px">
      <li><span><h3>Top-of-the-Line Equipment</h3><p>We use the latest technology to capture high-quality aerial footage and photographs.</p></span></li>
      <li><span><h3>Certified and Experienced Pilots</h3><p>Our team of pilots is skilled and experienced in capturing the perfect shots from the sky.</p></span></li>
      <li><span><h3>Attention to Detail</h3><p>We believe in capturing the essence and beauty of every event or location, paying attention to even the smallest details.</p></span></li>
    </ul>
  </div>
</section>
"""
    rows = ""
    for i, s in enumerate(SERVICES, 1):
        rows += f"""<a href="{s["slug"]}/">
  <span class="n">0{i}</span><span class="t">{escape(s["name"])}</span>
  <span class="more"><span>Learn more</span> {ARROW}</span>
  <span class="peek"><img src="assets/img/{s["img"]}" alt="" loading="lazy"></span>
</a>"""
    out += f"""
<section class="section dark" id="services">
  <div class="wrap">
    <div class="head reveal">
      <div><h2>Our Services</h2></div>
    </div>
    <nav class="index reveal" aria-label="Services">{rows}</nav>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="why reveal">
      <div class="media"><img src="assets/img/hero-waste-site.jpg" alt="Aerial view of an industrial site captured by SKYi" loading="lazy"></div>
      <div class="txt">
        <h2>Why Choose SKYi?</h2>
        <p>Our commitment to quality and exceptional customer service sets us apart from the competition.</p>
        <ul class="features">
          <li><span><h3>Breathtaking Aerial Footage</h3><p>Our team of skilled professionals possess unmatched expertise in their respective fields, ensuring that you receive the highest level of service.</p></span></li>
          <li><span><h3>Safe and Insured Services</h3><p>You can trust our certified pilots and fully insured services for a worry-free aerial photography and videography experience.</p></span></li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""
    out += faq_section([
        ("How long does it take to capture a time-lapse sequence?", "The duration of the time-lapse sequence depends on the specific requirements of your project. We'll work closely with you to establish a timeframe that meets your needs."),
        ("Can I choose the intervals between frames?", "Yes, SKYi provides customisable options for interval timing, allowing you to tailor the time-lapse sequence to your preferences."),
        ("Are the drone flights disruptive to regular operations?", "Our team plans flights with minimal disruption, prioritising safety and adherence to regulations. We ensure that our operations integrate seamlessly with your project."),
        ("What types of projects are suitable for Drone Time-Lapse Photography?", "Our services are suitable for a wide range of projects, including construction progress monitoring, landscape documentation, event coverage, and more."),
        ("Is post-processing included in the service?", "Yes, SKYi provides comprehensive services, including post-processing to enhance and refine your time-lapse sequences."),
        ("Can I view samples of previous time-lapse projects?", "Certainly! Contact our team, and we'll be happy to share examples of our stunning time-lapse photography work."),
    ], title="FAQ’s")
    out += contact_section()
    out += cta(p, "Let’s Create Together", "Connect with us to explore how we can make your vision a reality.")
    out += footer(p)
    write("index.html", out)


# ------------------------------------------------------------------ about
def about():
    p = "../"
    out = head("SKYi: Expert Drone Photography and Videography Services",
               "Unleash the power of visual storytelling with SKYi's state-of-the-art drone photography and videography. Our certified pilots and high-quality equipment deliver breathtaking aerial captures.", p)
    out += header(p, "about")
    out += hero(p, "about-1.jpg", "About <em>Us</em>",
                "Founded by Professionals in Construction and Marketing, SKYi offers enhanced perspective to aerial photography and videography.",
                crumbs=[f'<a href="{p}">Home</a>', "About us"], short=True)
    out += f"""
<section class="section">
  <div class="wrap split">
    <div class="body reveal">
      <h2>Certified pilots. Construction and marketing know-how.</h2>
      <p class="big">With years of experience and expertise in the field, our team of certified pilots ensures precise and stunning aerial captures. Our top-of-the-line equipment enables us to deliver high-quality footage and photographs that truly capture the essence of any event or location.</p>
      <p>Over the years, we have had the privilege of serving a diverse range of clients, including event organisers, real estate developers, construction companies, and more. Our dedication to excellence and commitment to customer satisfaction have earned us a loyal client base.</p>
    </div>
    <div class="mosaic reveal">
      <img src="{p}assets/img/hero-waste-site.jpg" alt="Aerial view of an industrial site" loading="lazy">
      <img src="{p}assets/img/about-3.jpg" alt="" loading="lazy">
      <img src="{p}assets/img/about-2.jpg" alt="" loading="lazy">
      <img src="{p}assets/img/about-4.jpg" alt="" loading="lazy">
    </div>
  </div>
  <div class="wrap" style="margin-top:clamp(56px,7vw,96px)">
    <ul class="features reveal" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));column-gap:40px">
      <li><span><h3>Top-of-the-Line Equipment</h3><p>We use the latest technology to capture high-quality aerial footage and photographs.</p></span></li>
      <li><span><h3>Certified and Experienced Pilots</h3><p>Our team of pilots is skilled and experienced in capturing the perfect shots from the sky.</p></span></li>
      <li><span><h3>Attention to Detail</h3><p>We believe in capturing the essence and beauty of every event or location, paying attention to even the smallest details.</p></span></li>
    </ul>
  </div>
</section>

<section class="section dark">
  <div class="wrap">
    <div class="vm">
      <div class="reveal"><h3>Our Vision</h3><p>Our vision is to revolutionise visual storytelling by elevating perspectives and capturing moments from the sky that resonate with emotions and create lasting memories.</p></div>
      <div class="reveal"><h3>Our Mission</h3><p>Our mission is to provide safe, reliable, and fully insured drone photography and videography services that exceed our clients’ expectations. We strive to consistently deliver breathtaking aerial footage and photographs that bring our clients’ visions to life.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="head reveal">
      <div><h2>Our Process</h2></div>
      <p class="lede">At SKYi Drone Photography, we have a streamlined process to ensure that your aerial photography and videography needs are met with efficiency and precision. From the initial consultation to the final touches, we work with you every step of the way to ensure that your vision is brought to life.</p>
    </div>
    <ol class="process reveal">
      <li><h3>Pre-flight Planning</h3><p>Our team of experts will work with you to plan out every detail of your aerial shoot, including flight plans, equipment needs, and safety precautions.</p></li>
      <li><h3>On-Site Drone Management</h3><p>Our team of experienced pilots and photographers will execute your aerial shoot with precision and attention to detail.</p></li>
      <li><h3>Photography and Videography</h3><p>Using state-of-the-art drones and equipment, we capture stunning aerial footage and images for your project or event.</p></li>
      <li><h3>Post-Production</h3><p>We use cutting-edge software and technology to edit and enhance your aerial footage and images, ensuring that the final product is of the highest quality.</p></li>
    </ol>
  </div>
</section>
"""
    out += contact_section()
    out += cta(p, "Let’s Create Together", "Connect with us to explore how we can make your vision a reality. Join us in shaping the future.")
    out += footer(p)
    write("about-us-drone-photography/index.html", out)


# ------------------------------------------------------------------ contact
def contact():
    p = "../"
    out = head("Explore Creative Solutions & Innovate with Skyi.UK",
               "Discover a world of tailored creative solutions with Skyi. Connect with us today and let's shape the future together. Get in touch now!", p)
    out += header(p, "contact")
    out += hero(p, "contact.jpg", "Get In <em>Touch</em>",
                "Explore a world of creative solutions and innovation tailored to your needs.",
                crumbs=[f'<a href="{p}">Home</a>', "Contact"], actions=False, short=True)
    out += contact_section(heading="Send Us a Message", intro="Here’s how you can contact us for any questions.", white=False)
    out += cta(p, "Let’s Create Together", "Connect with us to explore how we can make your vision a reality. Join us in shaping the future.")
    out += footer(p)
    write("aerial-drone-photgraphy-north-west/index.html", out)


# ------------------------------------------------------------------ legal
LEGAL_NAV = [("terms-of-use", "Terms of Use"), ("privacy-policy", "Privacy Policy"), ("cookie-privacy-policy", "Cookie Policy")]


def legal(slug, title, desc, h1, body_html):
    p = "../"
    out = head(title, desc, p) + header(p, slug)
    out = out.replace('<header class="site-header">', '<header class="site-header solid">')
    aside = "".join(f'<a href="{p}{s}/"{" aria-current=page" if s == slug else ""}>{n}</a>' for s, n in LEGAL_NAV)
    out += f"""
<section class="section" style="padding-top:calc(var(--section) + 84px)">
  <div class="wrap">
    <div class="head stack"><div><h1 style="font-size:clamp(2.4rem,5vw,4rem);margin-top:18px">{escape(h1)}</h1></div></div>
    <div class="legal-layout">
      <aside aria-label="Legal pages">{aside}</aside>
      <div class="prose">{body_html}</div>
    </div>
  </div>
</section>
"""
    out += footer(p)
    write(f"{slug}/index.html", out)


TERMS = """
<p>These Terms govern your access to, usage of all content, Product and Services available at https://skyi.co.uk website (the “Service”) operated by SKYi (“us”, “we”, or “our”).</p>
<p>Your access to our services are subject to your acceptance, without modification, of all of the terms and conditions contained herein and all other operating rules and policies published and that may be published from time to time by us.</p>
<p>Please read the Agreement carefully before accessing or using our Services. By accessing or using any part of our Services, you agree to be bound by these Terms. If you do not agree to any part of the terms of the Agreement, then you may not access or use our Services.</p>
<h2>Intellectual Property</h2>
<p>The Agreement does not transfer from Us to you any of Ours or third party intellectual property, and all right, title, and interest in and to such property will remain (as between the parties) solely with SKYi and its licensors.</p>
<h2>Third Party Services</h2>
<p>In using the Services, you may use third-party services, products, software, embeds, or applications developed by a third party (“Third Party Services”).</p>
<p>If you use any Third Party Services, you understand that:</p>
<ul>
<li>Any use of a Third Party Service is at your own risk, and we shall not be responsible or liable to anyone for Third Party websites or Services.</li>
<li>You acknowledge and agree that We shall not be responsible or liable for any damage or loss caused or alleged to be caused by or in connection with the use of any such content, goods or services available on or through any such web sites or services.</li>
</ul>
<h2>Accounts</h2>
<p>Where use of any part of our Services requires an account, you agree to provide us with complete and accurate information when you register for an account.</p>
<p>You will be solely responsible and liable for any activity that occurs under your account. You are responsible for keeping your account information up-to-date and for keeping your password secure.</p>
<p>You are responsible for maintaining the security of your account that you use to access the Service. You shall not share or misuse your access credentials. You must notify us immediately of any unauthorized uses of your account or upon becoming aware of any other breach of security.</p>
<h2>Termination</h2>
<p>We may terminate or suspend your access to all or any part of our Services at any time, with or without cause, with or without notice, effective immediately.</p>
<p>If you wish to terminate the Agreement or your SKYi account, you may simply discontinue using our Services.</p>
<p>All provisions of the Agreement which by their nature should survive termination shall survive termination, including, without limitation, ownership provisions, warranty disclaimers, indemnity, and limitations of liability.</p>
<h2>Disclaimer</h2>
<p>Our Services are provided “AS IS.” and “AS AVAILABLE” basis. SKYi and its suppliers and licensors hereby disclaim all warranties of any kind, express or implied, including, without limitation, the warranties of merchantability, fitness for a particular purpose and non-infringement. Neither SKYi, nor its suppliers and licensors, makes any warranty that our Services will be error free or that access thereto will be continuous or uninterrupted. You understand that you download from, or otherwise obtain content or services through, our Services at your own discretion and risk.</p>
<h2>Jurisdiction and Applicable Law</h2>
<p>Except to the extent any applicable law provides otherwise, the Agreement and any access to or use of our Services will be governed by the laws of United Kingdom.</p>
<p>The proper venue for any disputes arising out of or relating to the Agreement and any access to or use of our Services will be the state and federal courts located in United Kingdom.</p>
<h2>Changes</h2>
<p>SKYi reserves the right, at our sole discretion, to modify or replace these Terms at any time.</p>
<p>If we make changes that are material, we will let you know by posting on our website, or by sending you an email or other communication before the changes take effect. The notice will designate a reasonable period of time after which the new terms will take effect.</p>
<p>If you disagree with our changes, then you should stop using our Services within the designated notice period, or once the changes become effective.</p>
<p>Your continued use of our Services will be subject to the new terms.</p>
"""

PRIVACY = """
<p>Welcome to https://skyi.co.uk (the “Site”). We understand that privacy online is important to users of our Site, especially when conducting business. This statement governs our privacy policies with respect to those users of the Site (“Visitors”) who visit without transacting business and Visitors who register to transact business on the Site and make use of the various services offered by SKYi (collectively, “Services”) (“Authorized Customers”).</p>
<h2>“Personally Identifiable Information”</h2>
<p>refers to any information that identifies or can be used to identify, contact, or locate the person to whom such information pertains, including, but not limited to, name, address, phone number, fax number, email address, financial profiles, social security number, and credit card information. Personally Identifiable Information does not include information that is collected anonymously (that is, without identification of the individual user) or demographic information not connected to an identified individual.</p>
<h2>What Personally Identifiable Information is collected?</h2>
<p>We may collect basic user profile information from all of our Visitors. We collect the following additional information from our Authorized Customers: the names, addresses, phone numbers and email addresses of Authorized Customers, the nature and size of the business, and the nature and size of the advertising inventory that the Authorized Customer intends to purchase or sell.</p>
<h2>What organizations are collecting the information?</h2>
<p>In addition to our direct collection of information, our third party service vendors (such as credit card companies, clearinghouses and banks) who may provide such services as credit, insurance, and escrow services may collect this information from our Visitors and Authorized Customers. We do not control how these third parties use such information, but we do ask them to disclose how they use personal information provided to them from Visitors and Authorized Customers. Some of these third parties may be intermediaries that act solely as links in the distribution chain, and do not store, retain, or use the information given to them.</p>
<h2>How does the Site use Personally Identifiable Information?</h2>
<p>We use Personally Identifiable Information to customize the Site, to make appropriate service offerings, and to fulfill buying and selling requests on the Site. We may email Visitors and Authorized Customers about research or purchase and selling opportunities on the Site or information related to the subject matter of the Site. We may also use Personally Identifiable Information to contact Visitors and Authorized Customers in response to specific inquiries, or to provide requested information.</p>
<h2>With whom may the information be shared?</h2>
<p>Personally Identifiable Information about Authorized Customers may be shared with other Authorized Customers who wish to evaluate potential transactions with other Authorized Customers. We may share aggregated information about our Visitors, including the demographics of our Visitors and Authorized Customers, with our affiliated agencies and third party vendors. We also offer the opportunity to “opt out” of receiving information or being contacted by us or by any agency acting on our behalf.</p>
<h2>How is Personally Identifiable Information stored?</h2>
<p>Personally Identifiable Information collected by SKYi is securely stored and is not accessible to third parties or employees of SKYi except for use as indicated above.</p>
<h2>What choices are available to Visitors regarding collection, use and distribution of the information?</h2>
<p>Visitors and Authorized Customers may opt out of receiving unsolicited information from or being contacted by us and/or our vendors and affiliated agencies by responding to emails as instructed, or by contacting us at 51 Leslie Road, St Helens, Merseyside, WA10 3AQ.</p>
<h2>Are Cookies Used on the Site?</h2>
<p>Cookies are used for a variety of reasons. We use Cookies to obtain information about the preferences of our Visitors and the services they select. We also use Cookies for security purposes to protect our Authorized Customers. For example, if an Authorized Customer is logged on and the site is unused for more than 10 minutes, we will automatically log the Authorized Customer off.</p>
<h2>How does SKYi use login information?</h2>
<p>SKYi uses login information, including, but not limited to, IP addresses, ISPs, and browser types, to analyze trends, administer the Site, track a user’s movement and use, and gather broad demographic information.</p>
<h2>What partners or service providers have access to Personally Identifiable Information from Visitors and/or Authorized Customers on the Site?</h2>
<p>SKYi has entered into and will continue to enter into partnerships and other affiliations with a number of vendors. Such vendors may have access to certain Personally Identifiable Information on a need to know basis for evaluating Authorized Customers for service eligibility. Our privacy policy does not cover their collection or use of this information. Disclosure of Personally Identifiable Information to comply with law. We will disclose Personally Identifiable Information in order to comply with a court order or subpoena or a request from a law enforcement agency to release information. We will also disclose Personally Identifiable Information when reasonably necessary to protect the safety of our Visitors and Authorized Customers.</p>
<h2>How does the Site keep Personally Identifiable Information secure?</h2>
<p>All of our employees are familiar with our security policy and practices. The Personally Identifiable Information of our Visitors and Authorized Customers is only accessible to a limited number of qualified employees who are given a password in order to gain access to the information. We audit our security systems and processes on a regular basis. Sensitive information, such as credit card numbers or social security numbers, is protected by encryption protocols, in place to protect information sent over the Internet. While we take commercially reasonable measures to maintain a secure site, electronic communications and databases are subject to errors, tampering and break-ins, and we cannot guarantee or warrant that such events will not take place and we will not be liable to Visitors or Authorized Customers for any such occurrences.</p>
<h2>How can Visitors correct any inaccuracies in Personally Identifiable Information?</h2>
<p>Visitors and Authorized Customers may contact us to update Personally Identifiable Information about them or to correct any inaccuracies by emailing us at <a href="mailto:info@skyi.co.uk">info@skyi.co.uk</a>.</p>
<h2>Can a Visitor delete or deactivate Personally Identifiable Information collected by the Site?</h2>
<p>We provide Visitors and Authorized Customers with a mechanism to delete/deactivate Personally Identifiable Information from the Site’s database by contacting <a href="mailto:info@skyi.co.uk">info@skyi.co.uk</a>. However, because of backups and records of deletions, it may be impossible to delete a Visitor’s entry without retaining some residual information. An individual who requests to have Personally Identifiable Information deactivated will have this information functionally deleted, and we will not sell, transfer, or use Personally Identifiable Information relating to that individual in any way moving forward.</p>
<h2>What happens if the Privacy Policy Changes?</h2>
<p>We will let our Visitors and Authorized Customers know about changes to our privacy policy by posting such changes on the Site. However, if we are changing our privacy policy in a manner that might cause disclosure of Personally Identifiable Information that a Visitor or Authorized Customer has previously requested not be disclosed, we will contact such Visitor or Authorized Customer to allow such Visitor or Authorized Customer to prevent such disclosure.</p>
<h2>Links</h2>
<p>https://skyi.co.uk contains links to other web sites. Please note that when you click on one of these links, you are moving to another web site. We encourage you to read the privacy statements of these linked sites as their privacy policies may differ from ours.</p>
"""

COOKIES = """
<p>https://skyi.co.uk is committed to protecting your privacy online.</p>
<h2>What information do we collect?</h2>
<p>We collect information from you when you visit our site. When submitting or registering on our site, you may be asked to enter your name or e-mail address. You may, however, visit our site anonymously.</p>
<h2>What do we use your information for?</h2>
<p>Any of the information we collect from you may be used in one of the following ways:</p>
<ul><li>To improve our website</li><li>To improve customer service</li></ul>
<h2>How do we protect your information?</h2>
<p>We implement a variety of security measures to maintain the safety of your personal information when you place an order or enter, submit, or access your personal information.</p>
<h2>Cookies</h2>
<p>Cookies are small files that a site or its service provider transfers to your computer’s hard drive through your Web browser (if you allow) that enables the site’s or service provider’s systems to recognise your browser and capture and remember certain information. We use cookies to understand and save your preferences for future visits.</p>
<h2>Online Privacy Policy Only</h2>
<p>This online privacy policy applies only to information collected through our website and not to information collected offline.</p>
<h2>Changes to our Privacy Policy</h2>
<p>If we decide to change our privacy policy, we will post those changes on this page. If you have any questions and suggestions regarding our Privacy Policy Statement, please contact us and we will get back to you very soon.</p>
<h2>Contact Information</h2>
<p>SKYi<br>Mailing address: 51 Leslie Road, St Helens, Merseyside, WA10 3AQ, United Kingdom<br>Phone: 07385 204229<br>Contact Email: <a href="mailto:info@skyi.co.uk">info@skyi.co.uk</a></p>
"""


if __name__ == "__main__":
    home()
    for d in (ROOF, PROPERTY, CONSTRUCTION, EVENTS, MARKETING, WEDDINGS):
        service_page(d)
    about()
    contact()
    legal("terms-of-use", "Access SKYi Services: Comprehend Our Terms & Conditions", "SKYi terms and conditions.", "Terms and Conditions", TERMS)
    legal("privacy-policy", "Secure and Trustworthy Privacy Policy at SKYi", "SKYi privacy policy.", "Privacy Policy", PRIVACY)
    legal("cookie-privacy-policy", "Secure Online Experience with SKYi: Protecting Your Privacy", "SKYi cookie policy.", "Cookie Policy", COOKIES)
