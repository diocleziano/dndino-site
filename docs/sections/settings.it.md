# Impostazioni

La sezione **Impostazioni** raccoglie le preferenze globali di DnDino. Qui non si lavora su una singola avventura o su un singolo personaggio, ma si definisce **come deve comportarsi l'app nel suo insieme**.

Le impostazioni influenzano soprattutto:

- l'aspetto generale dell'interfaccia
- il comportamento della topbar
- il flusso di `Luoghi`
- il comportamento del `Combattimento`
- la gestione di immagini, backup e snapshot
- il supporto e la diagnostica del database

## Come è organizzata la schermata

La pagina è divisa in due aree:

- una **barra laterale sinistra** con le categorie
- un **pannello principale** a destra con le opzioni della sezione selezionata

Le categorie disponibili sono:

- `Generali`
- `Topbar`
- `Luoghi`
- `Combattimento`
- `Media`
- `Tema`
- `Database e Media`
- `Supporto`
- `Licenze`

Questa struttura separa bene le preferenze d’uso quotidiano da quelle più tecniche, come backup e diagnostica.

## Generali

La sezione `Generali` raccoglie le preferenze di base dell'app.

### Profilo DM

Qui puoi personalizzare il tuo profilo con:

- `Nome utente`
- `Genere`

Il nome viene riutilizzato anche in altre parti dell'app, per esempio nel messaggio di benvenuto della `Home`.

### Lingua interfaccia

Puoi decidere se:

- seguire la lingua del sistema
- forzare una lingua specifica dell'app

### Conferme globali

L'opzione `Chiedi conferma per le eliminazioni` aggiunge una conferma prima delle azioni distruttive, come rimozioni ed eliminazioni.

### Metadati

In `Generali` trovi anche:

- `Mostra metadati nell'app`

Questa opzione decide se visualizzare o meno i pannelli metadati nelle schermate che li prevedono.

### Disposizione pannelli dashboard avventura

Questa parte è importante se usi spesso la `Dashboard Avventura`.

Puoi:

- trascinare i pannelli
- riordinarli nella colonna sinistra o destra
- spostarli da una colonna all'altra

### Tema attivo

In `Generali` viene anche mostrato il **tema attualmente selezionato** come riepilogo rapido. Il cambio vero e proprio del tema si fa nella sezione `Tema`.

### Guide introduttive

Da qui puoi ripristinare il comportamento di primo utilizzo dell'app.

Il pulsante `Ripristina Primo Utilizzo` fa in modo che DnDino consideri di nuovo come non ancora viste le guide contestuali e i percorsi introduttivi.

## Topbar

La sezione `Topbar` definisce il comportamento degli strumenti rapidi presenti nella barra superiore dell'app. Per la descrizione completa di ogni pulsante, vedi la pagina `Topbar`.

### Aspetto topbar

Puoi scegliere se visualizzare la topbar:

- con sole icone
- oppure con icone e nome sotto

### Dado predefinito

Qui puoi scegliere il **tipo di dado predefinito** proposto dal lanciadadi dentro `Strumenti rapidi`.

### Apertura rapida personaggi

Questa impostazione controlla il comportamento dell'apertura rapida dei personaggi.

Puoi decidere se l'apertura veloce deve portare:

- a una visualizzazione più orientata alla lettura
- oppure a una modalità più vicina alla modifica

### Apertura rapida regole

Questa impostazione controlla l'apertura veloce delle `Regole`.

Da qui puoi decidere se la scorciatoia deve aprire:

- l'editor completo
- oppure una finestra più compatta e orientata alla consultazione

### Controlli finestra giocatori nella topbar

L'opzione `Mostra controlli finestra giocatori nella topbar` mostra i controlli rapidi per aprire o chiudere manualmente la `Finestra Giocatori`.

## Luoghi

La sezione `Luoghi` contiene le preferenze globali usate come comportamento di default nella dashboard dei luoghi.

### Ruolo presenza predefinito

Quando aggiungi una presenza a un luogo, DnDino può proporre un ruolo iniziale predefinito.

### Mostra mappe dei luoghi padre di default

Se attivi questa opzione, nella schermata `Luoghi` le mappe ereditate dai luoghi padre partono già visibili.

### Ricorda ultimo luogo visitato

Se attivo, quando rientri nella schermata `Luoghi` l'app prova a ripristinare l'ultimo luogo selezionato per quell'avventura.

### Chiudi automaticamente il luogo precedente

Questa impostazione si applica durante una **sessione live attiva**.

Quando un luogo viene segnato `In visita`, il luogo che era prima `In visita` viene marcato automaticamente come `Visitato`.

## Combattimento

La sezione `Combattimento` raccoglie le preferenze globali del sistema di combattimento.

Qui trovi le opzioni di presentazione e le preferenze che influenzano la `Finestra Giocatori`.

### Abilita schermata combattimento per i giocatori

Questa è l'opzione principale. Se è disattivata, DnDino non usa la finestra giocatori per mostrare intro, turno corrente, round o riepilogo finale del combattimento, e le opzioni collegate vengono nascoste.

### Apri la finestra giocatori se chiusa

Se attiva, quando parte il combattimento DnDino apre automaticamente la `Finestra Giocatori`. Se è disattivata, la presentazione viene aggiornata solo quando la finestra è già aperta.

### Apri la finestra giocatori anche con un solo monitor

Questa preferenza compare solo se l'apertura automatica è attiva. Serve quando vuoi usare la `Finestra Giocatori` anche senza un secondo schermo.

## Presentazione combattimento

Questa sottosezione controlla le informazioni generali mostrate ai giocatori durante lo scontro:

- `Mostra intro combattimento ai giocatori`
- `Mostra riepilogo finale ai giocatori`
- `Mostra round nella schermata giocatori`
- `Mostra durata scontro nella schermata giocatori`
- `Mostra prossimo turno nella schermata giocatori`

La durata dello scontro viene mostrata come timer leggibile; se il combattimento è in pausa, il conteggio si ferma.

## Informazioni eroi

Queste opzioni valgono quando il partecipante di turno è un eroe o un alleato. Anche un PNG o un mostro marcato come `Alleato` usa quindi queste impostazioni. Puoi decidere se mostrare:

- PF attuali, massimi e temporanei
- condizioni attive

## Informazioni PNG

Queste opzioni valgono solo quando il partecipante di turno è un PNG non alleato. I PNG marcati come `Alleato` ricadono nelle impostazioni degli eroi/alleati. Puoi decidere separatamente se mostrare:

- PF attuali, massimi e temporanei
- condizioni attive
- nome reale del PNG

Se il nome dei PNG è nascosto, nella `Finestra Giocatori` viene usato il nome generico `PNG`.

## Informazioni mostri

Queste opzioni valgono solo quando il partecipante di turno è un mostro non alleato. I mostri marcati come `Alleato` ricadono nelle impostazioni degli eroi/alleati. Puoi decidere separatamente se mostrare:

- PF attuali, massimi e temporanei
- condizioni attive
- nome reale dei nemici

Se il nome dei mostri/nemici è nascosto, nella `Finestra Giocatori` viene usato il nome generico `Nemico`.

## Media

La sezione `Media` raccoglie le preferenze per la gestione delle immagini e della finestra di presentazione.

### Immagini giocatori a tutto schermo

Se attivo, le immagini mostrate ai giocatori vengono aperte in modalità fullscreen.

### Immagini DM sul monitor principale

Questa opzione fa sì che la finestra del DM venga aperta di default sul primo schermo disponibile.

### Ricorda dimensione finestra DM

Se attivo, quando riapri una nuova immagine per il DM la finestra mantiene:

- ultima dimensione
- ultima posizione

## Manutenzione media

La sezione `Manutenzione media` serve per il lato più tecnico della gestione immagini.

Da qui puoi lanciare `Ripulisci media inutilizzati`, che controlla i file immagine salvati dall'app e rimuove quelli che non risultano più collegati ad alcuna entità.

## Tema

La sezione `Tema` permette di scegliere la **palette globale** dell'app.

Ogni tema mostra una piccola anteprima visiva con i colori principali, così puoi capire subito come cambierà l'aspetto generale dell'interfaccia.

## Database e Media

La sezione `Database e Media` è una delle più importanti per la sicurezza dei dati.

Qui trovi:

- dimensione del database
- numero di immagini salvate nell'app
- dimensione totale delle immagini salvate
- gestione degli snapshot
- esportazione dei backup
- esportazione dei media

Nella versione di rilascio DnDino non mostra i percorsi tecnici interni dell'app. Quei dati sono utili solo in debug e non servono nell'uso normale.

### Backup automatico

Puoi scegliere:

- la frequenza del backup automatico
- il numero massimo di snapshot automatici da mantenere

### Snapshot cloud

DnDino gestisce anche la modalità degli snapshot cloud.

Da qui puoi scegliere il comportamento relativo ai salvataggi cloud e vedere lo stato corrente tramite il testo di riepilogo mostrato nella schermata.

### Azioni principali

Nel pannello `Database` trovi i pulsanti più importanti di manutenzione:

- `Apri cartella dati`
- `Apri cartella backup`
- `Crea snapshot...`
- `Ripristina snapshot...`
- `Ripristina da iCloud`

### Reimpostazione applicazione

La funzione `Reimposta dati applicazione` cancella:

- database dell'app
- media dell'app

ma mantiene i backup già creati.

### Ultimi snapshot

Nella parte bassa della sezione `Database` viene mostrato anche l'elenco degli ultimi snapshot trovati.

Per ciascuno vengono mostrati:

- nome file
- data
- dimensione

### Esportazione snapshot e media

Gli snapshot e i media possono essere esportati in una posizione scelta dall'utente tramite i normali pannelli di salvataggio di macOS.

Questo è utile per:

- conservare una copia esterna dei backup
- archiviare tutte le immagini salvate dall'app
- spostare una copia dei dati su un supporto scelto dall'utente

I media usati dall'app restano comunque copiati nella sandbox dell'applicazione, così DnDino non perde i riferimenti se il file originale viene spostato o cancellato dal Mac.

## Diagnostica

La sezione `Diagnostica` è riservata alla versione di debug e non viene mostrata nella versione di rilascio.

## Supporto

La sezione `Supporto` raccoglie i canali rapidi per contattare chi sviluppa l'app.

Qui trovi:

- l'email di supporto
- il pulsante `Richiedi supporto`
- il pulsante `Invia un consiglio`
- il pulsante `Copia email`

## Licenze

La sezione `Licenze` raccoglie i riferimenti legali e di attribuzione usati dall'app.

Attualmente include in particolare la parte relativa al materiale del **System Reference Document 5.2** di Dungeons & Dragons, con i relativi riferimenti:

- al documento SRD
- alla licenza `CC-BY-4.0`

!!! tip
    Se stai configurando DnDino per la prima volta, le sezioni più utili da controllare subito sono `Generali`, `Topbar`, `Combattimento` e `Database`. In genere sono quelle che incidono di più sull'uso quotidiano e sulla sicurezza dei dati.
