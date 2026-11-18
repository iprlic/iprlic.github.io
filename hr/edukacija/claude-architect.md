---
layout: home
permalink: /hr/edukacija/claude-architect/
lang: hr
ref: training-claude-architect
sticky_cta:
  label: Dogovorite poziv
  url: https://calendly.com/prlic/15min
image:
  path: /assets/img/og-image.png
  width: 1200
  height: 630
locale: hr_HR
title: Tečaj za ispit Claude Certified Architect (CCAR-F)
description: >-
  Dvodnevni tečaj za arhitekte: agentske petlje, sustavi s više agenata, MCP, Claude Code u CI-ju, strukturirani izlaz i pouzdanost. Priprema za CCAR-F.

last_updated: 2026-11-18
# Course JSON-LD (_includes/course-schema.html); price_from only where the price is published.
course:
  order: 3
  level: Srednja razina
  exam: Claude Certified Architect – Foundations (CCAR-F)
  workload: P2D
  price_from: 4000

header:
  compact: true
  title: Arhitektura s Claudeom
  subtitle: Priprema za ispit Claude Certified Architect – Foundations (CCAR-F)
  text: >-
    Dva dana o projektiranju Claude sustava koji izdrže produkciju: agentske
    petlje i Agent SDK, koordinator sa subagentima, MCP alati, Claude Code za tim
    i u CI-ju, provjerena ekstrakcija podataka i agenti koji eskaliraju umjesto
    da nagađaju. Svaki modul završava vježbom, a tečaj pokriva svih pet domena
    ispita CCAR-F kroz scenarije kakvi su i na ispitu.
  action:
    label: Pogledajte program
    url: '#modules'
  proof:
    - 2 dana
    - Arhitekti i iskusni inženjeri
    - Online ili kod vas
    - Na hrvatskom ili engleskom, do 20 polaznika

sections:
  - type: course-overview.html
    section_id: overview
    background_style: bg-subtle
    title: Za koga je tečaj i što ćete nakon njega znati
    text: >-
      Jedan od četiri [tečaja za Claude](/hr/edukacija/), za one koji odlučuju
      kako se Claude uklapa u sustav i koji pregledavaju rezultat.
    columns:
      - title: Za koga je
        items:
          - Arhitekti rješenja koji projektiraju agente, integracije i platforme temeljene na Claudeu
          - Iskusni i vodeći inženjeri odgovorni za dizajn Claude funkcionalnosti
          - Platformski timovi i timovi za produktivnost programera koji uvode Claude Code
          - Svi koji se pripremaju za ispit Claude Certified Architect – Foundations
      - title: Što ćete moći
        items:
          - Izgraditi agentsku petlju i deterministički je kontrolirati hookovima i sesijama
          - Projektirati koordinatora sa subagentima, čistim predajama i razumnom podjelom zadataka
          - Projektirati sučelja alata i MCP servere sa strukturiranim pogreškama i pravim opsegom
          - Postaviti Claude Code za timski repozitorij i pokretati ga u CI pipelineu
          - Dobiti strukturirani izlaz koji prolazi provjeru, uz ponovne pokušaje, batch obradu i višeprolazni pregled
          - Održati dugotrajne agente pouzdanima, uz eskalaciju, ljudski pregled i podrijetlo podataka

  - type: course-modules.html
    section_id: modules
    title: Program tečaja
    text: >-
      Svi moduli koriste istog izmišljenog trgovca, pa se scenariji s ispita
      (agent za podršku, istraživački sustav, generiranje koda, CI, ekstrakcija
      podataka) odvijaju u jednom, dosljednom okruženju. Svaki modul ima
      demonstracije, provjeru znanja i praktičnu vježbu.
    modules:
      - title: Agentske petlje i Agent SDK
        text: >-
          Kako radi agentska petlja, hookovi za determinističku kontrolu te
          nastavljanje i grananje sesija.
        lab: Izgradite i učvrstite agentsku petlju
      - title: Orkestracija više agenata
        text: >-
          Arhitektura koordinatora i subagenata, pokretanje subagenata i
          prosljeđivanje konteksta, strukturirane predaje i podjela zadataka.
        lab: Istraživački koordinator s više agenata
      - title: Dizajn alata i MCP integracija
        text: >-
          Projektiranje sučelja alata, strukturirane pogreške, raspodjela alata
          među agentima, MCP serveri u Claude Codeu i agentima te ugrađeni alati
          za istraživanje koda.
        lab: Projektirajte, učvrstite i povežite MCP alate
      - title: Konfiguracija Claude Codea
        text: >-
          Hijerarhija CLAUDE.md datoteka, naredbe i skillovi, pravila po
          putanjama te kada planirati prije izvršavanja.
        lab: Postavite Claude Code za timski repozitorij
      - title: Claude Code tijekovi rada i CI/CD
        text: >-
          Claude Code u pipelineu, automatizirani pregled koda koji ostaje
          koristan i iterativni rad koji počinje testovima.
        lab: Uvedite Claude Code u CI pipeline
      - title: Oblikovanje uputa i strukturirani izlaz
        text: >-
          Precizni kriteriji i primjeri (few-shot), strukturirani izlaz kroz
          korištenje alata, provjera i ponovni pokušaji, batch obrada i
          višeprolazni pregled.
        lab: Ekstrakcija podataka s provjerom
      - title: Upravljanje kontekstom i pouzdanost
        text: >-
          Očuvanje konteksta u dugotrajnom radu, eskalacija i nejasnoće, širenje
          pogrešaka među agentima te ljudski pregled s podrijetlom podataka.
        lab: Učinite agente pouzdanima
      - title: Vježba scenarija i sažetak
        text: >-
          Vježba u stilu ispita kroz svih šest ispitnih scenarija, pregled pet
          domena, pravila na dan ispita i plan učenja.

  - type: course-overview.html
    section_id: exam
    background_style: bg-subtle
    title: Usklađenost s ispitom
    text: >-
      Tečaj pokriva svih pet domena iz vodiča za ispit Claude Certified
      Architect – Foundations. Ispit se temelji na scenarijima: svako polaganje
      nasumično izvlači četiri od šest scenarija, a na tečaju se vježba svih šest.
      Isprobajte [20 besplatnih probnih pitanja](/training/claude-mock-exams/#ccar-f)
      za ovaj ispit, s objašnjenjem svakog odgovora (na engleskom).
      Ne znate koji ispit odabrati? Pogledajte
      [usporedbu svih pet Claude certifikacija](/hr/edukacija/claude-certifikacije/).
    facts:
      - label: Oznaka ispita
        value: CCAR-F
      - label: Pitanja
        value: "60"
      - label: Trajanje
        value: 120 minuta
      - label: Prolazni rezultat
        value: 720 / 1.000
      - label: Cijena ispita
        value: 125 USD
    columns:
      - title: Preduvjeti
        items:
          - Iskustvo u projektiranju ili razvoju softverskih sustava, najbolje i s LLM-ovima
          - Čitanje i pokretanje Python koda; vježbe koriste Python 3.11+, Claude API i Agent SDK
          - Laptop s instaliranim Pythonom, VS Codeom, Gitom i Claude Codeom
          - Claude API ključ ili pristup Amazon Bedrocku, najbolje vaš; pomažem s postavljanjem
      - title: Polaganje ispita
        items:
          - Polaže se kod Pearson VUE-a, online uz nadzor ili u ispitnom centru
          - Prijava ide preko Anthropic Partner Academyja, za što tvrtka kandidata mora biti članica Claude Partner Networka
          - Pitanja s jednim ili više točnih odgovora, skalirani rezultat od 100 do 1.000
          - Certifikat vrijedi 12 mjeseci

  - type: faq.html
    section_id: faq
    title: Dobro je znati
    items:
      - q: Tko predaje?
        a: >-
          Ja. AWS Authorized Instructor i Claude Certified Architect –
          Professional, s više od 20 godina iskustva u razvoju softvera.
          Svakodnevno projektiram produkcijske Claude sustave, primjerice
          privatnu Claude platformu s punim audit tragom na Amazon Bedrocku za
          reguliranu organizaciju i interni marketplace Claude Code pluginova, i
          odatle dolaze primjeri na tečaju. Više na [naslovnoj stranici](/hr/).

      - q: Online ili uživo, i na kojem jeziku?
        a: >-
          Online uživo, u blokovima od pola dana, ili kod vas, bilo gdje u
          Hrvatskoj i Europi; putni troškovi naplaćuju se po stvarnom trošku.
          Tečaj se održava na hrvatskom ili engleskom, za do 20 polaznika po
          grupi.

      - q: Može li se tečaj prilagoditi našem timu?
        a: >-
          Može. Gornji program je jezgra usklađena s ispitom; primjere i vježbe
          projektiranja prilagođavam vašoj arhitekturi i slučajevima primjene.
          Prije tečaja dobivate detaljan program na odobrenje.

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
          Certified Architect – Foundations, ali nije službeni Anthropicov tečaj.
          Ispit se polaže kod Pearson VUE-a; prijava ide preko Anthropic Partner
          Academyja, za što tvrtka polaznika mora biti članica Claude Partner
          Networka.

  - type: contact.html
    section_id: contacts
    title: Dogovorimo tečaj
    watermark: CCAR-F
    text: >-
      Recite mi nešto o timu i sustavima koje projektira. Kratak poziv obično je
      dovoljan da dogovorimo format, primjere i termine.
    actions:
      - title: Dogovorite poziv
        icon: fa-calendar-alt
        url: https://calendly.com/prlic/15min
      - title: ivan@prlic.io
        icon: fa-envelope
        url: mailto:ivan@prlic.io?subject=Te%C4%8Daj%3A%20Arhitektura%20s%20Claudeom%20(CCAR-F)
      - title: LinkedIn
        icon: fa-linkedin
        icon_type: fab
        url: https://www.linkedin.com/in/iprlic/
---
