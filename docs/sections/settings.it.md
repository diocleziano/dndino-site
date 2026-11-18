# Impostazioni

La sezione **Impostazioni** raccoglie le preferenze globali di DnDino. Qui non si lavora su una singola avventura o su un singolo personaggio, ma si definisce **come deve comportarsi l'app nel suo insieme**.

Le impostazioni influenzano soprattutto:

- l'aspetto generale dell'interfaccia
- il comportamento della topbar
- il flusso di `Luoghi`
- il comportamento del `Combattimento`
- la gestione di immagini, backup e snapshot
- il supporto e la diagnostica del database

## Contenuti, aiuti e nuovi temi

**Generali → Contenuto ufficiale** attiva o nasconde i cataloghi SRD, senza eliminare i dati personali o interrompere i riferimenti esistenti. Il controllo è condiviso con le liste. Vedi [Contenuti ufficiali](official-content.md).

I pulsanti guida **?** si possono disabilitare globalmente e sono attivi di default. Il tema **Halloween** si aggiunge alle altre palette; **Sistema** continua a seguire l'aspetto effettivo di macOS. Topbar, pulsanti contestuali e menu sono stati uniformati per mantenere leggibili icone e testo.

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

### Mantieni lo schermo acceso

In **Impostazioni > Generali**, attiva **Mantieni lo schermo acceso** per evitare lo spegnimento automatico del display mentre DnDino è in primo piano. È utile durante una sessione quando stai consultando appunti o mostrando contenuti senza usare continuamente mouse e tastiera.

L’opzione è **disattivata di default**. Funziona anche a batteria, ma aumenta il consumo energetico. La scelta viene ricordata tra gli avvii: passando a un’altra app il vincolo viene rilasciato; tornando a DnDino viene ripristinato se l’opzione è ancora attiva. Puoi disattivarla in qualsiasi momento dallo stesso controllo.

Non richiede permessi speciali e non modifica le impostazioni di sicurezza di macOS. Non impedisce il blocco manuale, la sospensione richiesta dall’utente, la chiusura del coperchio o le protezioni del sistema; non garantisce di impedire salvaschermo o blocchi imposti da policy indipendenti.

Se macOS non riesce ad attivare la funzione, compare un avviso: disattiva e riattiva l’opzione per riprovare. Il ripristino completo delle impostazioni la riporta su disattivato.

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

Le guide si gestiscono in [Reset app e guide](#app-and-guide-reset): riaprire l'introduzione e ripristinare le guide contestuali sono due comandi distinti, senza cancellazione dei dati.

## Topbar

La sezione `Topbar` definisce il comportamento degli strumenti rapidi presenti nella barra superiore dell'app. Per la descrizione completa di ogni pulsante, vedi la pagina `Topbar`.

### Aspetto topbar

Puoi scegliere se visualizzare la topbar:

- con sole icone
- oppure con icone e nome sotto

### Dado predefinito

Qui puoi scegliere il **tipo di dado predefinito** proposto dal lanciadadi dentro `Strumenti rapidi`.

### Apertura rapida personaggi

Ogni risultato ha due pulsanti circolari a destra: **Visualizzazione** apre la scheda compatta, **Modifica** apre l'editor. La riga non apre più la scheda da sola e non esiste una preferenza globale per scegliere tra le due modalità. [Topbar](topbar.md).

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

Le preferenze di presentazione e visibilità definiscono i **valori iniziali dei nuovi combattimenti**. Per cambiarle in un singolo scontro usa [Gestione secondo schermo e Visibilità giocatori](combat.md#player-screen-options), anche con comandi massivi per gruppi. Le scelte già salvate negli altri combattimenti non vengono sovrascritte.

L'abilitazione della schermata giocatori e la politica di apertura delle finestre rimangono globali. Nei combattimenti preesistenti non conclusi i valori iniziali vengono memorizzati una sola volta alla prima apertura.

### Abilita schermata combattimento per i giocatori

Questi controlli compaiono solo se in **Impostazioni > Combattimento** è attiva **Abilita schermata combattimento per i giocatori**. Se la disattivi, i controlli vengono nascosti sia nella preparazione sia durante lo scontro; le scelte salvate restano conservate. Non è necessario che un secondo monitor sia già collegato o che la finestra giocatori sia già aperta.

### Apri la finestra giocatori se chiusa

Se attiva, quando parte il combattimento DnDino apre automaticamente la `Finestra Giocatori`. Se è disattivata, la presentazione viene aggiornata solo quando la finestra è già aperta.

### Apri la finestra giocatori anche con un solo monitor

Questa preferenza compare solo se l'apertura automatica è attiva. Serve quando vuoi usare la `Finestra Giocatori` anche senza un secondo schermo.

## Presentazione combattimento

Queste opzioni definiscono i valori iniziali della presentazione dei nuovi combattimenti; puoi modificarli nello scontro senza cambiare le impostazioni:

- `Mostra intro combattimento ai giocatori`
- `Mostra riepilogo finale ai giocatori`
- `Mostra round nella schermata giocatori`
- `Mostra durata scontro nella schermata giocatori`
- `Mostra prossimo turno nella schermata giocatori`

La durata dello scontro viene mostrata come timer leggibile; se il combattimento è in pausa, il conteggio si ferma.

## Informazioni eroi

Definiscono la visibilità iniziale per i partecipanti di tipo eroe nei nuovi combattimenti. Puoi decidere se mostrare:

- PF attuali, massimi e temporanei
- condizioni attive

## Informazioni PNG

Definiscono la visibilità iniziale dei PNG nei nuovi combattimenti, anche quando il loro ruolo è Alleato. Puoi decidere separatamente se mostrare:

- PF attuali, massimi e temporanei
- condizioni attive
- nome reale del PNG

Se il nome dei PNG è nascosto, nella `Finestra Giocatori` viene usato il nome generico `PNG`.

## Informazioni mostri

Definiscono la visibilità iniziale dei mostri nei nuovi combattimenti. I loro PF e condizioni seguono queste opzioni anche quando sono alleati; inizialmente i nomi dei mostri non nemici restano visibili. Puoi decidere separatamente se mostrare:

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

<!-- guide-coverage: MOD-042 MOD-043 MOD-049 MOD-051 MOD-060 MOD-061 MOD-062 MOD-070 MOD-071 MOD-073 MOD-077 MOD-078 MOD-079 MOD-080 MOD-086 MOD-088 MOD-145 MOD-146 MOD-147 MOD-148 MOD-163 MOD-164 MOD-168 MOD-170 -->

## Temi, sfondi e opacità

**Sistema** è la prima scelta e segue macOS. Gli altri temi sono raggruppati in **Palette di colori**, **Speciali** e **Stagioni**. Negli Speciali trovi anche **Inferno** e **Magia**; le quattro stagioni hanno paesaggi fantasy illustrati con avventurieri. Gli stessi temi e immagini sono disponibili su Hero.

Puoi disattivare lo sfondo decorativo o importare uno **sfondo personalizzato**. Viene conservata una sola immagine: una nuova sostituisce la precedente. Cambiare tema disattiva lo sfondo personale ma non lo elimina.

Il cursore di opacità aggiorna subito i pannelli predisposti, compresi titoli e ricerca dei luoghi, intestazione dell'avventura, card degli eroi e sessioni. Queste superfici conservano una tonalità più scura o un'opacità attenuata per la leggibilità; testo, immagini e controlli non diventano trasparenti. I pannelli non predisposti rimangono opachi. **Predefinito** ripristina le diverse opacità originali e la posizione corretta del cursore, non un valore comune del 50%.

Al cambio tema la schermata principale viene ricreata e torna a **Impostazioni → Tema**. Le finestre secondarie aperte e le loro bozze non salvate rimangono intatte; la barra inferiore segue il nuovo tema. I pulsanti principali e la selezione della sidebar usano i colori del tema, con testo adattato al contrasto. **Sistema** conserva il comportamento dei controlli di macOS.

Per autorizzazioni, storico dei dispositivi, avvio live automatico facoltativo e differenza tra scollegare, rimuovere l'associazione e dimenticare, consulta [Collegamento con Hero](hero-sync.md).

## Notifiche e suoni {#notification-settings}

In **Impostazioni → Dispositivi Hero**, puoi nascondere la cronologia nella barra inferiore senza disabilitare i banner. Un interruttore separato, attivo di default, abilita il suono per **nuovi messaggi e richieste di abbinamento**. Aggiornamenti Live, collegamenti/disconnessioni e avvisi di combattimento restano silenziosi. Vedi [Notifiche nella barra inferiore](topbar.md#notification-history).

## Reset app e guide {#app-and-guide-reset}

La sezione distingue operazioni diverse: leggi la spiegazione prima di confermare.

- **Apri guida introduttiva** riapre il percorso iniziale senza eliminare dati o azzerare le guide contestuali. La nuova introduzione della 2.0.0 compare anche per chi aveva già visto quella precedente.
- **Mostra di nuovo le guide contestuali** le rende nuovamente disponibili nelle relative schermate, senza azzerare l'introduzione. Le guide scorrono verso le aree fuori vista e aprono le sezioni richieste.
- **Reimposta dati applicazione**, presente anche in Database e Media, cancella archivio e media ma conserva profilo, preferenze, guide e backup locali/iCloud.
- **Elimina backup locali** cancella le copie manuali e automatiche gestite da DnDino, non i dati correnti né i file esportati altrove.
- **Elimina copia iCloud** rimuove solo lo snapshot dell'app, quando disponibile. Se il backup cloud rimane attivo, un salvataggio futuro può ricrearlo.
- **Ripristino completo**, separato in fondo e con doppia conferma, cancella dati, media, backup gestiti, sfondo personale, credenziali Hero, profilo, preferenze e guide, poi chiude l'app. I file esportati altrove restano intatti.

Chiudi sessione live e finestre secondarie prima delle operazioni sull'archivio. Se iCloud non è disponibile, il ripristino completo richiede di scegliere esplicitamente quello locale; se la cancellazione cloud richiesta fallisce, i dati locali non vengono cancellati. Non è un'operazione annullabile: esporta prima ciò che vuoi conservare.
