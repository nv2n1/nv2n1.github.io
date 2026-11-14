---
title: "ggzmod_h(3)"
name: "ggzmod_h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-ggzmod_h/"
description: "ggzmod.h – Common functions for interfacing a game server and GGZ."
---

<h2 class="name">NAME</h2>
<p> ggzmod.h &#8211; Common functions for interfacing a game server and GGZ. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ggz.h&gt;<br />
 #include &lt;ggz_common.h&gt; </p>
<h3>Defines</h3>
<p> #define <code>GGZMOD_VERSION_MAJOR</code> 0 </p>
<p> #define <code>GGZMOD_VERSION_MINOR</code> 0 </p>
<p> #define <code>GGZMOD_VERSION_MICRO</code> 11 </p>
<p> #define <code>GGZMOD_VERSION_IFACE</code> &#8216;3:1:1&#8217; </p>
<h3>Typedefs</h3>
<p> typedef <code>GGZMod</code> <code>GGZMod</code><br />
 <i>A GGZmod object, used for tracking a ggz&lt;-&gt;table connection. </i><br />
 typedef void(* <code>GGZModHandler</code> )(<code>GGZMod</code> *mod, <code>GGZModEvent</code> e, const void *data)<br />
 <i>Event handler prototype. </i></p>
<h3>Enumerations</h3>
<p> enum <code>GGZModState</code> { <code>GGZMOD_STATE_CREATED</code>, <code>GGZMOD_STATE_CONNECTED</code>, <code>GGZMOD_STATE_WAITING</code>, <code>GGZMOD_STATE_PLAYING</code>, <code>GGZMOD_STATE_DONE</code> }<br />
 <i>Table states. </i><br />
 enum <code>GGZModEvent</code> { <code>GGZMOD_EVENT_STATE</code>, <code>GGZMOD_EVENT_SERVER</code>, <code>GGZMOD_EVENT_PLAYER</code>, <code>GGZMOD_EVENT_SEAT</code>, <code>GGZMOD_EVENT_SPECTATOR_SEAT</code>, <code>GGZMOD_EVENT_CHAT</code>, <code>GGZMOD_EVENT_STATS</code>, <code>GGZMOD_EVENT_ERROR</code> }<br />
 <i>Callback events. </i><br />
 enum <code>GGZModType</code> { <code>GGZMOD_GGZ</code>, <code>GGZMOD_GAME</code> }<br />
 <i>The &#8216;type&#8217; of ggzmod. </i></p>
<h3>Functions</h3>
<p> <code>GGZMod</code> * <code>ggzmod_new</code> (<code>GGZModType</code> type)<br />
 <i>Create a new ggzmod object. </i><br />
 void <code>ggzmod_free</code> (<code>GGZMod</code> *ggzmod)<br />
 <i>Destroy a finished ggzmod object. </i><br />
 int <code>ggzmod_get_fd</code> (<code>GGZMod</code> *ggzmod)<br />
 <i>Get the file descriptor for the GGZMod socket. </i><br />
 <code>GGZModType</code> <code>ggzmod_get_type</code> (<code>GGZMod</code> *ggzmod)<br />
 <i>Get the type of the ggzmod object. </i><br />
 <code>GGZModState</code> <code>ggzmod_get_state</code> (<code>GGZMod</code> *ggzmod)<br />
 <i>Get the current state of the table. </i><br />
 int <code>ggzmod_get_server_fd</code> (<code>GGZMod</code> *ggzmod)<br />
 <i>Get the fd of the game server connection. </i><br />
 int <code>ggzmod_get_num_seats</code> (<code>GGZMod</code> *ggzmod)<br />
 <i>Get the total number of seats at the table. </i><br />
 <code>GGZSeat</code> <code>ggzmod_get_seat</code> (<code>GGZMod</code> *ggzmod, int seat)<br />
 <i>Get all data for the specified seat. </i><br />
 int <code>ggzmod_get_num_spectator_seats</code> (<code>GGZMod</code> *ggzmod)<br />
 <i>Get the maximum number of spectators. This function returns the maximum number of spectator seats available. A game can use this to iterate over the spectator seats to look for spectators occupying them. Since spectators may come and go at any point and there is no limit on the number of spectators, you should consider this value to be dynamic and call this function again each time you&#8217;re looking for spectators. </i><br />
 <code>GGZSpectatorSeat</code> <code>ggzmod_get_spectator_seat</code> (<code>GGZMod</code> *ggzmod, int seat)<br />
 <i>Get a spectator&#8217;s data. </i><br />
 const char * <code>ggzmod_get_player</code> (<code>GGZMod</code> *ggzmod, int *is_spectator, int *seat_num)<br />
 <i>Get data about this player. </i><br />
 void * <code>ggzmod_get_gamedata</code> (<code>GGZMod</code> *ggzmod)<br />
 <i>Return gamedata pointer. </i><br />
 void <code>ggzmod_set_gamedata</code> (<code>GGZMod</code> *ggzmod, void *data)<br />
 <i>Set gamedata pointer. </i><br />
 void <code>ggzmod_set_handler</code> (<code>GGZMod</code> *ggzmod, <code>GGZModEvent</code> e, <code>GGZModHandler</code> func)<br />
 <i>Set a handler for the given event. </i><br />
 int <code>ggzmod_dispatch</code> (<code>GGZMod</code> *ggzmod)<br />
 <i>Check for and handle input. </i><br />
 int <code>ggzmod_set_state</code> (<code>GGZMod</code> *ggzmod, <code>GGZModState</code> state)<br />
 <i>Change the table&#8217;s state. </i><br />
 int <code>ggzmod_connect</code> (<code>GGZMod</code> *ggzmod)<br />
 <i>Connect to ggz. </i><br />
 int <code>ggzmod_disconnect</code> (<code>GGZMod</code> *ggzmod)<br />
 <i>Disconnect from ggz. </i><br />
 void <code>ggzmod_request_stand</code> (<code>GGZMod</code> *ggzmod)<br />
 <i>Stand up (move from your seat into a spectator seat). </i><br />
 void <code>ggzmod_request_sit</code> (<code>GGZMod</code> *ggzmod, int seat_num)<br />
 <i>Sit down (move from a spectator seat into a player seat). </i><br />
 void <code>ggzmod_request_boot</code> (<code>GGZMod</code> *ggzmod, const char *name)<br />
 <i>Boot a player. Only the game host may do this. </i><br />
 void <code>ggzmod_request_bot</code> (<code>GGZMod</code> *ggzmod, int seat_num)<br />
 <i>Change the requested seat from an opean seat to a bot. </i><br />
 void <code>ggzmod_request_open</code> (<code>GGZMod</code> *ggzmod, int seat_num)<br />
 <i>Change the requested seat from a bot to an open seat. </i><br />
 void <code>ggzmod_request_chat</code> (<code>GGZMod</code> *ggzmod, const char *chat_msg)<br />
 <i>Chat! This initiates a table chat. </i><br />
 int <code>ggzmod_player_get_record</code> (<code>GGZMod</code> *ggzmod, <code>GGZSeat</code> *seat, int *wins, int *losses, int *ties, int *forfeits)<br />
 <i>Get the player&#8217;s win-loss record. </i><br />
 int <code>ggzmod_player_get_rating</code> (<code>GGZMod</code> *ggzmod, <code>GGZSeat</code> *seat, int *rating)<br />
 <i>Get the player&#8217;s rating. </i><br />
 int <code>ggzmod_player_get_ranking</code> (<code>GGZMod</code> *ggzmod, <code>GGZSeat</code> *seat, int *ranking)<br />
 <i>Get the player&#8217;s ranking. </i><br />
 int <code>ggzmod_player_get_highscore</code> (<code>GGZMod</code> *ggzmod, <code>GGZSeat</code> *seat, int *highscore)<br />
 <i>Get the player&#8217;s highscore. </i><br />
 int <code>ggzmod_spectator_get_record</code> (<code>GGZMod</code> *ggzmod, <code>GGZSpectatorSeat</code> *seat, int *wins, int *losses, int *ties, int *forfeits)<br />
 <i>Get the spectator&#8217;s win-loss record. </i><br />
 int <code>ggzmod_spectator_get_rating</code> (<code>GGZMod</code> *ggzmod, <code>GGZSpectatorSeat</code> *seat, int *rating)<br />
 <i>Get the spectator&#8217;s rating. </i><br />
 int <code>ggzmod_spectator_get_ranking</code> (<code>GGZMod</code> *ggzmod, <code>GGZSpectatorSeat</code> *seat, int *ranking)<br />
 <i>Get the spectator&#8217;s ranking. </i><br />
 int <code>ggzmod_spectator_get_highscore</code> (<code>GGZMod</code> *ggzmod, <code>GGZSpectatorSeat</code> *seat, int *highscore)<br />
 <i>Get the spectator&#8217;s highscore. </i></p>
<h2>Detailed Description</h2>
<p> Common functions for interfacing a game server and GGZ. </p>
<p> This file contains all libggzmod functions used by game servers to interface with GGZ (and vice versa). Just include <code>ggzmod.h</code> and make sure your program is linked with libggzmod. Then use the functions below as appropriate. </p>
<p> GGZmod currently provides an event-driven interface. Data from communication sockets is read in by the library, and a handler function (registered as a callback) is invoked to handle any events. The calling program should not read/write data from/to the GGZ socket unless it really knows what it is doing. </p>
<p> That this does not apply to the client sockets: ggzmod provides one file desriptor for communicating (TCP) to each client. If data is ready to be read by one of these file descriptors ggzmod may invoke the appropriate handler (see below), but will never actually read any data. </p>
<p> For more information, see the documentation at <a rel="nofollow" href="http://ggz.sf.net/.">http://ggz.sf.net/.</a></p>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>GGZMod</code> <code>GGZMod</code></h3>
<p> A GGZmod object, used for tracking a ggz&lt;-&gt;table connection. </p>
<p> A game client should track a pointer to a GGZMod object; it contains all the state information for communicating with GGZ. The GGZ client will track one such object for every game table that is running.</p>
<h3>typedef void(* <code>GGZModHandler</code>)(<code>GGZMod</code> *mod, <code>GGZModEvent</code> e, const void *data)</h3>
<p> Event handler prototype. </p>
<p> A function of this type will be called to handle a ggzmod event. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>mod</i> The ggzmod state object.<br />
 <i>e</i> The event that has occured.<br />
 <i>data</i> Pointer to additional data for the event. The additional data will be of the following form:</p>
<dl>
<dt>&bull;</p>
<dd> GGZMOD_EVENT_STATE: The old state (GGZModState*)</p>
<dt>&bull;</p>
<dd> GGZMOD_EVENT_SERVER: The fd of the server connection (int*)</p>
<dt>&bull;</p>
<dd> GGZMOD_EVENT_PLAYER: The old player data (int[2])</p>
<dt>&bull;</p>
<dd> GGZMOD_EVENT_SEAT: The old seat (GGZSeat*)</p>
<dt>&bull;</p>
<dd> GGZMOD_EVENT_SPECTATOR_SEAT: The old seat (GGZSpectatorSeat*)</p>
<dt>&bull;</p>
<dd> GGZMOD_EVENT_ERROR: An error string (char*)</dl>
</dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>GGZModEvent</code></h3>
<p> Callback events. </p>
<p> Each of these is a possible GGZmod event. For each event, the table may register a handler with GGZmod to handle that event. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>GGZModHandler</code> </p>
<p> <code>ggzmod_set_handler</code></dl>
<p> <code>Enumeration values: </code></p>
<dl>
<dt><i>GGZMOD_EVENT_STATE </i></p>
<dd> Module status changed This event occurs when the game&#8217;s status changes. The old state (a GGZModState*) is passed as the event&#8217;s data.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>GGZModState</code></dl>
<dl>
<dt><i>GGZMOD_EVENT_SERVER </i></p>
<dd> A new server connection has been made This event occurs when a new connection to the game server has been made. The fd is passed as the event&#8217;s data.</p>
<dt><i>GGZMOD_EVENT_PLAYER </i></p>
<dd> The player&#8217;s seat status has changed.</dl>
<p> This event occurs when the player&#8217;s seat status changes; i.e. he changes seats or starts/stops spectating. The event data is a int[2] pair consisting of the old {is_spectator, seat_num}.</p>
<dl>
<dt><i>GGZMOD_EVENT_SEAT </i></p>
<dd> A seat change.</dl>
<p> This event occurs when a seat change occurs. The old seat (a GGZSeat*) is passed as the event&#8217;s data. The seat information will be updated before the event is invoked.</p>
<dl>
<dt><i>GGZMOD_EVENT_SPECTATOR_SEAT </i></p>
<dd> A spectator seat change.</dl>
<p> This event occurs when a spectator seat change occurs. The old spectator (a GGZSpectator*) is passed as the event&#8217;s data. The spectator information will be updated before the event is invoked.</p>
<dl>
<dt><i>GGZMOD_EVENT_CHAT </i></p>
<dd> A chat message event.</dl>
<p> This event occurs when we receive a chat. The chat may have originated in another game client or from the GGZ client; in either case it will be routed to us. The chat information (a GGZChat*) is passed as the event&#8217;s data. Note that the chat may originate with a player or a spectator, and they may have changed seats or left the table by the time it gets to us.</p>
<dl>
<dt><i>GGZMOD_EVENT_STATS </i></p>
<dd> A player&#8217;s stats have been updated.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzmod_player_get_record</code> </p>
<p> <code>ggzmod_player_get_rating</code> </p>
<p> <code>ggzmod_player_get_ranking</code> </p>
<p> <code>ggzmod_player_get_highscore</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The name of the player whose stats have changed.</dl>
<dl>
<dt><i>GGZMOD_EVENT_ERROR </i></p>
<dd> An error has occurred This event occurs when a GGZMod error has occurred. An error message (a char*) will be passed as the event&#8217;s data. GGZMod may attempt to recover from the error, but it is not guaranteed that the GGZ connection will continue to work after an error has happened.</dl>
<h3>enum <code>GGZModState</code></h3>
<p> Table states. </p>
<p> Each table has a current &#8216;state&#8217; that is tracked by ggzmod. First the table is executed and begins running. Then it receives a launch event from GGZ and begins waiting for players. At some point a game will be started and played at the table, after which it may return to waiting. Eventually the table will probably halt and then the program will exit. </p>
<p> More specifically, the game is in the CREATED state when it is first executed. It moves to the CONNECTED state after GGZ first communicates with it, and to WAITING after the connection is established with the game server. After this, the game server may use ggzmod_set_state to change between WAITING, PLAYING, and DONE states. A WAITING game is considered waiting for players (or whatever), while a PLAYING game is actively being played (this information may be, but currently is not, propogated back to GGZ for display purposes). Once the state is changed to DONE, the table is considered dead and will exit shortly thereafter (ggzmod_loop will stop looping, etc.) (see the kill_on_exit game option). </p>
<p> Each time the game state changes, a GGZMOD_EVENT_STATE event will be propogated to the game server. </p>
<p> <code>Enumeration values: </code></p>
<dl>
<dt><i>GGZMOD_STATE_CREATED </i></p>
<dd> Initial state. The game starts out in this state. Once the state is changed it should never be changed back.</p>
<dt><i>GGZMOD_STATE_CONNECTED </i></p>
<dd> Connected state. After the GGZ client and game client get connected, the game changes into this state automatically. Once this happens messages may be sent between these two. Once the game leaves this state it should never be changed back.</p>
<dt><i>GGZMOD_STATE_WAITING </i></p>
<dd> Waiting state. After the game client and game server are connected, the client enters the waiting state. The game client may now call ggzmod_set_state to change between WAITING, PLAYING, and DONE states.</p>
<dt><i>GGZMOD_STATE_PLAYING </i></p>
<dd> Playing state. This state is only entered after the game client changes state to it via ggzmod_set_state. State may be changed back and forth between WAITING and PLAYING as many times as are wanted.</p>
<dt><i>GGZMOD_STATE_DONE </i></p>
<dd> Done state. Once the game client is done running, ggzmod_set_state should be called to set the state to done. At this point nothing &#8216;new&#8217; can happen. The state cannot be changed again after this. However the game client will not be terminated by the GGZ client; GGZ just waits for it to exit of its own volition.</dl>
<h3>enum <code>GGZModType</code></h3>
<p> The &#8216;type&#8217; of ggzmod. </p>
<p> The &#8216;flavor&#8217; of GGZmod object this is. Affects what operations are allowed. </p>
<p> <code>Enumeration values: </code></p>
<dl>
<dt><i>GGZMOD_GGZ </i></p>
<dd> Used by the ggz client (&#8216;ggz&#8217;).</p>
<dt><i>GGZMOD_GAME </i></p>
<dd> Used by the game client (&#8216;table&#8217;).</dl>
<h2>Function Documentation</h2>
<h3>int ggzmod_connect (<code>GGZMod</code> * ggzmod)</h3>
<p> Connect to ggz. </p>
<p> Call this function to make an initial GGZ &lt;-&gt; game connection.</p>
<dl>
<dt>&bull;</p>
<dd> When called by the game server, this function makes the physical connection to ggz.</p>
<dt>&bull;</p>
<dd> When called by ggz, it will launch a table and connect to it.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The ggzmod object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, -1 on failure.</dl>
<h3>int ggzmod_disconnect (<code>GGZMod</code> * ggzmod)</h3>
<p> Disconnect from ggz. </p>
<dl>
<dt>&bull;</p>
<dd> When called by the game server, this function stops the connection to GGZ. It should only be called when the table is ready to exit.</p>
<dt> &bull;</p>
<dd> When called by the GGZ server, this function will kill and clean up after the table.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The ggzmod object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, -1 on failure.</dl>
<h3>int ggzmod_dispatch (<code>GGZMod</code> * ggzmod)</h3>
<p> Check for and handle input. </p>
<p> This function handles input from the communications sockets:</p>
<dl>
<dt>&bull;</p>
<dd> It will check for input, but will not block.</p>
<dt>&bull;</p>
<dd> It will monitor input from the GGZmod socket.</p>
<dt>&bull;</p>
<dd> It will monitor input from player sockets only if a handler is registered for the PLAYER_DATA event.</p>
<dt>&bull;</p>
<dd> It will call an event handler as necessary.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The ggzmod object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 on error, the number of events handled (0-1) on success.</dl>
<h3>void ggzmod_free (<code>GGZMod</code> * ggzmod)</h3>
<p> Destroy a finished ggzmod object. </p>
<p> After the connection is through, the object may be freed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The GGZMod object.</dl>
<h3>int ggzmod_get_fd (<code>GGZMod</code> * ggzmod)</h3>
<p> Get the file descriptor for the GGZMod socket. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The GGZMod object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GGZMod&#8217;s main ggz &lt;-&gt; table socket FD.</dl>
<h3>void* ggzmod_get_gamedata (<code>GGZMod</code> * ggzmod)</h3>
<p> Return gamedata pointer. </p>
<p> Each GGZMod object can be given a &#8216;gamedata&#8217; pointer that is returned by this function. This is useful for when a single process serves multiple GGZmod&#8217;s. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The GGZMod object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A pointer to the gamedata block (or NULL if none).</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzmod_set_gamedata</code></dl>
<h3>int ggzmod_get_num_seats (<code>GGZMod</code> * ggzmod)</h3>
<p> Get the total number of seats at the table. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The number of seats, or -1 on error.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> If no connection is present, -1 will be returned. </p>
<p> While in GGZMOD_STATE_CREATED, we don&#8217;t know the number of seats.</dl>
<h3>int ggzmod_get_num_spectator_seats (<code>GGZMod</code> * ggzmod)</h3>
<p> Get the maximum number of spectators. This function returns the maximum number of spectator seats available. A game can use this to iterate over the spectator seats to look for spectators occupying them. Since spectators may come and go at any point and there is no limit on the number of spectators, you should consider this value to be dynamic and call this function again each time you&#8217;re looking for spectators. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The number of available spectator seats, or -1 on error.</dl>
<h3>const char* ggzmod_get_player (<code>GGZMod</code> * ggzmod, int * is_spectator, int * seat_num)</h3>
<p> Get data about this player. </p>
<p> Call this function to find out where at the table this player is sitting. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The GGZMod object.<br />
 <i>is_spectator</i> Will be set to TRUE iff player is spectating.<br />
 <i>seat_num</i> Will be set to the number of our (spectator) seat.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The name of the player (or NULL on error).</dl>
<h3><code>GGZSeat</code> ggzmod_get_seat (<code>GGZMod</code> * ggzmod, int seat)</h3>
<p> Get all data for the specified seat. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The GGZMod object.<br />
 <i>seat</i> The seat number (0..(number of seats &#8211; 1)).</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A valid <code>GGZSeat</code> structure, if seat is a valid seat.</dl>
<h3>int ggzmod_get_server_fd (<code>GGZMod</code> * ggzmod)</h3>
<p> Get the fd of the game server connection. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The GGZMod object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The server connection fd</dl>
<h3><code>GGZSpectatorSeat</code> ggzmod_get_spectator_seat (<code>GGZMod</code> * ggzmod, int seat)</h3>
<p> Get a spectator&#8217;s data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The GGZMod object.<br />
 <i>seat</i> The number, between 0 and (number of spectators &#8211; 1).</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A valid GGZSpectator structure, if given a valid seat.</dl>
<h3><code>GGZModState</code> ggzmod_get_state (<code>GGZMod</code> * ggzmod)</h3>
<p> Get the current state of the table. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The GGZMod object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The state of the table.</dl>
<h3><code>GGZModType</code> ggzmod_get_type (<code>GGZMod</code> * ggzmod)</h3>
<p> Get the type of the ggzmod object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The GGZMod object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The type of the GGZMod object (GGZ or GAME).</dl>
<h3><code>GGZMod</code>* ggzmod_new (<code>GGZModType</code> type)</h3>
<p> Create a new ggzmod object. </p>
<p> Before connecting through ggzmod, a new ggzmod object is needed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>type</i> The type of ggzmod. Should be GGZMOD_GAME for game servers.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>GGZModType</code></dl>
<h3>int ggzmod_player_get_highscore (<code>GGZMod</code> * ggzmod, <code>GGZSeat</code> * seat, int * highscore)</h3>
<p> Get the player&#8217;s highscore. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE if there is a highscore; FALSE if not or on error.</dl>
<h3>int ggzmod_player_get_ranking (<code>GGZMod</code> * ggzmod, <code>GGZSeat</code> * seat, int * ranking)</h3>
<p> Get the player&#8217;s ranking. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE if there is a ranking; FALSE if not or on error.</dl>
<h3>int ggzmod_player_get_rating (<code>GGZMod</code> * ggzmod, <code>GGZSeat</code> * seat, int * rating)</h3>
<p> Get the player&#8217;s rating. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE if there is a rating; FALSE if not or on error.</dl>
<h3>int ggzmod_player_get_record (<code>GGZMod</code> * ggzmod, <code>GGZSeat</code> * seat, int * wins, int * losses, int * ties, int * forfeits)</h3>
<p> Get the player&#8217;s win-loss record. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE if there is a record; FALSE if not or on error.</dl>
<h3>void ggzmod_request_boot (<code>GGZMod</code> * ggzmod, const char * name)</h3>
<p> Boot a player. Only the game host may do this. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The ggzmod object.<br />
 <i>name</i> The name of the player to boot.</dl>
<h3>void ggzmod_request_bot (<code>GGZMod</code> * ggzmod, int seat_num)</h3>
<p> Change the requested seat from an opean seat to a bot. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The ggzmod object.<br />
 <i>seat_num</i> The number of the seat to toggle.</dl>
<h3>void ggzmod_request_chat (<code>GGZMod</code> * ggzmod, const char * chat_msg)</h3>
<p> Chat! This initiates a table chat. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The ggzmod object.<br />
 <i>chat_msg</i> The chat message.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The chat message should be in UTF-8.</dl>
<h3>void ggzmod_request_open (<code>GGZMod</code> * ggzmod, int seat_num)</h3>
<p> Change the requested seat from a bot to an open seat. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The ggzmod object.<br />
 <i>seat_num</i> The number of the seat to toggle.</dl>
<h3>void ggzmod_request_sit (<code>GGZMod</code> * ggzmod, int seat_num)</h3>
<p> Sit down (move from a spectator seat into a player seat). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The ggzmod object.<br />
 <i>seat_num</i> The seat to sit in.</dl>
<h3>void ggzmod_request_stand (<code>GGZMod</code> * ggzmod)</h3>
<p> Stand up (move from your seat into a spectator seat). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The ggzmod object.</dl>
<h3>void ggzmod_set_gamedata (<code>GGZMod</code> * ggzmod, void * data)</h3>
<p> Set gamedata pointer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The GGZMod object.<br />
 <i>data</i> The gamedata block (or NULL for none).</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzmod_get_gamedata</code></dl>
<h3>void ggzmod_set_handler (<code>GGZMod</code> * ggzmod, <code>GGZModEvent</code> e, <code>GGZModHandler</code> func)</h3>
<p> Set a handler for the given event. </p>
<p> As described above, GGZmod uses an event-driven structure. Each time an event is called, the event handler (there can be only one) for that event will be called. This function registers such an event handler. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The GGZmod object.<br />
 <i>e</i> The GGZmod event.<br />
 <i>func</i> The handler function being registered.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzmod_get_gamedata</code></dl>
<h3>int ggzmod_set_state (<code>GGZMod</code> * ggzmod, <code>GGZModState</code> state)</h3>
<p> Change the table&#8217;s state. </p>
<p> This function should be called to change the state of a table. A game can use this function to change state between WAITING and PLAYING, or to set it to DONE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ggzmod</i> The ggzmod object.<br />
 <i>state</i> The new state.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, -1 on failure/error.</dl>
<h3>int ggzmod_spectator_get_highscore (<code>GGZMod</code> * ggzmod, <code>GGZSpectatorSeat</code> * seat, int * highscore)</h3>
<p> Get the spectator&#8217;s highscore. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE if there is a highscore; FALSE if not or on error.</dl>
<h3>int ggzmod_spectator_get_ranking (<code>GGZMod</code> * ggzmod, <code>GGZSpectatorSeat</code> * seat, int * ranking)</h3>
<p> Get the spectator&#8217;s ranking. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE if there is a ranking; FALSE if not or on error.</dl>
<h3>int ggzmod_spectator_get_rating (<code>GGZMod</code> * ggzmod, <code>GGZSpectatorSeat</code> * seat, int * rating)</h3>
<p> Get the spectator&#8217;s rating. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE if there is a rating; FALSE if not or on error.</dl>
<h3>int ggzmod_spectator_get_record (<code>GGZMod</code> * ggzmod, <code>GGZSpectatorSeat</code> * seat, int * wins, int * losses, int * ties, int * forfeits)</h3>
<p> Get the spectator&#8217;s win-loss record. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE if there is a record; FALSE if not or on error.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for GGZMod from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAL">Enumeration Type Documentation</a></p>
<dd>
<dt><a href="#lbAP">Function Documentation</a></p>
<dd>
<dt><a href="#lbBW">Author</a></p>
<dd></dl>
