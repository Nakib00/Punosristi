import os
import glob
from bs4 import BeautifulSoup

def process_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # 1. Update HTML tag
    html_tag = soup.find('html')
    if html_tag:
        html_tag['lang'] = 'en-BD'

    # 2. Extract title and description logic based on filename
    filename = os.path.basename(filepath)
    title = ""
    description = ""
    schema = ""
    h1_text = ""
    
    if filename == "index.html":
        title = "Punoshristi | Smart Plastic Recycling Rewards in Bangladesh"
        description = "Punoshristi offers IoT-enabled Smart Reverse Vending Machines for plastic bottle recycling in Dhaka, Bangladesh. Drop bottles, earn instant digital reward points."
        h1_text = "Punoshristi: Smart Plastic Recycling in Bangladesh."
        schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Punoshristi",
  "alternateName": "পুনঃসৃষ্টি",
  "url": "https://punoshristi.com/",
  "logo": "https://punoshristi.com/assets/images/image_2.1.png",
  "description": "IoT-enabled Smart Reverse Vending Machines for plastic bottle recycling in Dhaka, Bangladesh.",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+880-1234-567890",
    "contactType": "customer service",
    "areaServed": "BD",
    "availableLanguage": ["en", "bn"]
  }
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Punoshristi Smart Reverse Vending Machine",
  "description": "Smart waste management RVM for plastic recycling in Bangladesh. Earn recycling reward points instantly.",
  "brand": {
    "@type": "Brand",
    "name": "Punoshristi"
  }
}
</script>"""
    elif filename == "about.html":
        title = "About Punoshristi | Green Tech Startup in Bangladesh"
        description = "Learn about Punoshristi's mission to solve the plastic recycling crisis in Dhaka, Bangladesh with smart technology, community action, and an eco-friendly vision."
        h1_text = "Punoshristi's Mission: Smart Plastic Recycling for a Greener Bangladesh"
    elif filename == "how-it-works.html":
        title = "How Punoshristi Works | Smart RVM Recycling Bangladesh"
        description = "Discover how Punoshristi's reverse vending machines work in Dhaka. Drop a plastic bottle, let AI sort it, scan your QR code, and earn instant rewards."
        h1_text = "How Punoshristi Works: Recycling Rewards in Bangladesh"
        schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to recycle a plastic bottle with Punoshristi RVM",
  "description": "Learn how to use Punoshristi's smart Reverse Vending Machine to recycle plastic bottles and earn rewards in Dhaka, Bangladesh.",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Find Machine",
      "text": "Locate the nearest Punoshristi Smart RVM using our mobile app."
    },
    {
      "@type": "HowToStep",
      "name": "Drop Bottle",
      "text": "Insert your empty PET bottle into the RVM."
    },
    {
      "@type": "HowToStep",
      "name": "Scan QR & Earn",
      "text": "Scan the QR code displayed on the screen with the Punoshristi app to instantly credit points to your digital wallet."
    }
  ]
}
</script>"""
    elif filename == "impact.html":
        title = "Our Impact | Eco-Tech & Plastic Recycling in Bangladesh"
        description = "See the real-time environmental impact of Punoshristi's smart waste management network across Bangladesh. Tracking plastic recycled and CO2 emissions saved."
        h1_text = "Punoshristi's Impact: Reversing Plastic Pollution in Bangladesh"
        schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How do I report an issue with a machine?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Please use the contact form and select 'General Inquiry', detailing the machine location."
    }
  }, {
    "@type": "Question",
    "name": "Are you expanding outside Dhaka?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "We are planning to open our Chittagong Hub soon. Stay tuned to our social channels!"
    }
  }]
}
</script>"""
    elif filename == "contact.html":
        title = "Contact Punoshristi | Smart Waste Management Dhaka"
        description = "Get in touch with Punoshristi to host a smart reverse vending machine, partner with us, or learn more about plastic recycling initiatives in Bangladesh."
        h1_text = "Contact Punoshristi: Let's Re-Create Bangladesh Together"
        schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Punoshristi",
  "image": "https://punoshristi.com/assets/images/image_2.1.png",
  "url": "https://punoshristi.com/",
  "telephone": "+8801234567890",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Bashundhara R/A",
    "addressLocality": "Dhaka",
    "addressRegion": "Dhaka",
    "postalCode": "1229",
    "addressCountry": "BD"
  }
}
</script>"""

    # 3. Replace entire Head
    head_tag = soup.find('head')
    if head_tag:
        # Save old styles and specific fonts if we want, but we have a fixed set.
        new_head = BeautifulSoup(f"""
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title}</title>
<meta name="description" content="{description}"/>
<meta name="robots" content="index, follow"/>
<meta name="author" content="Punoshristi"/>
<meta name="keywords" content="Punoshristi, পুনঃসৃষ্টি, plastic recycling Bangladesh, reverse vending machine Dhaka, RVM Bangladesh, eco tech Bangladesh, recycling reward app Dhaka, smart waste management Bangladesh, green technology Bangladesh"/>
<meta name="language" content="English"/>
<meta name="geo.region" content="BD-13"/>
<meta name="geo.placename" content="Dhaka"/>
<meta name="revisit-after" content="7 days"/>
<meta name="theme-color" content="#1A5C2A"/>

<meta property="og:type" content="website"/>
<meta property="og:url" content="https://punoshristi.com/{filename if filename != 'index.html' else ''}"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{description}"/>
<meta property="og:image" content="https://punoshristi.com/assets/images/image_2.1.png"/>
<meta property="og:site_name" content="Punoshristi"/>
<meta property="og:locale" content="en_US"/>
<meta property="og:locale:alternate" content="bn_BD"/>

<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{title}"/>
<meta name="twitter:description" content="{description}"/>
<meta name="twitter:image" content="https://punoshristi.com/assets/images/image_2.1.png"/>

<link rel="canonical" href="https://punoshristi.com/{filename if filename != 'index.html' else ''}"/>
<link rel="alternate" hreflang="en-BD" href="https://punoshristi.com/{filename if filename != 'index.html' else ''}"/>
<link rel="alternate" hreflang="bn-BD" href="https://punoshristi.com/bn/{filename if filename != 'index.html' else ''}"/>

<link rel="icon" href="assets/images/favicon.ico" type="image/x-icon"/>

<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Outfit:wght@400;600;700;800&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>

<link rel="stylesheet" href="assets/css/style.css"/>

{schema}

<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
</head>
        """, 'html.parser').head
        head_tag.replace_with(new_head)

    # 4. Move scripts to bottom with defer
    body_tag = soup.find('body')
    if body_tag:
        # Remove tailwindcss and config from where they were if they exist in head
        # Oh wait, we already replaced the whole head.
        # Add them to the end of body
        scripts_to_add = [
            '<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries" defer></script>',
            '<script src="assets/js/tailwind-config.js" defer></script>'
        ]
        
        # also find existing mobile-menu script and add defer
        existing_scripts = body_tag.find_all('script')
        for script in existing_scripts:
            script['defer'] = ''

        for script_str in scripts_to_add:
            script_tag = BeautifulSoup(script_str, 'html.parser').script
            body_tag.append(script_tag)

    # 5. Fix H1s
    h1s = soup.find_all('h1')
    for i, h1 in enumerate(h1s):
        if i == 0:
            # First H1 is kept, but its text is modified to contain the primary keyword
            # But wait, it might ruin the design if we completely overwrite text. 
            # We'll just append it or set it, we will just use the text we defined but keep its classes.
            h1.string = h1_text
        else:
            # Change subsequent H1s to H2s
            h1.name = 'h2'

    # 6. Optimize images
    images = soup.find_all('img')
    for i, img in enumerate(images):
        # Determine eager/lazy
        if i == 0:
            img['loading'] = 'eager'
        else:
            img['loading'] = 'lazy'
            
        # Ensure dimensions
        if not img.has_attr('width'):
            img['width'] = '800'
        if not img.has_attr('height'):
            img['height'] = '600'
            
        # Alt text
        old_alt = img.get('alt', img.get('data-alt', ''))
        img['alt'] = f"{old_alt} - Punoshristi Bangladesh Plastic Recycling" if old_alt else "Punoshristi Bangladesh Plastic Recycling"

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Finished {filepath}")

# Process all 5 files
files = ["index.html", "about.html", "how-it-works.html", "impact.html", "contact.html"]
for f in files:
    full_path = os.path.join(r"d:\ZAN IT\ZAN Tech\Punoshristi\stitch_punoshristi_smart_recycling_rewards\stitch_punoshristi_smart_recycling_rewards", f)
    process_file(full_path)

print("SEO Optimization completed.")
