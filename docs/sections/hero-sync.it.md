# Collegamento con DnDino Hero: guida per il Master

Collega i personaggi dei giocatori alla tua avventura, ricevi le loro schede e gestisci i valori di gioco dal Mac. Il collegamento è locale: non richiede un server esterno.

Per le istruzioni sul telefono o tablet, consulta la [guida per chi usa Hero](../companion/dndino-sync.md).

!!! info "Disponibilità delle nuove funzioni"
    Questa pagina descrive anche il nuovo confronto dei dati al collegamento, preparato per il prossimo aggiornamento delle app. Per utilizzarlo servono versioni di **DnDino e DnDino Hero che lo supportano entrambe**. Nelle versioni precedenti alcune opzioni o il comportamento iniziale possono essere diversi.

## Prima di iniziare

- Apri l'avventura corretta in DnDino.
- Usa la stessa rete locale e consenti l'accesso alla rete locale quando richiesto. Tieni Wi-Fi e Bluetooth attivi e i dispositivi vicini.
- Chiedi al giocatore di selezionare la scheda corretta in Hero.
- La sincronizzazione live richiede **iOS/iPadOS 26 o successivo** su Hero. Sui sistemi precedenti è disponibile **solo l'invio manuale della scheda**, anche fuori dal combattimento.

**Collegato non significa sincronizzato:** una connessione può essere attiva con la sincronizzazione automatica disabilitata.

## Primo collegamento, passo passo

1. Nella dashboard avventura, nel pannello **Sessione Live**, premi **Avvia** nell'area **DnDino Hero**. Non occorre avviare una sessione di gioco per ricevere una scheda.
2. Il giocatore apre **Impostazioni → Collegamento DnDino**, preme **Cerca DnDino** e sceglie la tua avventura.
3. Autorizza il dispositivo quando richiesto. Controlla nome del dispositivo e personaggio prima di confermare.
4. Per una scheda non ancora associata scegli **Importa nuovo** oppure **Associa esistente**. La seconda opzione permette di aggiornare una scheda già presente: controlla la conferma di sostituzione per non sovrascrivere quella sbagliata.
5. Se vuoi gli aggiornamenti in diretta, abilita **Sincronizzazione automatica** per quel dispositivo. Il giocatore vede lo stato, ma non deve attivare un secondo interruttore.

Le associazioni non si basano soltanto sul nome. Dopo il collegamento, rinominare un personaggio non richiede di crearne un'altra copia.

## Chi decide quali dati conservare?

**La struttura della scheda proviene da Hero:** il giocatore gestisce livelli, caratteristiche, descrizioni, incantesimi e configurazione delle progressioni. Il Master controlla l'abilitazione live e i valori di gioco consentiti.

Con le nuove versioni, a ogni collegamento o riconnessione Hero invia una scheda aggiornata prima degli scambi live. Anche riattivare la sincronizzazione richiede l'allineamento. Se i valori coincidono, non compare alcun confronto.

Se ci sono differenze, si apre **Allineamento personaggio**:

- confronta PF attuali, massimi e temporanei, CA, ispirazione eroica, condizioni, residui delle risorse e slot utilizzati;
- per ogni differenza scegli **Conserva** nella colonna DnDino oppure Hero: **Hero è preselezionato**;
- **Tutto da DnDino** e **Tutto da Hero** applicano la scelta a tutte le differenze;
- premi **Conferma e allinea** e attendi l'esito.

Esempio: DnDino conserva 18 PF e Hero ne indica 24. Puoi conservare i 18 PF del Master ma scegliere le condizioni di Hero. Le condizioni si scelgono **come insieme completo**, non vengono sommate automaticamente.

I massimi e la configurazione delle risorse rimangono quelli della scheda Hero. Una combinazione incompatibile viene segnalata. Durante l'attesa gli aggiornamenti di quel dispositivo restano sospesi; gli altri giocatori continuano a lavorare. Se i dati cambiano nel frattempo, verifica il confronto aggiornato. **Riprova** richiede dati freschi; chiudere la finestra o scegliere **Interrompi collegamento** interrompe il collegamento.

La conferma dell'allineamento, da sola, **non attiva la sincronizzazione live**.

## Durante la partita

Con live attiva, i valori supportati si aggiornano tra le due app: PF attuali/massimi/temporanei, CA, ispirazione e condizioni. Nel combattimento viene considerato il partecipante collegato.

Nel dettaglio del PG trovi anche le progressioni e gli slot importati:

| Informazione | Utilizzo |
| --- | --- |
| Progressioni con consumo | **Residui/Totale**, con meno per consumare e più per ripristinare |
| Progressioni fisse del livello attuale | Riquadri consultabili, senza pulsanti di consumo |
| Slot incantesimi | Totali e utilizzati, distinti per origine quando presenti più fonti |

I contatori sono salvati anche su DnDino, non soltanto mostrati durante la connessione. Quando il collegamento live è operativo, i comandi supportati del Master vengono confermati da Hero. Se un valore cambia contemporaneamente, leggi l'esito e riprova dopo l'aggiornamento: non presumere che un clic non confermato sia stato applicato.

Un nuovo livello o una diversa configurazione richiedono l'aggiornamento della **scheda completa**, non il solo scambio dei contatori.

## Scheda completa, chat e barra inferiore

Il pulsante di **download della scheda**, a destra della chat, richiede al dispositivo collegato il personaggio già associato, senza chiedere al giocatore di inviarlo di nuovo. Non abilita automaticamente la live. Richiede Hero compatibile, collegato e autorizzato e non è disponibile durante un allineamento in attesa.

Nella barra inferiore l'area Hero raccoglie i collegamenti avvenuti durante l'apertura corrente di DnDino e resta visibile anche se un dispositivo perde la connessione. Da qui puoi controllare stato e identità, effettuare un **test collegamento**, aprire la **chat**, gestire la live o scollegare. Il test non importa dati. La chat privata richiede la live attiva; i messaggi non letti sono segnalati nella barra.

## Riconnessione, scollegamento e problemi comuni

Di default ogni nuova connessione richiede una nuova attivazione live sul Master. Nelle impostazioni puoi scegliere l'avvio automatico per dispositivi già autorizzati: anche in quel caso il nuovo allineamento resta necessario.

- **Il Mac non appare:** verifica avventura in ascolto, stessa rete, permessi Rete locale e app aperte.
- **Collegato ma senza aggiornamenti:** verifica autorizzazione, associazione, iOS/iPadOS 26+, allineamento concluso e interruttore live del Master.
- **Connessione persa:** mantieni Hero in primo piano durante il gioco; tornando nell'app può tentare la riconnessione. È disponibile anche **Ricollega**.
- **Scollega** interrompe il collegamento attuale; non equivale a cancellare la scheda importata.
- **Rimuovi associazione al personaggio** revoca autorizzazione e associazioni nell'avventura corrente; **Dimentica dispositivo** agisce su tutte le avventure. Le schede già importate non vengono eliminate.

!!! tip "Prima della sessione"
    Prova il collegamento e una piccola variazione di PF con ciascun giocatore. Controlla l'esito su entrambe le app prima di iniziare il combattimento.
