# Combattimento

La sezione **Combattimento** di DnDino è il tracker operativo dello scontro. È pensata per essere rapida, compatta e leggibile mentre il tavolo è nel momento più concitato della sessione.

Il combattimento nasce sempre nel contesto di un **luogo** e porta con sé gli eroi dell'avventura, le presenze locali e gli eventuali mostri o PNG collegati alla scena.

Questa pagina spiega:

- la preparazione del pre-combattimento
- l'inserimento e l'ordinamento dell'iniziativa
- la schermata principale del combattimento
- i controlli del turno
- attacchi, danni, cure, condizioni e tiri salvezza
- uso dei link interni negli attacchi e nelle abilità
- riepilogo laterale, ultimi eventi e undo
- Finestra Giocatori
- riepilogo finale e statistiche

## Utilizzo con uno o due schermi

Il combattimento funziona bene anche su **schermo singolo**: tutta la parte operativa resta nella schermata principale, con tracker iniziativa, schede compatte e riepilogo.

Con un secondo schermo puoi usare anche la **Finestra Giocatori**:

- sullo schermo del DM restano controlli, schede, bersagli, condizioni e statistiche
- sullo schermo dei giocatori appare una presentazione pulita con immagini e overlay

!!! tip
    Il secondo schermo non è obbligatorio. Serve solo se vuoi separare il pannello tecnico del DM dalla presentazione evocativa per i giocatori.

## Finestra Giocatori durante il combattimento

Quando lo scontro viene avviato, DnDino può aprire o aggiornare automaticamente la **Finestra Giocatori**.

Se la presentazione è attiva, può mostrare:

- intro iniziale con i partecipanti
- partecipante del turno corrente
- animazione degli attacchi
- riepilogo finale

L'overlay può includere:

- round
- PF attuali, massimi e temporanei
- condizioni
- prossimo turno

Per nemici, mostri e PNG puoi scegliere se mostrare nomi e dettagli ai giocatori dalle impostazioni.

## Impostazioni utili

Le opzioni principali sono in **Impostazioni**, nelle sezioni dedicate a combattimento e Finestra Giocatori.

Le più importanti sono:

- `Apri la finestra giocatori anche con un solo monitor`
- `Mostra controlli finestra giocatori nella topbar`
- `Mostra intro combattimento ai giocatori`
- `Mostra riepilogo finale ai giocatori`
- `Mostra round nella schermata giocatori`
- `Mostra PF nella schermata giocatori`
- `Mostra condizioni nella schermata giocatori`
- `Mostra prossimo turno nella schermata giocatori`
- `Mostra dettagli di PNG e mostri ai giocatori`
- `Mostra condizioni dei nemici ai giocatori`
- `Mostra i nomi dei nemici ai giocatori`

La conferma di fine combattimento viene sempre richiesta, perché chiudere uno scontro sincronizza dati e statistiche.

## Dove si apre il combattimento

Il combattimento si crea dal contesto di un **luogo**. Una volta aperto, la schermata cambia in base allo stato dello scontro:

- **Pre-combattimento**: prepari partecipanti, nomi e iniziative.
- **Combattimento attivo**: gestisci turno, schede, bersagli e riepilogo.
- **Combattimento concluso**: consulti il riepilogo finale del DM.

## Pre-combattimento

Il pre-combattimento serve a preparare lo scontro prima del primo turno.

In questa fase la schermata usa tre aree principali:

- colonna **Eroi**
- colonna **Mostri e PNG**
- pannello **Ordine finale**

In alto trovi anche il nome dell'incontro, il numero dei partecipanti e le azioni principali.

## Azioni del pre-combattimento

Le azioni principali sono:

- `Aggiungi`
- `Avvia scontro`
- `Init PNG/Mostri`, nella colonna di mostri e PNG

`Aggiungi` apre il selettore dei partecipanti.

`Avvia scontro` avvia il combattimento. Se almeno un partecipante ha iniziativa `0`, DnDino chiede conferma.

`Init PNG/Mostri` tira automaticamente l'iniziativa solo per mostri e PNG. Gli eroi restano pensati per l'inserimento manuale, perché di solito il valore arriva dal tavolo.

## Modifica di nomi e iniziativa

Nel pre-combattimento puoi correggere:

- nome mostrato del partecipante
- iniziativa

Questo è utile soprattutto per i mostri, per esempio quando vuoi distinguere:

- Goblin 1
- Goblin 2
- Capitano Goblin

L'iniziativa viene recepita mentre scrivi, senza dover uscire dal campo. L'ordine delle colonne operative non viene rimescolato continuamente mentre stai digitando: l'ordinamento definitivo viene applicato all'avvio dello scontro.

## Ordine finale

Il pannello **Ordine finale** mostra l'anteprima sempre aggiornata dell'ordine che verrà usato quando avvii lo scontro.

L'ordine viene calcolato così:

1. iniziativa più alta
2. in caso di pareggio, modificatore di Destrezza più alto
3. se il pareggio resta, spareggio casuale

Questo pannello serve a controllare il risultato senza disturbare la fase di inserimento.

## Da dove arrivano i partecipanti

Il pannello di aggiunta può proporre:

- `Eroi`
- `Presenze Luogo`
- `Globali`

Gli eroi già collegati all'avventura possono entrare una sola volta nello stesso combattimento.

Le presenze del luogo riusano lo stato locale, se disponibile.

I mostri globali possono essere aggiunti più volte, perché spesso rappresentano più copie della stessa creatura.

## Combattimento attivo

Quando avvii lo scontro, la schermata passa alla gestione operativa.

La struttura è divisa in tre zone:

- a sinistra il **tracker iniziativa**
- al centro le schede compatte del **turno corrente** e del **selezionato**
- a destra il **riepilogo** di salute, danni ed eventi

L'obiettivo è vedere più informazioni possibili senza aprire pannelli enormi.

## Controlli del turno

In alto trovi i controlli principali.

A sinistra:

- `Precedente`
- `Pausa` / `Riprendi`
- `Successivo`
- `Annulla evento`

A destra:

- `Aggiungi`
- `Ordina`
- `Fine combattimento`

`Precedente` e `Successivo` cambiano turno.

`Pausa` ferma il timer del combattimento. Quando il combattimento è in pausa diventa `Riprendi`.

`Annulla evento` permette di ripristinare uno degli ultimi eventi annullabili.

`Aggiungi` inserisce altri partecipanti anche a combattimento iniziato.

`Ordina` ricostruisce l'ordine di iniziativa.

`Fine combattimento` chiude lo scontro dopo conferma.

## Tracker iniziativa

La colonna sinistra mostra tutti i partecipanti in modo compatto.

Ogni riga mostra:

- iniziativa
- nome
- CA
- PF
- PF temporanei
- eventuale indicatore condizioni
- colore del ruolo

Il colore laterale aiuta a distinguere:

- eroi
- alleati
- neutrali
- nemici

Cliccando una riga:

- il partecipante viene aperto come **selezionato**
- se era già selezionato, la colonna del selezionato si richiude

Il cestino sulla riga rimuove il partecipante dal combattimento.

## Schede compatte del turno e del selezionato

Al centro puoi vedere fino a due schede:

- il partecipante di turno
- il partecipante selezionato dalla lista

Le schede hanno larghezza fissa e scroll verticale interno, così la pagina resta stabile anche con testi lunghi.

Nella parte superiore della scheda trovi:

- nome
- tipo, razza o sottotipo
- linguaggi, se presenti
- grado sfida e PE, se presenti
- anteprima immagine
- pulsanti operativi

## Campi rapidi nella scheda

Nella scheda puoi modificare direttamente:

- PF attuali
- PF temporanei
- iniziativa

La CA viene mostrata come valore compatto con icona scudo.

Per gli eroi collegati all'avventura può comparire anche il pulsante di **Ispirazione Eroica**.

Le modifiche ai PF vengono tenute allineate con la lista a sinistra e con il riepilogo a destra.

## Azioni del partecipante

Ogni scheda può mostrare i pulsanti:

- `Attacca`
- `Danni`
- `Cura`
- `TS`
- `Condizioni`
- `Note DM`
- `Modifica`

`Attacca` apre una finestra con l'attaccante e la lista dei bersagli.

`Danni` applica danni diretti al partecipante.

`Cura` applica guarigione diretta.

`TS` apre i tiri salvezza disponibili.

`Condizioni` apre una finestra dedicata, utile perché la gestione delle condizioni richiede più spazio.

`Note DM` salva appunti sul partecipante. Le note non rientrano nell'undo.

`Modifica` apre la scheda completa del partecipante.

## Lista bersagli

Le liste bersagli sono ordinate in modo contestuale.

Se l'attaccante è un nemico:

- prima eroi e alleati
- poi neutrali
- poi nemici

Se l'attaccante è un eroe, un alleato o un neutrale:

- prima nemici
- poi neutrali
- poi eroi e alleati

Dentro ogni gruppo i nomi sono ordinati alfabeticamente.

La linea colorata laterale aiuta a riconoscere il ruolo del bersaglio.

## Attacchi, abilità e link interni

Le sezioni principali sono:

- `Condizioni`
- `Attacchi`
- `Abilità speciali`
- `Abilità`
- `Incantesimi`
- `Descrizione`

Le sezioni sono collassabili e usano un leggero gradiente colorato coerente con il titolo.

I testi di attacchi, abilità speciali e abilità possono contenere link interni creati nella scheda del personaggio, durante la creazione o la modifica.

Durante il combattimento questi link aprono finestre dedicate, così puoi risolvere l'azione con più spazio.

I link più utili sono:

- `Attacco completo`
- `1d20 + MOD`
- tiro libero
- tiro di danno
- collegamenti a entità interne

## Attacco completo

`Attacco completo` è pensato per i testi di attacco dei mostri, PNG o eroi.

Lo prepari nella schermata di creazione o modifica del personaggio: selezioni il testo dell'attacco e crei un link di tipo `Attacco completo`. Da quel momento, durante il combattimento, quel testo diventa un'azione pronta da aprire e risolvere.

Quando lo usi in combattimento:

- la finestra mostra il nome dell'attacco
- viene indicato l'attaccante
- puoi scegliere uno o più bersagli
- puoi gestire più righe di danno
- applichi il danno selezionato ai bersagli scelti

In fase di creazione il danno è modulare: puoi aggiungere righe con il pulsante `+` e visualizzare solo quelle valorizzate.

## Incantesimi

Se il partecipante ha incantesimi, la scheda mostra la sezione `Incantesimi`.

Gli incantesimi sono raggruppati per livello.

Per mostri e PNG, la riga del livello può mostrare anche il contatore degli slot usati, per esempio:

- `0/3`
- `2/3`
- `3/3`

Il pulsante `Usa` sul singolo incantesimo incrementa il contatore del livello.

Il contatore non blocca l'utilizzo quando arriva al massimo: serve come promemoria per il DM.

I trucchetti non usano slot.

## Condizioni

La finestra `Condizioni` permette di:

- aggiungere condizioni
- rimuovere condizioni
- scegliere durata
- collegare la scadenza al turno di un partecipante
- gestire note collegate

Quando una condizione viene applicata, DnDino mostra feedback visivo sulla schermata e sulla riga interessata.

## Eroi a 0 PF o meno

Gli eroi seguono una regola diversa rispetto a mostri e PNG.

Un eroe può scendere sotto `0` PF.

La regola è:

- tra `0` e `-(PF massimi - 1)` è **Incosciente**
- a `-PF massimi` o meno muore
- muore anche se raggiunge 3 fallimenti nei tiri salvezza contro la morte

Quando un eroe è a `0` PF o meno ma non è morto, nella scheda compare la sezione per i **Tiri salvezza contro la morte**.

Se raggiunge 3 successi, torna a `1` PF.

## PNG e mostri a 0 PF

Per PNG e mostri la regola è più semplice:

- a `0` PF o meno sono considerati morti
- vengono esclusi dal ciclo dei turni
- nel riepilogo possono apparire con stato morto

## Riepilogo laterale

La colonna destra mostra il **Riepilogo**.

Qui trovi:

- round
- durata
- turno corrente
- salute di eroi e alleati
- salute di PNG e mostri
- danni fatti
- danni subiti
- ultimi 5 eventi

È una vista di controllo: non serve per modificare, ma per leggere subito la situazione dello scontro.

I PF cambiano colore:

- normale se il partecipante è in buone condizioni
- giallo sotto il 50%
- arancione sotto il 10%
- rosso se è a 0 o meno

Per gli eroi i PF vengono barrati solo quando il personaggio è morto davvero, non quando è semplicemente sotto 0 PF.

## Ultimi 5 eventi e undo

Il combattimento conserva gli ultimi eventi annullabili.

Possono rientrare nell'undo:

- attacchi
- danni applicati da attacchi
- cure, se gestite come evento annullabile
- condizioni applicate o modificate

Le `Note DM` non vengono annullate.

L'undo ripristina anche le statistiche collegate, così i danni fatti e subiti non restano sballati.

Questo è importante perché la somma dei danni inflitti dai partecipanti deve restare coerente con la somma dei danni subiti.

## Feedback visivo

Quando succede qualcosa nel combattimento, DnDino mostra feedback immediato:

- banner in alto
- animazione sulla riga del partecipante coinvolto
- effetto sul pulsante `Applica`, quando previsto
- aggiornamento del riepilogo laterale

Questo serve a capire subito che il comando è stato recepito.

## Riepilogo finale dello scontro

Quando confermi la fine del combattimento, lo scontro non è più modificabile.

La schermata finale mostra:

- round totali
- durata
- nemici uccisi
- danni inflitti
- danni subiti
- stato finale dei partecipanti

I PF finali e le condizioni vengono sincronizzati con i record collegati.

## Sincronizzazione finale

Alla chiusura del combattimento, DnDino sincronizza i dati dove serve.

Per gli eroi dell'avventura:

- PF attuali
- PF temporanei
- condizioni
- stato finale

Per le presenze del luogo con stato locale:

- PF attuali
- PF temporanei
- condizioni
- stato finale

Inoltre il combattimento può alimentare i dati della **sessione live** e delle statistiche.

## Statistiche

DnDino usa i combattimenti conclusi per alimentare statistiche e grafici.

Le statistiche possono includere:

- danni inflitti
- danni subiti
- durata degli scontri
- numero di combattimenti
- nemici uccisi
- andamento dei danni per giorno
- durata media delle sessioni

Nella dashboard dell'avventura è disponibile una vista **Statistiche Avventura** che raccoglie i combattimenti completati, anche fuori da una singola sessione live, e li raggruppa in modo consultabile.

Nel riepilogo della sessione live, invece, i grafici possono mostrare i dati dei combattimenti completati durante quella sessione.

## Quando il combattimento rende di più

Il combattimento di DnDino rende al massimo quando:

1. prepari bene il pre-combattimento
2. assegni iniziative e nomi prima di partire
3. usi il tracker sinistro per non perdere mai il quadro generale
4. tieni aperta la scheda del turno e, quando serve, quella del bersaglio selezionato
5. sfrutti i link negli attacchi e nelle abilità
6. usi il riepilogo laterale per controllare salute, danni e ultimi eventi
7. chiudi lo scontro solo quando sei sicuro, così statistiche e sincronizzazioni restano pulite

!!! tip
    Anche se DnDino automatizza molte operazioni, puoi continuare a tirare fisicamente i dadi. In quel caso usa il combattimento soprattutto per applicare danni, cure e condizioni in modo rapido, evitando calcoli manuali ripetuti sui PF e sulle statistiche.
