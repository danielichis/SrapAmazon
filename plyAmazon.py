from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    tr1=[]
    tr2=[]
    page.goto("https://www.amazon.com/port%C3%A1til-pantalla-pulgadas-almacenamiento-Graphics/dp/B09BG85LRV/ref=sr_1_2_sspa?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1RH58286CLJMH&keywords=laptop%2Bgamer&qid=1657223494&sprefix=laptop%2Bgame%2Caps%2C154&sr=8-2-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFLMDhNVzE1QjExMlcmZW5jcnlwdGVkSWQ9QTA3MTE4MTM2M0RXQldXNU5KUjYmZW5jcnlwdGVkQWRJZD1BMDEyNjE5MDFLUFRZSEJENklESkMmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1")
    #page.pause()
    product_name=page.query_selector("span#productTitle").inner_text()
    tr11=[e.inner_text() for e in page.query_selector_all("table.a-normal.a-spacing-micro tbody tr td:nth-child(1) span")]
    tr12=[e.inner_text() for e in page.query_selector_all("table.a-normal.a-spacing-micro tbody tr td:nth-child(2) span")]

    tr22=[e.inner_text().replace('\u200e','') for e in page.query_selector_all('table#productDetails_techSpec_section_1 tbody tr td')]
    tr21=[e.inner_text() for e in page.query_selector_all('table#productDetails_techSpec_section_1 tbody tr th')]

    tr32=[e.inner_text().replace('\u200e','') for e in page.query_selector_all('table#productDetails_techSpec_section_2 tbody tr td')]
    tr31=[e.inner_text() for e in page.query_selector_all('table#productDetails_techSpec_section_2 tbody tr th')]

    about=[e.inner_text() for e in page.query_selector_all("div#feature-bullets li:not([id]) span.a-list-item")]
    product_info=page.query_selector("#productDescription.a-section.a-spacing-small p span").inner_text()
    tr11.extend(tr21)
    tr11.extend(tr31)

    tr12.extend(tr22)
    tr12.extend(tr32)
    length=len(tr11)
    print(length)
    detailsList=[]
    for j,u in enumerate(tr11):
        details={
            tr11[j]:tr12[j]
        }
        detailsList.append(details)
    seen = set()
    new_l = []
    j=0
    for d in detailsList:
        t = tuple(d.items())
        if t not in seen:
            if j<1:
                ss="-"+list(d.keys())[0]+": "+list(d.values())[0]+"\n"
                #print(d.keys(),d.values())
            else:
                #print(d.keys(),d.values())
                ss=ss+"-"+list(d.keys())[0]+": "+list(d.values())[0]+"\n"
            j=j+1
            seen.add(t)
            new_l.append(d)
    
    guiones="-------------------------------------------------------------------"
    tittle_part=f'Titulo\n{guiones} {product_name}'
    state_part=f"Estado{guiones}\nNuevo en caja importado por UNALUKA"
    sss=f"{tittle_part}\n{state_part}\n Descripción:\n {guiones}\n {ss}"
    with open("laptop.txt", "w") as f:
        f.write(sss)
    print(sss)
    print(len(new_l))
    browser.close()
    