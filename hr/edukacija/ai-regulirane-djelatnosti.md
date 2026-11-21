---
layout: home
permalink: /hr/edukacija/ai-regulirane-djelatnosti/
lang: hr
ref: training-ai-regulated-public-sector
sticky_cta:
  label: Iskažite interes
  url: mailto:ivan@prlic.io?subject=Te%C4%8Daj%3A%20AI%20u%20reguliranim%20djelatnostima%20i%20javnom%20sektoru
image:
  path: /assets/img/og-image.png
  width: 1200
  height: 630
locale: hr_HR
title: Uvođenje AI-ja u regulirane djelatnosti i javni sektor
description: >-
  Dvodnevni tečaj o sigurnom uvođenju AI-ja u regulirane djelatnosti i javni sektor: sigurnost, EU Akt o UI, GDPR, NIS2 i tajni podaci, uz plan uvođenja.

last_updated: 2026-11-21
# Course JSON-LD (_includes/course-schema.html); price_from only where the price is published.
course:
  order: 6
  level: Srednja razina
  workload: P2D
  instances:
    - mode: Online
      workload: P2D
    - mode: Onsite
      workload: P2D

header:
  compact: true
  title: AI u reguliranim djelatnostima i javnom sektoru
  subtitle: Uvedite AI, a da ne izgubite kontrolu nad podacima
  text: >-
    Tečaj za organizacije u kojima curenje podataka ili pogrešna odluka ima
    pravne posljedice: državna i javna uprava, zdravstvo, energetika, promet,
    banke i osiguranja te njihovi dobavljači. Pokriva što od vas traže EU Akt
    o umjetnoj inteligenciji, GDPR i Zakon o kibernetičkoj sigurnosti, kako
    osobne, povjerljive i klasificirane podatke držati podalje od krivih
    sustava, kako zaštititi AI asistente i agente te kako nabaviti AI alate i
    upravljati njima. Vaš tim odlazi s razvrstanim popisom slučajeva primjene,
    referentnom arhitekturom i planom uvođenja za jedan od njih.
  action:
    label: Pogledajte program
    url: '#modules'
  proof:
    - 2 dana, za vašu organizaciju
    - Sigurnost, usklađenost i IT
    - Online ili kod vas
    - Hrvatski ili engleski

sections:
  - type: course-overview.html
    section_id: overview
    background_style: bg-subtle
    title: Kome je namijenjen i što ćete znati
    text: >-
      Jedan od [praktičnih AI tečajeva](/hr/edukacija/#practical-ai), nije
      vezan uz certifikacijski ispit. U istu prostoriju dovodi one koji moraju
      odobriti AI (sigurnost, zaštita podataka, pravni poslovi, IT) i one koji
      ga žele koristiti, i daje im zajednički način odlučivanja.
    columns:
      - title: Kome je namijenjen
        items:
          - Voditeljima informacijske sigurnosti, sigurnosnim savjetnicima i IT arhitektima koji odobravaju ili grade AI rješenja
          - Službenicima za zaštitu podataka, timovima za usklađenost i pravnim službama koje pitaju "smijemo li ovo koristiti?"
          - Rukovoditeljima u državnoj i javnoj upravi, zdravstvu, energetici i financijama koji vode AI projekte
          - Službama nabave koje kupuju AI alate ili pišu tehničke specifikacije za natječaje
          - Dobavljačima i integratorima koji grade AI sustave za regulirane klijente
      - title: Što ćete znati
        items:
          - Objasniti koje obveze iz EU Akta o umjetnoj inteligenciji imate kao dobavljač ili kao subjekt koji uvodi AI, i u koju kategoriju rizika spada svaki slučaj primjene
          - Odlučiti kada slučaj primjene traži procjenu učinka na zaštitu podataka (DPIA) ili procjenu učinka na temeljna prava, i što u nju ide
          - Razvrstati podatke i odlučiti koju AI uslugu, model hostinga i regiju smije koristiti svaka vrsta podataka, od javnih servisa do privatnih ili lokalnih modela
          - Prepoznati sigurnosne rizike svojstvene jezičnim modelima i agentima, poput umetanja uputa (prompt injection) i curenja podataka kroz alate, i kontrole koje ih rješavaju
          - Procijeniti dobavljača AI-ja, ugovorne uvjete, obradu i lokaciju podataka, rok čuvanja, treniranje modela na vašim podacima i izlaznu strategiju
          - Postaviti upravljanje koje prolazi reviziju, AI politiku, popis AI sustava, ljudski nadzor, zapisivanje, praćenje i postupanje s incidentima

  - type: course-modules.html
    section_id: modules
    title: Program tečaja
    text: >-
      Osam modula kroz dva dana. Svaki završava vježbom na vašim slučajevima
      primjene, pa na kraju imate razvrstan popis slučajeva primjene,
      referentnu arhitekturu i plan uvođenja. Bez programiranja.
    modules:
      - title: Regulatorni okvir
        text: >-
          EU Akt o umjetnoj inteligenciji (zabranjene prakse, visokorizični
          sustavi, modeli opće namjene, transparentnost, AI pismenost i rokovi
          nakon izmjena), GDPR i Zakon o provedbi Opće uredbe o zaštiti
          podataka, Zakon o kibernetičkoj sigurnosti (NIS2) te sektorska pravila
          poput DORA-e za financijski sektor, i gdje se preklapaju. Tko je
          dobavljač, a tko subjekt koji uvodi AI.
        lab: Mapa propisa koji se odnose na vašu organizaciju
      - title: Razvrstavanje slučajeva primjene
        text: >-
          Razvrstavanje slučajeva primjene prema kategoriji rizika iz Akta i
          prema podacima koje dotiču. Kada je potrebna procjena učinka na
          zaštitu podataka, kada javna tijela trebaju procjenu učinka na temeljna
          prava i s kojim slučajevima primjene početi.
        lab: Razvrstajte svoj popis slučajeva primjene
      - title: Zaštita podataka u praksi
        text: >-
          Pravna osnova, smanjenje količine podataka i ograničenje svrhe kod
          AI-ja, izvršitelji i podizvršitelji obrade, prijenos podataka izvan
          EU-a, rok čuvanja i ponude "bez zadržavanja podataka", trenira li
          dobavljač model na vašim podacima te mogućnosti čuvanja podataka u EU
          na velikim oblacima.
        lab: Kontrolna lista zaštite podataka za jedan slučaj primjene
      - title: Povjerljivi i klasificirani podaci
        text: >-
          Što nikada ne smije doći do javne AI usluge, kako se stupnjevi tajnosti
          po Zakonu o tajnosti podataka (OGRANIČENO, POVJERLJIVO, TAJNO, VRLO
          TAJNO) i klasificirani podaci EU-a prevode u zahtjeve za smještaj
          sustava, akreditirana i izolirana okruženja, suvereni oblak i lokalno
          hostani otvoreni modeli te postupanje s osjetljivim, ali
          neklasificiranim podacima.
        lab: Matrica vrsta podataka i dopuštenih AI usluga
      - title: Sigurnost AI sustava
        text: >-
          Model prijetnji za jezične modele i agente, umetanje uputa, curenje
          podataka kroz alate, nesigurno korištenje izlaza modela, rizici modela
          i lanca opskrbe (OWASP Top 10 za LLM aplikacije). Identitet i najmanje
          potrebne ovlasti za agente, mrežna izolacija, zaštitne ograde,
          zapisivanje i odvajanje onih koji upravljaju sustavom od onih koji ga
          revidiraju.
        lab: Model prijetnji za AI asistenta nad internim dokumentima
      - title: Nabava i provjera dobavljača
        text: >-
          Što pitati dobavljače AI-ja i kako čitati odgovore, ugovori o obradi
          podataka, sigurnosni certifikati, lokacija podataka, promjene modela,
          ovisnost o dobavljaču i izlaz. Kako napisati zahtjeve za AI u javnoj
          nabavi.
        lab: Upitnik za provjeru dobavljača
      - title: Upravljanje i rad u produkciji
        text: >-
          AI politika koju se ljudi zaista drže, popis AI sustava, ljudski
          nadzor, evaluacija i praćenje, postupanje s incidentima i njihovo
          prijavljivanje te AI pismenost zaposlenika kakvu očekuje Akt.
        lab: Nacrt AI politike i popisa AI sustava
      - title: Referentna arhitektura i uvođenje
        text: >-
          Privatni asistent nad internim dokumentima kao primjer, arhitektura,
          kontrole, dokazi za revizore i postupno uvođenje od pilota do
          produkcije s jasnim kriterijima za nastavak ili zaustavljanje.
        lab: Plan uvođenja za vaš prvi slučaj primjene

  - type: course-overview.html
    section_id: formats
    background_style: bg-subtle
    title: Format
    text: >-
      Održava se za jednu organizaciju, pa vježbe koriste vaše stvarne
      slučajeve primjene, politike i sustave. Rasprave ostaju unutar vaše
      organizacije.
    facts:
      - label: Trajanje
        value: 2 dana
      - label: Grupa
        value: do 16 polaznika
      - label: Izvedba
        value: Online ili kod vas
      - label: Programiranje
        value: Nije potrebno
    columns:
      - title: Za vašu organizaciju, dva dana
        items:
          - Dva dana kod vas ili online u četiri poludnevna bloka
          - "Najbolje radi mješovita grupa: sigurnost, zaštita podataka, pravna služba, IT i vlasnici slučajeva primjene"
          - Primjeri i vježbe prilagođeni vašem sektoru i propisima koji se na njega odnose
          - Detaljan program na odobrenje prije tečaja
      - title: Što zadržavate
        items:
          - Slučajeve primjene razvrstane prema riziku i osjetljivosti podataka
          - Matricu vrsta podataka i dopuštenih AI usluga te upitnik za dobavljače
          - Nacrt AI politike i popisa AI sustava
          - Referentnu arhitekturu i plan uvođenja za prvi slučaj primjene
    note: >-
      Novi tečaj. Prve izvedbe dogovaramo s organizacijama koje iskažu interes;
      javite mi sektor, veličinu grupe i okvirne termine. Na tečaju se ne
      koriste klasificirani ni osobni podaci, primjeri su javni ili izmišljeni,
      a vaši materijali ostaju kod vas.

  - type: faq.html
    section_id: faq
    title: Dobro je znati
    items:
      - q: Tko vodi tečaj?
        a: >-
          Ja. Projektiram i gradim AI sustave za regulirane organizacije, poput
          privatne Claude platforme na Amazon Bedrocku s revizijskim tragom,
          koja podatke drži u EU i odvaja one koji sustavom upravljaju od onih
          koji ga revidiraju. Ovlašteni sam AWS instruktor, imam certifikate AWS
          Security Specialty i Claude Certified Architect – Professional te više
          od 20 godina iskustva u razvoju softvera. Više na
          [početnoj stranici](/hr/).

      - q: Je li ovo pravni savjet?
        a: >-
          Nije. Tečaj pokriva tehničku i organizacijsku stranu usklađenosti, što
          propisi traže u praksi i kako izgraditi i voditi sustave koji to
          ispunjavaju. Pravno tumačenje za vaš konkretan slučaj ostaje vašim
          pravnicima i službeniku za zaštitu podataka, koji su dobrodošli na
          tečaju.

      - q: Je li vezan uz jednog dobavljača AI-ja?
        a: >-
          Nije. Pokriva javne AI usluge (ChatGPT, Microsoft 365 Copilot, Claude,
          Gemini), platforme u oblaku (Amazon Bedrock, Azure, Google Cloud) i
          lokalno hostane otvorene modele. Praktični primjeri dolaze iz sustava
          koje sam izgradio na AWS-u, jer tamo mogu pokazati stvarne kontrole, a
          ne samo slajdove.

      - q: Trebate li pristup našim klasificiranim ili povjerljivim materijalima?
        a: >-
          Ne. Tečaj koristi javne i izmišljene primjere. Vježbe se rade na
          opisima vaših slučajeva primjene, a ono što vaš tim napiše ostaje kod
          vas. Ako se o nekom slučaju ne može otvoreno razgovarati, radimo na
          njegovoj očišćenoj verziji.

      - q: Online ili kod nas, i na kojem jeziku?
        a: >-
          Kod vas bilo gdje u Hrvatskoj i Europi, uz putne troškove po stvarnom
          trošku, ili online u poludnevnim blokovima. Tečaj se održava na
          hrvatskom ili engleskom.

      - q: Koliko košta?
        a: >-
          Edukacija za timove počinje od 4.000 € za tečaj od jednog do dva dana,
          bez PDV-a i putnih troškova; konačna cijena ovisi o formatu i veličini
          grupe.

  - type: contact.html
    section_id: contacts
    title: Iskažite interes
    watermark: USKLAĐENOST
    text: >-
      Javite mi sektor, tko bi sudjelovao i okvirno kada. Poslat ću vam
      detaljan program i predložiti termine prve izvedbe.
    actions:
      - title: Dogovorite poziv
        icon: fa-calendar-alt
        url: https://calendly.com/prlic/15min
      - title: ivan@prlic.io
        icon: fa-envelope
        url: mailto:ivan@prlic.io?subject=Te%C4%8Daj%3A%20AI%20u%20reguliranim%20djelatnostima%20i%20javnom%20sektoru
      - title: LinkedIn
        icon: fa-linkedin
        icon_type: fab
        url: https://www.linkedin.com/in/iprlic/
---
