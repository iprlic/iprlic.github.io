---
layout: home
permalink: /hr/edukacija/claude-pojmovi/
lang: hr
ref: training-claude-confusions
last_updated: 2026-11-20
sticky_cta:
  label: Dogovorite poziv
  url: https://calendly.com/prlic/15min
image:
  path: /assets/img/og-image.png
  width: 1200
  height: 630
locale: hr_HR
title: "Claude pojmovi koji se često brkaju: 14 parova"
description: >-
  Caching ili compaction, streaming ili batch, Skills ili MCP, hookovi ili dozvole: 14 Claude pojmova koji se brkaju i koji ih ispit provjerava.

header:
  compact: true
  title: Claude pojmovi koji se često brkaju
  subtitle: Četrnaest parova koji zvuče slično, kada koristiti koji i koji ih ispit provjerava
  text: >-
    Većina pogrešnih odgovora na Claude certifikacijskim ispitima nije
    posljedica nepoznate funkcionalnosti, nego dviju stvarnih funkcionalnosti
    koje zvuče slično, a scenarij odgovara samo jednoj. Ovo su parovi o kojima
    najčešće ovisi točan odgovor na probnim pitanjima, svaki s pravilom, kratkim
    primjerom i ispitima koji ga provjeravaju. Nazivi funkcionalnosti ostali
    su na engleskom, kao u dokumentaciji i na ispitu.
  action:
    label: Krenite od API-ja
    url: '#api'
  proof:
    - Provjereno prema Anthropicovoj dokumentaciji
    - Ažurirano 20. studenoga 2026.
    - Neovisan vodič, nije povezan s Anthropicom

sections:
  - type: course-overview.html
    section_id: api
    background_style: bg-subtle
    title: Pozivanje Claude API-ja
    text: >-
      Oznake ispita: CCAO-F Associate, CCDV-F Developer – Foundations, CCAR-F
      Architect – Foundations, CCDV-P Developer – Professional, CCAR-P
      Architect – Professional ([usporedba](/hr/edukacija/claude-certifikacije/)).
    columns:
      - title: Streaming ili Message Batches
        text: >-
          **Streaming** kad netko čeka: tekst se pojavljuje dok nastaje, a
          dugi odgovori ne udaraju u HTTP timeout. Normalna cijena i normalna
          ograničenja.


          **Batch** kad nitko ne čeka: do 100.000 zahtjeva po batchu,
          rezultati unutar 24 sata (većina završi unutar sat vremena), po
          upola nižoj cijeni.


          *Primjer:* chat za korisničku podršku koristi streaming; noćna
          klasifikacija 40.000 tiketa ide u batch.


          **Provjerava se na:** CCDV-F, CCAR-F, CCDV-P

      - title: Šest stop reasona koji su bitni
        text: >-
          **end_turn**: Claude je gotov, koristite odgovor. **tool_use**:
          pokrenite alat i vratite `tool_result`. **max_tokens**: vaše
          ograničenje izlaza prekinulo je odgovor; povećajte ga ili nastavite.
          **pause_turn**: petlja serverskog alata, npr. web searcha, došla je
          do ograničenja iteracija; vratite sadržaj asistenta nepromijenjen da
          Claude nastavi. **refusal**: Claude je odbio iz sigurnosnih razloga;
          stiže kao normalan odgovor, ne kao greška.
          **model_context_window_exceeded**: kontekstni prozor je pun;
          odgovor je odrezan, a rješenje je manje konteksta, ne veći
          `max_tokens`.


          *Primjer:* petlja agenta koja provjerava samo `end_turn` i
          `tool_use` tiho izgubi posao kad web search vrati `pause_turn`.


          **Provjerava se na:** CCDV-F, CCAR-F, CCDV-P

      - title: "tool_choice: auto, any, tool ili none"
        text: >-
          **auto** (zadano kad postoje alati): Claude odlučuje hoće li
          pozvati alat. **any**: mora pozvati jedan od vaših alata. **tool**:
          mora pozvati baš onaj koji navedete. **none**: bez poziva alata.


          **Zamke:** prisilni poziv (`any` ili `tool`) počinje odgovor
          pozivom alata, pa prije njega nema ni teksta ni razmišljanja. Ručni
          extended thinking prihvaća samo `auto` i `none`, a neki aktualni
          modeli prisilne pozive uopće ne podržavaju; ondje koristite `auto`
          sa strict alatima ili structured outputs.


          *Primjer:* "uvijek pozovi `record_invoice`" je `tool`, ako ga model
          dopušta; inače zapis dobijte kroz structured outputs.


          **Provjerava se na:** CCDV-F, CCAR-F

      - title: Prompt caching, context editing ili compaction
        text: >-
          **Prompt caching** kad se isti dugi početak prompta (alati, sistemski
          prompt, dokumenti) šalje ponovno unutar nekoliko minuta: ponovno
          čitanje stoji djelić cijene i brže je. Ne mijenja ni odgovor ni to
          koliko kontekstnog prozora trošite.


          **Context editing** kad se kontekst agenta puni starim rezultatima
          alata ili razmišljanjem koje mu više ne treba: API ih po pravilu
          briše prije nego zahtjev stigne do Claudea.


          **Compaction** kad je sam razgovor predug, a njegov sadržaj je bitan:
          stariji dio razgovora zamjenjuje se sažetkom koji napiše Claude.


          Brisanje ili sažimanje mijenja početak prompta, pa cache od te
          točke više ne vrijedi; to je cijena.


          *Primjer:* agent za kodiranje cachira alate i upute, briše stara
          čitanja datoteka i sažima razgovor kad sesija traje satima.


          **Provjerava se na:** CCDV-F, CCDV-P, CCAR-P

      - title: Structured outputs ili tool use za JSON
        text: >-
          **Structured outputs** (JSON shema u `output_config.format`) kad
          želite da sam Claudeov odgovor bude JSON: odgovor je ograničen na
          shemu, pa se uvijek može parsirati.


          **Strict tool use** (`strict: true` na alatu) kad Claude bira akcije,
          a argumenti svakog poziva alata moraju odgovarati shemi alata.


          Prisiljavanje jednog "lažnog" alata da biste dobili JSON stariji je
          zaobilazni put; i dalje se pojavljuje u scenarijima na ispitu.


          *Primjer:* izvlačenje polja iz računa je structured outputs; agent
          koji poziva `issue_refund` s iznosom je strict alat.


          **Provjerava se na:** CCDV-F, CCAR-F

      - title: Pretraživanje (RAG), dugi kontekst ili Files API
        text: >-
          **Dugi kontekst** kad materijal udobno stane u prozor i zadatak
          treba sve: jedan ugovor, jedno izvješće. Uz ponovljena pitanja
          dodajte caching.


          **Pretraživanje** kad je zbirka mnogo veća od prozora ili se često
          mijenja: za svako pitanje dohvatite samo relevantne dijelove i
          citirajte ih.


          **Files API** nije treći način pronalaženja informacija. Datoteku
          učitate jednom i pozivate se na nju preko `file_id`; njezin sadržaj
          i dalje se naplaćuje kao ulazni tokeni i mora stati u kontekstni
          prozor.


          *Primjer:* pitanja nad 20.000 internih pravilnika traže
          pretraživanje; sažetak jednog PDF-a od 80 stranica traži dugi
          kontekst, učitan jednom kroz Files API ako ga koristi više zahtjeva.


          **Provjerava se na:** CCDV-F, CCDV-P, CCAR-P

  - type: course-overview.html
    section_id: agents
    title: Agenti i proširenja
    columns:
      - title: Agent ili workflow
        text: >-
          **Workflow** kad korake možete unaprijed zapisati: vaš kod određuje
          put (niz koraka, grananje, paralelno izvođenje), a Claude odrađuje
          svaki korak. Predvidljivo, jeftinije, lakše za testiranje.


          **Agent** kad koraci ovise o onome što Claude usput otkrije: Claude
          bira sljedeći poziv alata i odlučuje kad je gotov. Isplati se kad je
          fleksibilnost važnija od predvidljivosti; dajte mu jasne alate,
          ograničenja i uvjet zaustavljanja.


          *Primjer:* izvući, provjeriti i proknjižiti račun je workflow;
          "otkrij zašto ovom klijentu ne radi sinkronizacija" je agent.


          **Provjerava se na:** CCDV-F, CCAR-F, CCAR-P, CCDV-P

      - title: Alat, Skill, MCP server ili plugin
        text: >-
          **Alat** (tool): jedna funkcija koju Claude može pozvati, opisana
          imenom, opisom i shemom ulaza.


          **MCP server**: zasebna usluga koja kroz Model Context Protocol
          izlaže alate (te resurse i promptove), pa jedna integracija s
          vanjskim sustavom radi u svakom MCP klijentu.


          **Skill**: mapa sa `SKILL.md` i po želji skriptama i datotekama;
          Claude je učita kad zadatak to traži. Dodaje znanje, ne povezivanje.


          **Plugin** (Claude Code): pakiranje. Spaja skillove, subagente,
          hookove i MCP servere u jednu cjelinu koja se instalira odjednom i
          dijeli kroz marketplace.


          *Primjer:* MCP server spaja Claudea s Jirom, skill sadrži vaša
          pravila za trijažu tiketa, a plugin oboje isporučuje svakom
          inženjeru.


          **Provjerava se na:** CCDV-F, CCAR-F

      - title: Subagent, agent team ili Managed Agents sesija
        text: >-
          **Subagent** kad se usmjereni zadatak treba odraditi u vlastitom
          kontekstnom prozoru, a bitan je samo rezultat: vraća sažetak agentu
          koji ga je pokrenuo, pa glavni kontekst ostaje čist.


          **Agent team** (Claude Code, eksperimentalno) kad više izvršitelja
          mora dijeliti nalaze i preispitivati jedni druge: voditelj,
          zajednička lista zadataka i izravne poruke među članovima. Troši
          mnogo više tokena.


          **Managed Agents sesija** kad vaš proizvod treba dugotrajnog agenta
          na hostanoj infrastrukturi: preko API-ja pokrenete sesiju agenta
          kojeg ste definirali i s njim razmjenjujete događaje, bez vlastite
          petlje i sandboxa.


          *Primjer:* usporedba triju biblioteka paralelno ide preko
          subagenata; pet recenzenata koji raspravljaju o uzroku greške je
          agent team; noćni agent bez nadzora za vaše korisnike ide na Managed
          Agents.


          **Provjerava se na:** CCAR-F, CCDV-F, CCDV-P

  - type: course-overview.html
    section_id: claude-code
    background_style: bg-subtle
    title: Konfiguracija Claude Codea
    columns:
      - title: Hookovi, pravila dozvola ili sandbox
        text: >-
          **Pravila dozvola** (allow, ask, deny) određuju smije li se poziv
          alata uopće izvršiti. Vrijede za sve alate i provjeravaju se prije
          poziva.


          **Hookovi** pokreću vašu naredbu na određenom događaju, npr. prije
          ili poslije poziva alata, svaki put i bez Claudeove odluke. Za ono
          što se mora dogoditi uvijek: blokirati izmjenu, pokrenuti
          formatiranje, zapisati log.


          **Sandbox** ograničava što Bash naredbe i njihovi podprocesi mogu
          dohvatiti na datotečnom sustavu i mreži dok se izvršavaju, a to
          provodi operacijski sustav. Ne pokriva ugrađene alate za datoteke,
          MCP servere ni hookove.


          *Primjer:* čitanje `.env` zabranite pravilom dozvola, linter nakon
          svake izmjene pokrenite hookom, a build skriptu spriječite da zove
          nepoznate hostove sandboxom.


          **Provjerava se na:** CCAR-F, CCDV-F, CCDV-P

      - title: CLAUDE.md, rules, Skills ili settings.json
        text: >-
          **CLAUDE.md**: upute koje se učitavaju u svakoj sesiji, npr. naredbe
          za build i konvencije. Claude ih slijedi kao smjernice; ništa ih ne
          nameće.


          **.claude/rules/**: iste vrste uputa u zasebnim datotekama; s
          `paths` u zaglavlju učitavaju se samo kad Claude radi na datotekama
          koje odgovaraju.


          **Skills**: znanje ili postupci koji se učitavaju po potrebi ili
          pokreću s `/ime`.


          **settings.json**: konfiguracija koju Claude Code provodi, npr.
          dozvole, hookovi, varijable okruženja i model.


          *Primjer:* "koristi pnpm" ide u CLAUDE.md, konvencije testova za
          `src/api/**` u rule, checklista za izdanje u skill, a "nikad push"
          kao deny pravilo u settings.json.


          **Provjerava se na:** CCAR-F, CCDV-F

  - type: course-overview.html
    section_id: quality
    title: Claude aplikacije, kvaliteta i sam ispit
    columns:
      - title: Projects, Skills ili konektori u Claudeu
        text: >-
          **Project** kad tim dulje radi na jednoj temi: upute i datoteke
          znanja projekta dostupne su u svakom razgovoru unutar njega.


          **Skill** kad je riječ o postupku koji želite u bilo kojem
          razgovoru, a učitava se samo kad zadatak to traži: format izvješća,
          pravila brenda.


          **Konektor** kad Claude treba aktualne podatke iz druge aplikacije
          ili u njoj nešto napraviti.


          *Primjer:* projekt za natječaj u četvrtom kvartalu s natječajnom
          dokumentacijom, skill za format vaših ponuda, konektor koji s
          dijeljenog diska povuče ovotjedni cjenik.


          **Provjerava se na:** CCAO-F

      - title: Evaluacija kodom, LLM sucem ili ljudima
        text: >-
          **Kodom** kad pravilo može odlučiti: točno podudaranje, valjan JSON,
          test koji prolazi. Brzo, jeftino, ponovljivo; koristite gdje god
          možete.


          **LLM kao sudac** kad je kvaliteta stvar prosudbe, ali je možete
          zapisati kao kriterije: vjernost izvoru, ton. Skalira se, ali ga
          prvo kalibrirajte prema ljudskim ocjenama.


          **Ljudska procjena** za visoke uloge, nove zadatke i izradu
          referentnog skupa prema kojem se provjeravaju druga dva načina.


          *Primjer:* točnost klasifikacije tiketa ocjenjuje kod; "je li
          sažetak vjeran ugovoru?" LLM sudac s kriterijima, uz povremenu
          provjeru pravnog tima.


          **Provjerava se na:** CCAO-F, CCDV-F, CCDV-P, CCAR-P

      - title: Skalirani rezultat ili postotak točnih
        text: >-
          **Skalirani rezultat** odlučuje o prolazu: od 100 do 1.000,
          prolaz je 720. Skaliranje ujednačava male razlike u težini između
          verzija ispita, pa 720 nije 72 % točnih.


          **Postoci** se na izvješću o rezultatu prikazuju po dijelovima
          ispita. Služe za pronalaženje slabih domena, ne za izračun prolaza.
          Pitanja koja se ne boduju (10 od 70 na novijim ispitima, nisu
          označena) ne ulaze ni u jedno ni u drugo.


          *Primjer:* dva kandidata s istim brojem točnih odgovora na različitim
          verzijama ispita mogu dobiti različit skalirani rezultat.


          **Provjerava se na:** svih pet ispita (tako se boduju)
    note: >-
      Vježbajte parove na pitanjima kakva su na ispitu:
      [besplatna probna pitanja](/training/claude-mock-exams/), 20 po ispitu,
      svako s objašnjenjem (na engleskom). Format ispita se mijenja; pogledajte
      [pregled promjena po datumima](/hr/edukacija/claude-certifikacije-promjene/).
      Detalji o funkcionalnostima provjereni su prema Anthropicovoj
      dokumentaciji 20. studenoga 2026.

  - type: faq.html
    section_id: faq
    background_style: bg-subtle
    title: Pitanja o ovim pojmovima
    items:
      - q: Koja je razlika između prompt cachinga, context editinga i compactiona?
        a: >-
          Prompt caching čini ponovno slanje istog početka prompta jeftinijim
          i bržim, ali iz konteksta ništa ne uklanja. Context editing po
          pravilu briše određeni sadržaj, npr. stare rezultate alata ili
          blokove razmišljanja, prije nego zahtjev stigne do Claudea.
          Compaction stariji dio razgovora zamjenjuje sažetkom koji napiše
          Claude. Caching štedi novac, a druga dva štede prostor u kontekstu i
          poništavaju cache od mjesta na kojem mijenjaju prompt.

      - q: Koje stop reasone mora obraditi petlja agenta?
        a: >-
          Barem `end_turn` (gotovo), `tool_use` (pokrenite alat i vratite
          rezultat), `max_tokens` (izlaz je prekinulo vaše ograničenje),
          `pause_turn` (petlja serverskog alata je zastala; vratite odgovor da
          se nastavi), `refusal` (Claude je odbio) i
          `model_context_window_exceeded` (kontekstni prozor je pun, izlaz je
          odrezan). `stop_sequence` je bitan samo ako ste zadali stop
          sekvence.

      - q: Kada koristiti Message Batches API umjesto streaminga?
        a: >-
          Kad nitko ne čeka odgovor. Batch stoji upola manje i prima do
          100.000 zahtjeva, ali rezultati mogu stići i nakon 24 sata.
          Streaming je za interaktivnu upotrebu, kad korisnik treba vidjeti
          odgovor dok nastaje.

      - q: Koja je razlika između Skilla, MCP servera i plugina?
        a: >-
          MCP server povezuje Claudea s vanjskim sustavom i daje mu alate.
          Skill daje Claudeu upute i znanje, a učitava se kad ih zadatak
          treba. Plugin u Claude Codeu pakira skillove, subagente, hookove i
          MCP servere da ih tim instalira u jednom koraku.

      - q: Je li 720 na Claude ispitu isto što i 72 % točnih odgovora?
        a: >-
          Nije. 720 je skalirani rezultat na ljestvici od 100 do 1.000.
          Skaliranje uzima u obzir male razlike u težini između verzija
          ispita, pa ne postoji fiksni postotak koji znači prolaz. Postoci po
          dijelovima ispita na izvješću pokazuju gdje ste bili slabiji.

      - q: Je li certifikat Claude Academyja isto što i Claude certifikacija?
        a: >-
          Nije. Potvrda o završetku (certificate of completion) iz Anthropicove
          javne Claude Academy pokazuje da ste završili tečaj i riješili kviz.
          Claude certifikacija je ispit pod nadzorom kod Pearson VUE-a, s
          rezultatom od 100 do 1.000 i prolazom na 720, vrijedi 12 mjeseci i
          dostupna je samo zaposlenicima tvrtki iz Claude Partner Networka.
          Pogledajte [tko može polagati ispite](/hr/edukacija/claude-ispiti-uvjeti/).

  - type: contact.html
    section_id: contacts
    title: Naučite to kako treba
    watermark: CLAUDE
    text: >-
      Svaki moj pripremni tečaj obrađuje ove razlike kroz praktične vježbe,
      ne samo kroz slajdove. Javite mi za koji se ispit vaš tim sprema.
    actions:
      - title: Dogovorite poziv
        icon: fa-calendar-alt
        url: https://calendly.com/prlic/15min
      - title: ivan@prlic.io
        icon: fa-envelope
        url: mailto:ivan@prlic.io?subject=Claude%20certifikacija
      - title: LinkedIn
        icon: fa-linkedin
        icon_type: fab
        url: https://www.linkedin.com/in/iprlic/
---
