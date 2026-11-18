---
layout: home
permalink: /hr/edukacija/claude-developer/
lang: hr
ref: training-claude-developer
sticky_cta:
  label: Dogovorite poziv
  url: https://calendly.com/prlic/15min
image:
  path: /assets/img/og-image.png
  width: 1200
  height: 630
locale: hr_HR
title: Tečaj za ispit Claude Certified Developer (CCDV-F)
description: >-
  Dvodnevni praktični tečaj za programere: Claude API, upute, alati i MCP, agenti, Claude Code, sigurnost i evaluacija. Priprema za ispit CCDV-F.

header:
  compact: true
  title: Razvoj s Claudeom
  subtitle: Priprema za ispit Claude Certified Developer – Foundations (CCDV-F)
  text: >-
    Dva dana programiranja, a ne gledanja: od odabira modela i procjene troška
    do API klijenta, alata i MCP servera, nadzornog agenta sa zaštitnim mjerama,
    Claude Code repozitorija postavljenog za tim i evaluacije kao uvjeta za
    izdavanje. Svaki modul završava vježbom na istom primjeru, a tečaj pokriva
    svih osam domena ispita CCDV-F.
  action:
    label: Pogledajte program
    url: '#modules'
  proof:
    - 2 dana
    - Programeri, praktično programiranje
    - Online ili kod vas
    - Na hrvatskom ili engleskom, do 20 polaznika

sections:
  - type: course-overview.html
    section_id: overview
    background_style: bg-subtle
    title: Za koga je tečaj i što ćete nakon njega znati
    text: >-
      Jedan od četiri [tečaja za Claude](/hr/edukacija/), za programere koji će
      na Claudeu graditi funkcionalnosti proizvoda i interne alate.
    columns:
      - title: Za koga je
        items:
          - Backend, full-stack i platformski inženjeri koji u proizvod dodaju Claude funkcionalnosti
          - Programeri koji grade interne agente, automatizacije i integracije
          - Timovi koji uvode Claude Code i žele zajedničke, kontrolirane postavke
          - Svi koji se pripremaju za ispit Claude Certified Developer – Foundations
      - title: Što ćete moći
        items:
          - Odabrati Claude model za zadano opterećenje i procijeniti trošak rada
          - Izgraditi pouzdane API klijente sa streamingom, prompt cachingom, batch obradom i obradom pogrešaka
          - Oblikovati upute i kontekst koji daju provjeren, strukturiran izlaz
          - Implementirati alate s odobravanjem rizičnih radnji i izložiti vlastiti sustav kao MCP server
          - Odlučiti između tijeka rada i agenta te izgraditi agenta sa zaštitnim mjerama
          - Zaštititi Claude aplikaciju od prompt injectiona i curenja podataka i uvjetovati izdanja evaluacijom

  - type: course-modules.html
    section_id: modules
    title: Program tečaja
    text: >-
      Prvi dan pokriva osnovne gradivne elemente, drugi produkcijske sustave.
      Svaki modul počinje zahtjevom iz izmišljene SaaS tvrtke za fakturiranje,
      uključuje demonstracije i provjeru znanja, a završava vježbom
      programiranja.
    modules:
      - title: Osnove LLM-ova i odabir modela
        text: >-
          Kako modeli generiraju tekst, tokeni i uzorkovanje, usporedba Claude
          modela po kvaliteti, latenciji i cijeni te jednostavan model troškova.
        lab: Odaberite model i izračunajte trošak
      - title: Rad s Claude API-jem
        text: >-
          Messages API i dobra inženjerska praksa oko njega: streaming, vid,
          prošireno razmišljanje, prompt caching, batch obrada i Claude na cloud
          platformama poput Amazon Bedrocka.
        lab: Klijent za unos računa
      - title: Oblikovanje uputa i konteksta
        text: >-
          Dorada upute prema testnim slučajevima, odluka što ulazi u kontekst, a
          što ostaje izvan njega, i provjera izlaza prije upotrebe.
        lab: Upute, kontekst i izlaz kojem se može vjerovati
      - title: Alati i MCP
        text: >-
          Definicije alata i rezultati s pogreškom, klijentski i serverski alati,
          odobravanje rizičnih radnji te kada izgraditi MCP server.
        lab: Alati, odobravanje i MCP server
      - title: Agenti i tijekovi rada
        text: >-
          Kada fiksni tijek rada nadmašuje agenta, izgradnja agenata s Agent
          SDK-om, nadzorni agenti i subagenti, hookovi, memorija i česti obrasci.
        lab: Nadzorni agent sa zaštitnim mjerama
      - title: Dizajn aplikacija, konfiguracija i Claude Code
        text: >-
          Zahtjevi i životni ciklus aplikacije, konfiguracija i verzioniranje
          uputa te Claude Code za tim, bez sučelja i u CI-ju.
        lab: Postavite Claude Code i verzionirajte upute
      - title: Sigurnost i zaštita
        text: >-
          Prompt injection i nepouzdani ulazi, osobni podaci i kontrola pristupa,
          slojevite zaštitne mjere, najmanje potrebne ovlasti te upravljanje
          tajnama i ključevima.
        lab: Slojevite zaštitne mjere i zaštita tajni
      - title: Evaluacija, otklanjanje pogrešaka i troškovi
        text: >-
          Čitanje tragova izvođenja i oporavak od pogrešaka, oblikovanje i
          provođenje evaluacija te upravljanje tokenima i troškovima u produkciji.
        lab: Evaluacija kao uvjet za izdanje i izvještaj o troškovima
      - title: Sažetak i priprema za ispit
        text: >-
          Pregled svih osam domena, scenariji u stilu ispita, što očekivati na
          dan ispita i sljedeći koraci.

  - type: course-overview.html
    section_id: exam
    background_style: bg-subtle
    title: Usklađenost s ispitom
    text: >-
      Svaka domena iz vodiča za ispit Claude Certified Developer – Foundations
      obrađena je u barem jednom modulu, razmjerno svom udjelu u ispitu.
      Isprobajte [20 besplatnih probnih pitanja](/training/claude-mock-exams/#ccdv-f)
      za ovaj ispit, s objašnjenjem svakog odgovora (na engleskom).
    facts:
      - label: Oznaka ispita
        value: CCDV-F
      - label: Pitanja
        value: "53"
      - label: Trajanje
        value: 120 minuta
      - label: Prolazni rezultat
        value: 720 / 1.000
      - label: Cijena ispita
        value: 125 USD
    columns:
      - title: Preduvjeti
        items:
          - Sigurno programiranje; vježbe koriste Python SDK, a programeri koji rade u TypeScriptu lako ih prate
          - Poznavanje REST API-ja, JSON-a, Gita i naredbenog retka
          - Laptop s instaliranim Pythonom 3.11+, VS Codeom, Gitom i Claude Codeom
          - Claude API ključ ili pristup Amazon Bedrocku, najbolje vaš; pomažem s postavljanjem
      - title: Polaganje ispita
        items:
          - Polaže se kod Pearson VUE-a, online uz nadzor ili u ispitnom centru
          - Prijava ide preko Anthropic Partner Academyja, za što tvrtka kandidata mora biti članica Claude Partner Networka
          - Pitanja s jednim ili više točnih odgovora, skalirani rezultat od 100 do 1.000
          - Certifikat vrijedi 12 mjeseci
    note: >-
      Anthropic mijenja sadržaj ispita CCDV-F 7. prosinca 2026. Prije svakog
      tečaja nakon tog datuma program se usklađuje s novim vodičem za ispit.

  - type: faq.html
    section_id: faq
    title: Dobro je znati
    items:
      - q: Tko predaje?
        a: >-
          Ja. AWS Authorized Instructor i Claude Certified Architect –
          Professional, s više od 20 godina iskustva u razvoju softvera.
          Svakodnevno gradim produkcijske Claude sustave, primjerice privatnu
          Claude platformu s punim audit tragom na Amazon Bedrocku za reguliranu
          organizaciju i interni marketplace Claude Code pluginova, i odatle
          dolaze vježbe na tečaju. Više na [naslovnoj stranici](/hr/).

      - q: Online ili uživo, i na kojem jeziku?
        a: >-
          Online uživo, u blokovima od pola dana, ili kod vas, bilo gdje u
          Hrvatskoj i Europi; putni troškovi naplaćuju se po stvarnom trošku.
          Tečaj se održava na hrvatskom ili engleskom, za do 20 polaznika po
          grupi.

      - q: Može li se tečaj prilagoditi našem timu?
        a: >-
          Može. Gornji program je jezgra usklađena s ispitom; primjere i vježbe
          prilagođavam vašoj tehnologiji i slučajevima primjene. Prije tečaja
          dobivate detaljan program na odobrenje.

      - q: Koliko košta?
        a: >-
          Edukacija tima počinje od 4.000 € za tečaj od jednog do dva dana, bez
          PDV-a i putnih troškova; cijena ovisi o formatu i veličini grupe.
          Korištenje modela tijekom vježbi naplaćuje se na vaš Claude API ili AWS
          račun i obično je malo; procjenu dobivate unaprijed.

      - q: Je li ovo službeni Anthropicov tečaj?
        a: >-
          Nije. Neovisni sam predavač s Anthropicovim Claude certifikatima i
          gradim produkcijske sustave s Claudeom. Tečaj priprema za ispit Claude
          Certified Developer – Foundations, ali nije službeni Anthropicov tečaj.
          Ispit se polaže kod Pearson VUE-a; prijava ide preko Anthropic Partner
          Academyja, za što tvrtka polaznika mora biti članica Claude Partner
          Networka.

  - type: contact.html
    section_id: contacts
    title: Dogovorimo tečaj
    watermark: CCDV-F
    text: >-
      Recite mi nešto o timu i o tome što gradi. Kratak poziv obično je dovoljan
      da dogovorimo format, vježbe i termine.
    actions:
      - title: Dogovorite poziv
        icon: fa-calendar-alt
        url: https://calendly.com/prlic/15min
      - title: ivan@prlic.io
        icon: fa-envelope
        url: mailto:ivan@prlic.io?subject=Te%C4%8Daj%3A%20Razvoj%20s%20Claudeom%20(CCDV-F)
      - title: LinkedIn
        icon: fa-linkedin
        icon_type: fab
        url: https://www.linkedin.com/in/iprlic/
---
