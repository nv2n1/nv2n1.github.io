---
title: "ggzcore_h(3)"
name: "ggzcore_h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-ggzcore_h/"
description: "ggzcore.h – The interface for the ggzcore library used by GGZ clients."
---

<h2 class="name">NAME</h2>
<p> ggzcore.h &#8211; The interface for the ggzcore library used by GGZ clients. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdarg.h&gt;<br />
 #include &lt;sys/types.h&gt;<br />
 #include &lt;ggz_common.h&gt; </p>
<h3>Defines</h3>
<p> #define <code>GGZCORE_VERSION_MAJOR</code> 0 </p>
<p> #define <code>GGZCORE_VERSION_MINOR</code> 0 </p>
<p> #define <code>GGZCORE_VERSION_MICRO</code> 11 </p>
<p> #define <code>GGZCORE_VERSION_IFACE</code> &#8216;7:0:0&#8217; </p>
<p> #define <code>GGZCORE_DBG_CONF</code> &#8216;GGZCORE:CONF&#8217;<br />
 <i>ggz_debug debugging type for configuration system. </i><br />
 #define <code>GGZCORE_DBG_GAME</code> &#8216;GGZCORE:GAME&#8217;<br />
 <i>ggz_debug debugging type for game communication. </i><br />
 #define <code>GGZCORE_DBG_HOOK</code> &#8216;GGZCORE:HOOK&#8217;<br />
 <i>ggz_debug debugging type for hook system. </i><br />
 #define <code>GGZCORE_DBG_MODULE</code> &#8216;GGZCORE:MODULE&#8217;<br />
 <i>ggz_debug debugging type for accessing modules. </i><br />
 #define <code>GGZCORE_DBG_NET</code> &#8216;GGZCORE:NET&#8217;<br />
 <i>ggz_debug debugging type for network interaction. </i><br />
 #define <code>GGZCORE_DBG_POLL</code> &#8216;GGZCORE:POLL&#8217;<br />
 <i>ggz_debug debugging type for debugging while polling. </i><br />
 #define <code>GGZCORE_DBG_ROOM</code> &#8216;GGZCORE:ROOM&#8217;<br />
 <i>ggz_debug debugging type for room events and data. </i><br />
 #define <code>GGZCORE_DBG_SERVER</code> &#8216;GGZCORE:SERVER&#8217;<br />
 <i>ggz_debug debugging type for server events and data. </i><br />
 #define <code>GGZCORE_DBG_STATE</code> &#8216;GGZCORE:STATE&#8217;<br />
 <i>ggz_debug debugging type for state changes. </i><br />
 #define <code>GGZCORE_DBG_TABLE</code> &#8216;GGZCORE:TABLE&#8217;<br />
 <i>ggz_debug debugging type for table data. </i><br />
 #define <code>GGZCORE_DBG_XML</code> &#8216;GGZCORE:XML&#8217;<br />
 <i>ggz_debug debugging type for XML processing. </i><br />
 #define <code>ggzcore_server_get_channel</code>(server) (-1)<br />
 <i>Deprecated function. Do not use. </i><br />
 #define <code>ggzcore_server_create_channel</code>(server) (void)0<br />
 <i>Deprecated function. Do not use. </i><br />
 #define <code>ggzcore_module_launch</code>(m) ((int)(-1)) </p>
<p> #define <code>ggzcore_game_set_server_fd</code>(game, fd) (void)0<br />
 <i>Deprecated function. Do not use. </i></p>
<h3>Typedefs</h3>
<p> typedef <code>_GGZOptions</code> <code>GGZOptions</code> </p>
<p> typedef <code>GGZHookReturn</code>(* <code>GGZHookFunc</code> )(unsigned int id, const void *event_data, const void *user_data) </p>
<p> typedef void(* <code>GGZDestroyFunc</code> )(void *data)<br />
 <i>GGZ object destroy function type. </i><br />
 typedef _GGZServer <code>GGZServer</code><br />
 <i>A server object containing all information about a connection. </i><br />
 typedef _GGZRoom <code>GGZRoom</code><br />
 <i>Contains information about a single room on a server. </i><br />
 typedef _GGZPlayer <code>GGZPlayer</code><br />
 <i>Contains information about a single player. </i><br />
 typedef _GGZTable <code>GGZTable</code><br />
 <i>Contains information about a single table. </i><br />
 typedef _GGZGameType <code>GGZGameType</code><br />
 <i>Contains information about a _game type_. </i><br />
 typedef _GGZModule <code>GGZModule</code><br />
 <i>Contains information about a single module. A game module, on the client, is an executable designed to play a game. Each game type may have many modules that play it. </i><br />
 typedef _GGZGame <code>GGZGame</code><br />
 <i>Contains information about a single game table. This contains information about a table we are present at or are about to launch. It is thus associated with both a GGZTable and a GGZModule. </i></p>
<h3>Enumerations</h3>
<p> enum <code>GGZOptionFlags</code> { <code>GGZ_OPT_PARSER</code> = 0x0001, <code>GGZ_OPT_MODULES</code> = 0x0002, <code>GGZ_OPT_THREADED_IO</code> = 0x0004, <code>GGZ_OPT_EMBEDDED</code> = 0x0008, <code>GGZ_OPT_RECONNECT</code> = 0x0010 } </p>
<p> enum <code>GGZHookReturn</code> { <code>GGZ_HOOK_OK</code>, <code>GGZ_HOOK_REMOVE</code>, <code>GGZ_HOOK_ERROR</code>, <code>GGZ_HOOK_CRISIS</code> } </p>
<p> enum <code>GGZLoginType</code> { <code>GGZ_LOGIN</code>, <code>GGZ_LOGIN_GUEST</code>, <code>GGZ_LOGIN_NEW</code> } </p>
<p> enum <code>GGZServerEvent</code> { <code>GGZ_CONNECTED</code>, <code>GGZ_CONNECT_FAIL</code>, <code>GGZ_NEGOTIATED</code>, <code>GGZ_NEGOTIATE_FAIL</code>, <code>GGZ_LOGGED_IN</code>, <code>GGZ_LOGIN_FAIL</code>, <code>GGZ_MOTD_LOADED</code>, <code>GGZ_ROOM_LIST</code>, <code>GGZ_TYPE_LIST</code>, <code>GGZ_SERVER_PLAYERS_CHANGED</code>, <code>GGZ_ENTERED</code>, <code>GGZ_ENTER_FAIL</code>, <code>GGZ_LOGOUT</code>, <code>GGZ_NET_ERROR</code>, <code>GGZ_PROTOCOL_ERROR</code>, <code>GGZ_CHAT_FAIL</code>, <code>GGZ_STATE_CHANGE</code>, <code>GGZ_CHANNEL_CONNECTED</code>, <code>GGZ_CHANNEL_READY</code>, <code>GGZ_CHANNEL_FAIL</code>, <code>GGZ_NUM_SERVER_EVENTS</code> } </p>
<p> enum <code>GGZRoomEvent</code> { <code>GGZ_PLAYER_LIST</code>, <code>GGZ_TABLE_LIST</code>, <code>GGZ_CHAT_EVENT</code>, <code>GGZ_ROOM_ENTER</code>, <code>GGZ_ROOM_LEAVE</code>, <code>GGZ_TABLE_UPDATE</code>, <code>GGZ_TABLE_LAUNCHED</code>, <code>GGZ_TABLE_LAUNCH_FAIL</code>, <code>GGZ_TABLE_JOINED</code>, <code>GGZ_TABLE_JOIN_FAIL</code>, <code>GGZ_TABLE_LEFT</code>, <code>GGZ_TABLE_LEAVE_FAIL</code>, <code>GGZ_PLAYER_LAG</code>, <code>GGZ_PLAYER_STATS</code>, <code>GGZ_PLAYER_COUNT</code> } </p>
<p> enum <code>GGZGameEvent</code> { <code>GGZ_GAME_LAUNCHED</code>, <code>GGZ_GAME_LAUNCH_FAIL</code>, <code>GGZ_GAME_NEGOTIATED</code>, <code>GGZ_GAME_NEGOTIATE_FAIL</code>, <code>GGZ_GAME_PLAYING</code> } </p>
<p> enum <code>GGZStateID</code> { <code>GGZ_STATE_OFFLINE</code>, <code>GGZ_STATE_CONNECTING</code>, <code>GGZ_STATE_RECONNECTING</code>, <code>GGZ_STATE_ONLINE</code>, <code>GGZ_STATE_LOGGING_IN</code>, <code>GGZ_STATE_LOGGED_IN</code>, <code>GGZ_STATE_ENTERING_ROOM</code>, <code>GGZ_STATE_IN_ROOM</code>, <code>GGZ_STATE_BETWEEN_ROOMS</code>, <code>GGZ_STATE_LAUNCHING_TABLE</code>, <code>GGZ_STATE_JOINING_TABLE</code>, <code>GGZ_STATE_AT_TABLE</code>, <code>GGZ_STATE_LEAVING_TABLE</code>, <code>GGZ_STATE_LOGGING_OUT</code> }<br />
 <i>The states a server connection may be in. </i><br />
 enum <code>GGZModuleEnvironment</code> { <code>GGZ_ENVIRONMENT_PASSIVE</code>, <code>GGZ_ENVIRONMENT_CONSOLE</code>, <code>GGZ_ENVIRONMENT_FRAMEBUFFER</code>, <code>GGZ_ENVIRONMENT_XWINDOW</code>, <code>GGZ_ENVIRONMENT_XFULLSCREEN</code> }<br />
 <i>The environment a game frontend expects. </i></p>
<h3>Functions</h3>
<p> int <code>ggzcore_init</code> (<code>GGZOptions</code> options) </p>
<p> void <code>ggzcore_reload</code> (void) </p>
<p> void <code>ggzcore_destroy</code> (void) </p>
<p> <code>GGZServer</code> * <code>ggzcore_server_new</code> (void)<br />
 <i>Create a new server object. </i><br />
 int <code>ggzcore_server_reset</code> (<code>GGZServer</code> *server)<br />
 <i>Reset the server object. </i><br />
 int <code>ggzcore_server_add_event_hook</code> (<code>GGZServer</code> *server, const <code>GGZServerEvent</code> event, const <code>GGZHookFunc</code> func)<br />
 <i>Register a callback handler for a server event. </i><br />
 int <code>ggzcore_server_add_event_hook_full</code> (<code>GGZServer</code> *server, const <code>GGZServerEvent</code> event, const <code>GGZHookFunc</code> func, const void *data)<br />
 <i>Register a callback handler for a server event. </i><br />
 int <code>ggzcore_server_remove_event_hook</code> (<code>GGZServer</code> *server, const <code>GGZServerEvent</code> event, const <code>GGZHookFunc</code> func)<br />
 <i>Remove a single hook function from an event&#8217;s hook list. </i><br />
 int <code>ggzcore_server_remove_event_hook_id</code> (<code>GGZServer</code> *server, const <code>GGZServerEvent</code> event, const unsigned int hook_id)<br />
 <i>Remove a hook function with given ID from the event&#8217;s hook list. </i><br />
 int <code>ggzcore_server_set_hostinfo</code> (<code>GGZServer</code> *server, const char *host, const unsigned int port, const unsigned int use_tls)<br />
 <i>Set host info for connecting to the server. </i><br />
 int <code>ggzcore_server_set_logininfo</code> (<code>GGZServer</code> *server, const <code>GGZLoginType</code> type, const char *handle, const char *password, const char *email)<br />
 <i>Set login info for logging in to the server. </i><br />
 int <code>ggzcore_server_log_session</code> (<code>GGZServer</code> *server, const char *filename)<br />
 <i>Initiate logging of ggzcore events. </i><br />
 const char * <code>ggzcore_server_get_host</code> (const <code>GGZServer</code> *server)<br />
 <i>Get the hostname of the server. </i><br />
 int <code>ggzcore_server_get_port</code> (const <code>GGZServer</code> *server)<br />
 <i>Get the port of the server. </i><br />
 <code>GGZLoginType</code> <code>ggzcore_server_get_type</code> (const <code>GGZServer</code> *server)<br />
 <i>Get the login type being used for this server. </i><br />
 const char * <code>ggzcore_server_get_handle</code> (const <code>GGZServer</code> *server)<br />
 <i>Get the handle being used for this server. </i><br />
 const char * <code>ggzcore_server_get_password</code> (const <code>GGZServer</code> *server)<br />
 <i>Get the password being used for this server. </i><br />
 int <code>ggzcore_server_get_fd</code> (const <code>GGZServer</code> *server)<br />
 <i>Get the socket used for connection with the server. </i><br />
 <code>GGZStateID</code> <code>ggzcore_server_get_state</code> (const <code>GGZServer</code> *server)<br />
 <i>Get the state of the server connection. </i><br />
 int <code>ggzcore_server_get_tls</code> (const <code>GGZServer</code> *server)<br />
 <i>Get the current TLS status of this server. </i><br />
 int <code>ggzcore_server_get_num_players</code> (const <code>GGZServer</code> *server)<br />
 <i>Get the total number of players on the server. </i><br />
 int <code>ggzcore_server_get_num_rooms</code> (const <code>GGZServer</code> *server)<br />
 <i>Return the number of rooms on the server, or -1 on error. </i><br />
 <code>GGZRoom</code> * <code>ggzcore_server_get_cur_room</code> (const <code>GGZServer</code> *server)<br />
 <i>Return the current room, or NULL if there is none. </i><br />
 <code>GGZRoom</code> * <code>ggzcore_server_get_nth_room</code> (const <code>GGZServer</code> *server, const unsigned int num)<br />
 <i>Return the nth room on the server, or NULL on error. </i><br />
 int <code>ggzcore_server_get_num_gametypes</code> (const <code>GGZServer</code> *server)<br />
 <i>Return the overall number of game types on the server. </i><br />
 <code>GGZGameType</code> * <code>ggzcore_server_get_nth_gametype</code> (const <code>GGZServer</code> *server, const unsigned int num)<br />
 <i>Get the nth gametype, or NULL on error. </i><br />
 <code>GGZGame</code> * <code>ggzcore_server_get_cur_game</code> (const <code>GGZServer</code> *server)<br />
 <i>Return the player&#8217;s current game. </i><br />
 int <code>ggzcore_server_is_online</code> (const <code>GGZServer</code> *server)<br />
 <i>Return TRUE iff the server is online (connected?). </i><br />
 int <code>ggzcore_server_is_logged_in</code> (const <code>GGZServer</code> *server)<br />
 <i>Return TRUE iff we are logged into the server. </i><br />
 int <code>ggzcore_server_is_in_room</code> (const <code>GGZServer</code> *server)<br />
 <i>Return TRUE iff we are in a room on the server. </i><br />
 int <code>ggzcore_server_is_at_table</code> (const <code>GGZServer</code> *server)<br />
 <i>Return TRUE iff we are at a table on the server. </i><br />
 int <code>ggzcore_server_connect</code> (<code>GGZServer</code> *server)<br />
 <i>Connect to the server. </i><br />
 int <code>ggzcore_server_login</code> (<code>GGZServer</code> *server)<br />
 <i>Log in to the server. </i><br />
 int <code>ggzcore_server_motd</code> (<code>GGZServer</code> *server)<br />
 <i>Request the MOTD from the server. </i><br />
 int <code>ggzcore_server_list_rooms</code> (<code>GGZServer</code> *server, const int type, const char verbose)<br />
 <i>Request room list. </i><br />
 int <code>ggzcore_server_list_gametypes</code> (<code>GGZServer</code> *server, const char verbose)<br />
 <i>Request game type list. </i><br />
 int <code>ggzcore_server_join_room</code> (<code>GGZServer</code> *server, const unsigned int room)<br />
 <i>Join a room on the server. </i><br />
 int <code>ggzcore_server_logout</code> (<code>GGZServer</code> *server)<br />
 <i>Log out of a server. </i><br />
 int <code>ggzcore_server_disconnect</code> (<code>GGZServer</code> *server)<br />
 <i>Disconnect from a server after having logged out. </i><br />
 int <code>ggzcore_server_data_is_pending</code> (<code>GGZServer</code> *server)<br />
 <i>Check for data pending from the server socket. </i><br />
 int <code>ggzcore_server_read_data</code> (<code>GGZServer</code> *server, int fd)<br />
 <i>Read data for the server on the specified FD. </i><br />
 void <code>ggzcore_server_free</code> (<code>GGZServer</code> *server)<br />
 <i>Free GGZServer object and accompanying data. </i><br />
 <code>GGZRoom</code> * <code>ggzcore_room_new</code> (void)<br />
 <i>Allocate space for a new room object. </i><br />
 int <code>ggzcore_room_init</code> (<code>GGZRoom</code> *room, <code>GGZServer</code> *server, const unsigned int id, const char *name, const unsigned int game, const char *desc)<br />
 <i>Initialize room object. </i><br />
 void <code>ggzcore_room_free</code> (<code>GGZRoom</code> *room)<br />
 <i>De-allocate room object and its children. </i><br />
 <code>GGZServer</code> * <code>ggzcore_room_get_server</code> (<code>GGZRoom</code> *room)<br />
 <i>Return the server for this room (or NULL on error). </i><br />
 int <code>ggzcore_room_get_id</code> (const <code>GGZRoom</code> *room)<br />
 <i>Return the ID number of the room (or negative on error). </i><br />
 char * <code>ggzcore_room_get_name</code> (<code>GGZRoom</code> *room)<br />
 <i>Return the name of the room (or NULL on error). </i><br />
 char * <code>ggzcore_room_get_desc</code> (<code>GGZRoom</code> *room)<br />
 <i>Return the description of the room (or NULL on error). </i><br />
 <code>GGZGameType</code> * <code>ggzcore_room_get_gametype</code> (<code>GGZRoom</code> *room)<br />
 <i>Return the type of game played in this room (or NULL on error). </i><br />
 int <code>ggzcore_room_get_num_players</code> (<code>GGZRoom</code> *room)<br />
 <i>Return the number of players in the room (or negative on error). </i><br />
 <code>GGZPlayer</code> * <code>ggzcore_room_get_nth_player</code> (<code>GGZRoom</code> *room, const unsigned int num)<br />
 <i>Return the nth player in the room (or NULL on error). </i><br />
 int <code>ggzcore_room_get_num_tables</code> (<code>GGZRoom</code> *room)<br />
 <i>Return the number of tables in the room (or negative on error). </i><br />
 <code>GGZTable</code> * <code>ggzcore_room_get_nth_table</code> (<code>GGZRoom</code> *room, const unsigned int num)<br />
 <i>Return the nth table in the room (or NULL on error). </i><br />
 <code>GGZTable</code> * <code>ggzcore_room_get_table_by_id</code> (<code>GGZRoom</code> *room, const unsigned int id)<br />
 <i>Return the table in this room with matching ID (NULL on error). </i><br />
 int <code>ggzcore_room_add_event_hook</code> (<code>GGZRoom</code> *room, const <code>GGZRoomEvent</code> event, const <code>GGZHookFunc</code> func)<br />
 <i>Register a handler (hook) for the room event. </i><br />
 int <code>ggzcore_room_add_event_hook_full</code> (<code>GGZRoom</code> *room, const <code>GGZRoomEvent</code> event, const <code>GGZHookFunc</code> func, const void *data)<br />
 <i>Register a handler (hook) for thee room event, with data. </i><br />
 int <code>ggzcore_room_remove_event_hook</code> (<code>GGZRoom</code> *room, const <code>GGZRoomEvent</code> event, const <code>GGZHookFunc</code> func)<br />
 <i>Remove a hook from an event. </i><br />
 int <code>ggzcore_room_remove_event_hook_id</code> (<code>GGZRoom</code> *room, const <code>GGZRoomEvent</code> event, const unsigned int hook_id)<br />
 <i>Remove a hook from an event, by ID. </i><br />
 int <code>ggzcore_room_list_players</code> (<code>GGZRoom</code> *room)<br />
 <i>Call to request a list of players in the room. </i><br />
 int <code>ggzcore_room_list_tables</code> (<code>GGZRoom</code> *room, const int type, const char global)<br />
 <i>Call to request a list of tables in the room. </i><br />
 int <code>ggzcore_room_chat</code> (<code>GGZRoom</code> *room, const GGZChatType opcode, const char *player, const char *msg)<br />
 <i>Chat! </i><br />
 int <code>ggzcore_room_launch_table</code> (<code>GGZRoom</code> *room, <code>GGZTable</code> *table)<br />
 <i>Launch a table in the room. </i><br />
 int <code>ggzcore_room_join_table</code> (<code>GGZRoom</code> *room, const unsigned int table_id, int spectator)<br />
 <i>Join a table in the room, so that you can then play at it. </i><br />
 int <code>ggzcore_room_leave_table</code> (<code>GGZRoom</code> *room, int force)<br />
 <i>Leave the table you are currently playing at. </i><br />
 char * <code>ggzcore_player_get_name</code> (const <code>GGZPlayer</code> *player)<br />
 <i>Return the name of the player. </i><br />
 GGZPlayerType <code>ggzcore_player_get_type</code> (const <code>GGZPlayer</code> *player)<br />
 <i>Return the type of the player (admin/registered/guest). </i><br />
 <code>GGZRoom</code> * <code>ggzcore_player_get_room</code> (const <code>GGZPlayer</code> *player)<br />
 <i>Return the player&#8217;s room, or NULL if none. </i><br />
 <code>GGZTable</code> * <code>ggzcore_player_get_table</code> (const <code>GGZPlayer</code> *player)<br />
 <i>Return the player&#8217;s table, or NULL if none. </i><br />
 int <code>ggzcore_player_get_lag</code> (const <code>GGZPlayer</code> *player)<br />
 <i>Return the player&#8217;s lag class (1..5). </i><br />
 int <code>ggzcore_player_get_record</code> (const <code>GGZPlayer</code> *player, int *wins, int *losses, int *ties, int *forfeits)<br />
 <i>Get the player&#8217;s win-loss record. </i><br />
 int <code>ggzcore_player_get_rating</code> (const <code>GGZPlayer</code> *player, int *rating)<br />
 <i>Get the player&#8217;s rating. </i><br />
 int <code>ggzcore_player_get_ranking</code> (const <code>GGZPlayer</code> *player, int *ranking)<br />
 <i>Get the player&#8217;s ranking. </i><br />
 int <code>ggzcore_player_get_highscore</code> (const <code>GGZPlayer</code> *player, int *highscore)<br />
 <i>Get the player&#8217;s highscore. </i><br />
 <code>GGZTable</code> * <code>ggzcore_table_new</code> (void)<br />
 <i>Create a new table object. </i><br />
 int <code>ggzcore_table_init</code> (<code>GGZTable</code> *table, const <code>GGZGameType</code> *gametype, const char *desc, const unsigned int num_seats)<br />
 <i>Set data on a table object. </i><br />
 void <code>ggzcore_table_free</code> (<code>GGZTable</code> *table)<br />
 <i>Free the table object. </i><br />
 int <code>ggzcore_table_set_seat</code> (<code>GGZTable</code> *table, const unsigned int seat, GGZSeatType type, const char *name)<br />
 <i>Set a seat type at a table, pre-launch. </i><br />
 int <code>ggzcore_table_remove_player</code> (<code>GGZTable</code> *table, char *name)<br />
 <i>Find and remove the player from the table. </i><br />
 int <code>ggzcore_table_get_id</code> (const <code>GGZTable</code> *table)<br />
 <i>Return the ID of the table. </i><br />
 const <code>GGZRoom</code> * <code>ggzcore_table_get_room</code> (const <code>GGZTable</code> *table)<br />
 <i>Return the room this table is in. </i><br />
 const <code>GGZGameType</code> * <code>ggzcore_table_get_type</code> (const <code>GGZTable</code> *table)<br />
 <i>Return the game type of the table. </i><br />
 const char * <code>ggzcore_table_get_desc</code> (const <code>GGZTable</code> *table)<br />
 <i>Return the table&#8217;s description (or NULL). </i><br />
 GGZTableState <code>ggzcore_table_get_state</code> (const <code>GGZTable</code> *table)<br />
 <i>Return the state of the table. </i><br />
 int <code>ggzcore_table_get_num_seats</code> (const <code>GGZTable</code> *table)<br />
 <i>Return the number of seats at the table. </i><br />
 int <code>ggzcore_table_set_desc</code> (<code>GGZTable</code> *table, const char *desc)<br />
 <i>Set the table description. </i><br />
 int <code>ggzcore_table_get_seat_count</code> (const <code>GGZTable</code> *table, GGZSeatType type)<br />
 <i>Count the seats of the given type. </i><br />
 const char * <code>ggzcore_table_get_nth_player_name</code> (const <code>GGZTable</code> *table, const unsigned int num)<br />
 <i>Return the name of a player at the table, or NULL on error. </i><br />
 int <code>ggzcore_table_get_num_spectator_seats</code> (const <code>GGZTable</code> *table)<br />
 <i>Return the number of spectator seats at the table, or -1. </i><br />
 const char * <code>ggzcore_table_get_nth_spectator_name</code> (const <code>GGZTable</code> *table, const unsigned int num)<br />
 <i>Return the name of the nth spectator, or NULL if seat is empty. </i><br />
 GGZSeatType <code>ggzcore_table_get_nth_player_type</code> (const <code>GGZTable</code> *table, const unsigned int num)<br />
 <i>Return the type of a player at the table, or GGZ_PLAYER_NONE on error. </i><br />
 unsigned int <code>ggzcore_gametype_get_id</code> (const <code>GGZGameType</code> *type)<br />
 <i>Get the ID of this gametype. </i><br />
 const char * <code>ggzcore_gametype_get_name</code> (const <code>GGZGameType</code> *type)<br />
 <i>Get the name of the game type. </i><br />
 const char * <code>ggzcore_gametype_get_prot_engine</code> (const <code>GGZGameType</code> *type)<br />
 <i>Get the protocol &#8216;engine&#8217; used by the game type. </i><br />
 const char * <code>ggzcore_gametype_get_prot_version</code> (const <code>GGZGameType</code> *type)<br />
 <i>Get the version of the protocol the game uses. </i><br />
 const char * <code>ggzcore_gametype_get_version</code> (const <code>GGZGameType</code> *type)<br />
 <i>Get the version of the game itself. </i><br />
 const char * <code>ggzcore_gametype_get_author</code> (const <code>GGZGameType</code> *type)<br />
 <i>Get the author of the game. </i><br />
 const char * <code>ggzcore_gametype_get_url</code> (const <code>GGZGameType</code> *type)<br />
 <i>Get a URL for more info about the game. </i><br />
 const char * <code>ggzcore_gametype_get_desc</code> (const <code>GGZGameType</code> *type)<br />
 <i>Get a description of the game. </i><br />
 int <code>ggzcore_gametype_get_max_players</code> (const <code>GGZGameType</code> *type)<br />
 <i>Get the maximum number of players the game can support. </i><br />
 int <code>ggzcore_gametype_get_max_bots</code> (const <code>GGZGameType</code> *type)<br />
 <i>Get the maximum number of bots the game can support. </i><br />
 int <code>ggzcore_gametype_get_spectators_allowed</code> (const <code>GGZGameType</code> *type)<br />
 <i>Return TRUE iff spectators are allowed for this game type. </i><br />
 int <code>ggzcore_gametype_num_players_is_valid</code> (const <code>GGZGameType</code> *type, unsigned int num)<br />
 <i>Return TRUE iff the given number of players is valid. </i><br />
 int <code>ggzcore_gametype_num_bots_is_valid</code> (const <code>GGZGameType</code> *type, unsigned int num)<br />
 <i>Return TRUE iff the given number of bots is valid. </i><br />
 int <code>ggzcore_conf_initialize</code> (const char *g_path, const char *u_path) </p>
<p> int <code>ggzcore_conf_write_string</code> (const char *section, const char *key, const char *value) </p>
<p> int <code>ggzcore_conf_write_int</code> (const char *section, const char *key, int value) </p>
<p> int <code>ggzcore_conf_write_list</code> (const char *section, const char *key, int argc, char **argv) </p>
<p> char * <code>ggzcore_conf_read_string</code> (const char *section, const char *key, const char *def) </p>
<p> int <code>ggzcore_conf_read_int</code> (const char *section, const char *key, int def) </p>
<p> int <code>ggzcore_conf_read_list</code> (const char *section, const char *key, int *argcp, char ***argvp) </p>
<p> int <code>ggzcore_conf_remove_section</code> (const char *section) </p>
<p> int <code>ggzcore_conf_remove_key</code> (const char *section, const char *key) </p>
<p> int <code>ggzcore_conf_commit</code> (void) </p>
<p> unsigned int <code>ggzcore_module_get_num</code> (void)<br />
 <i>This returns the number of registered modules. </i><br />
 int <code>ggzcore_module_add</code> (const char *name, const char *version, const char *prot_engine, const char *prot_version, const char *author, const char *frontend, const char *url, const char *exe_path, const char *icon_path, const char *help_path, <code>GGZModuleEnvironment</code> environment) </p>
<p> int <code>ggzcore_module_get_num_by_type</code> (const char *game, const char *engine, const char *version)<br />
 <i>Returns how many modules support this game and protocol. </i><br />
 <code>GGZModule</code> * <code>ggzcore_module_get_nth_by_type</code> (const char *game, const char *engine, const char *version, const unsigned int num)<br />
 <i>Returns n-th module that supports this game and protocol. </i><br />
 const char * <code>ggzcore_module_get_name</code> (<code>GGZModule</code> *module)<br />
 <i>Return the name of the module. </i><br />
 const char * <code>ggzcore_module_get_version</code> (<code>GGZModule</code> *module)<br />
 <i>Return the (game?) version of the module. </i><br />
 const char * <code>ggzcore_module_get_prot_engine</code> (<code>GGZModule</code> *module)<br />
 <i>Return the name of the module&#8217;s protocol engine. </i><br />
 const char * <code>ggzcore_module_get_prot_version</code> (<code>GGZModule</code> *module)<br />
 <i>Return the version of the module&#8217;s protocol engine. </i><br />
 const char * <code>ggzcore_module_get_author</code> (<code>GGZModule</code> *module)<br />
 <i>Return the author of the module. </i><br />
 const char * <code>ggzcore_module_get_frontend</code> (<code>GGZModule</code> *module)<br />
 <i>Return the module&#8217;s frontend type. </i><br />
 const char * <code>ggzcore_module_get_url</code> (<code>GGZModule</code> *module)<br />
 <i>Return the URL associated with the module. </i><br />
 const char * <code>ggzcore_module_get_icon_path</code> (<code>GGZModule</code> *module) </p>
<p> const char * <code>ggzcore_module_get_help_path</code> (<code>GGZModule</code> *module)<br />
 <i>Return the help path of the module (?). </i><br />
 char ** <code>ggzcore_module_get_argv</code> (<code>GGZModule</code> *module)<br />
 <i>Return the executable arguments for the module. See exec(). </i><br />
 <code>GGZModuleEnvironment</code> <code>ggzcore_module_get_environment</code> (<code>GGZModule</code> *module)<br />
 <i>Return the preferred environment type. </i><br />
 <code>GGZGame</code> * <code>ggzcore_game_new</code> (void)<br />
 <i>Make a new game object. </i><br />
 int <code>ggzcore_game_init</code> (<code>GGZGame</code> *game, <code>GGZServer</code> *server, <code>GGZModule</code> *module)<br />
 <i>Initialize the game object. </i><br />
 void <code>ggzcore_game_free</code> (<code>GGZGame</code> *game)<br />
 <i>Free the game object. </i><br />
 int <code>ggzcore_game_add_event_hook</code> (<code>GGZGame</code> *game, const <code>GGZGameEvent</code> event, const <code>GGZHookFunc</code> func)<br />
 <i>Register a hook for a game event. </i><br />
 int <code>ggzcore_game_add_event_hook_full</code> (<code>GGZGame</code> *game, const <code>GGZGameEvent</code> event, const <code>GGZHookFunc</code> func, const void *data)<br />
 <i>Register a hook for a game event. </i><br />
 int <code>ggzcore_game_remove_event_hook</code> (<code>GGZGame</code> *game, const <code>GGZGameEvent</code> event, const <code>GGZHookFunc</code> func)<br />
 <i>Remove a hook from a game event. </i><br />
 int <code>ggzcore_game_remove_event_hook_id</code> (<code>GGZGame</code> *game, const <code>GGZGameEvent</code> event, const unsigned int hook_id)<br />
 <i>Remove a specified hook from a game event. </i><br />
 int <code>ggzcore_game_get_control_fd</code> (<code>GGZGame</code> *game)<br />
 <i>Return the control (ggzmod) socket for the game. </i><br />
 <code>GGZModule</code> * <code>ggzcore_game_get_module</code> (<code>GGZGame</code> *game)<br />
 <i>Return the module set for the game. </i><br />
 int <code>ggzcore_game_launch</code> (<code>GGZGame</code> *game)<br />
 <i>Launch thee game! </i><br />
 int <code>ggzcore_game_read_data</code> (<code>GGZGame</code> *game)<br />
 <i>Read data from the game. When data is pending on the control socket, call this function. </i></p>
<h2>Detailed Description</h2>
<p> The interface for the ggzcore library used by GGZ clients. </p>
<h2>Define Documentation</h2>
<h3>#define ggzcore_module_launch(m) ((int)(-1))</h3>
<p> This attempts to launch the specified module and returns 0 if successful or -1 on error.</p>
<h2>Typedef Documentation</h2>
<h3>typedef void(* <code>GGZDestroyFunc</code>)(void *data)</h3>
<p> GGZ object destroy function type. </p>
<p> <code>Todo</code></p>
<dl>
<dt>
<dd> This is not currently used.</dl>
<h3>typedef struct _GGZGameType <code>GGZGameType</code></h3>
<p> Contains information about a _game type_. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Each room has one game type; a game may be used in multiple rooms.</dl>
<h3>typedef <code>GGZHookReturn</code>(* <code>GGZHookFunc</code>)(unsigned int id, const void *event_data, const void *user_data)</h3>
<p> GGZ Event hook function type, used as a vallback for events</p>
<h3>typedef struct <code>_GGZOptions</code> <code>GGZOptions</code></h3>
<p> Options structure for ggzcore library</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>GGZGameEvent</code></h3>
<p> A GGZGameEvent is an event associated with the game, that is triggered by a communication from the server or from the game. When a game event occurs, the associated event handle will be called, and will be passed the event data (a void*) along with the (optional) user data. All game events apply to the current game. Game events are usually triggered by calling ggzcore_server_read_data or ggzcore_game_read_data. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_game_add_event_hook</code> </p>
<p> <code>ggzcore_server_read_data</code></dl>
<p> <code>Enumeration values: </code></p>
<dl>
<dt><i>GGZ_GAME_LAUNCHED </i></p>
<dd> A game was launched by the player (you). After this the core client should call ggzcore_game_get_control_fd, monitor the socket that function returns, and call ggzcore_game_read_data when there is data pending. This event is triggered inside of ggzcore_game_launch.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> NULL</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_game_launch</code></dl>
<dl>
<dt><i>GGZ_GAME_LAUNCH_FAIL </i></p>
<dd> Your game launch has failed. Triggered instead of GGZ_GAME_LAUNCHED when there&#8217;s a failure somewhere.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> NULL</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>GGZ_GAME_LAUNCHED</code></dl>
<dl>
<dt><i>GGZ_GAME_NEGOTIATED </i></p>
<dd> Negotiation with server was successful. This should happen some time after the launch succeeds. The core client need do nothing at this point.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> NULL</dl>
<dl>
<dt><i>GGZ_GAME_NEGOTIATE_FAIL </i></p>
<dd> Negotiation was not successful, game launch failed.</dl>
<p> <code>Todo</code></p>
<dl>
<dt>
<dd> Currently this can&#8217;t actually happen&#8230;</dl>
<dl>
<dt><i>GGZ_GAME_PLAYING </i></p>
<dd> Game reached the &#8216;playing&#8217; state. When this happens the core client should call ggzcore_room_launch_table or ggzcore_room_join_table to finalize the game join.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> NULL</dl>
<h3>enum <code>GGZHookReturn</code></h3>
<p> GGZ Hook function return types </p>
<p> <code>Enumeration values: </code></p>
<dl>
<dt><i>GGZ_HOOK_OK </i></p>
<dd> Success!</p>
<dt><i>GGZ_HOOK_REMOVE </i></p>
<dd> Remove this hook immediately.</p>
<dt><i>GGZ_HOOK_ERROR </i></p>
<dd> A localized error.</p>
<dt><i>GGZ_HOOK_CRISIS </i></p>
<dd> A major error; stop processing the event.</dl>
<h3>enum <code>GGZLoginType</code></h3>
<p> This controls the type of login a user chooses. A different value will require different information to be sent to the server. </p>
<p> <code>Enumeration values: </code></p>
<dl>
<dt><i>GGZ_LOGIN </i></p>
<dd> Standard login; uname and correct passwd needed.</p>
<dt><i>GGZ_LOGIN_GUEST </i></p>
<dd> Guest login; only a uname is required.</p>
<dt><i>GGZ_LOGIN_NEW </i></p>
<dd> New user login; only a uname is required. Password will be assigned by the server (but can be passed along).</dl>
<h3>enum <code>GGZModuleEnvironment</code></h3>
<p> The environment a game frontend expects. </p>
<p> Core clients should offer those game modules which fit their own environment. </p>
<p> <code>Enumeration values: </code></p>
<dl>
<dt><i>GGZ_ENVIRONMENT_PASSIVE </i></p>
<dd> No GUI, no interaction with user</p>
<dt><i>GGZ_ENVIRONMENT_CONSOLE </i></p>
<dd> Text console</p>
<dt><i>GGZ_ENVIRONMENT_FRAMEBUFFER </i></p>
<dd> VESA or framebuffer</p>
<dt><i>GGZ_ENVIRONMENT_XWINDOW </i></p>
<dd> X11 windowed mode (default)</p>
<dt><i>GGZ_ENVIRONMENT_XFULLSCREEN </i></p>
<dd> X11 fullscreen mode</dl>
<h3>enum <code>GGZOptionFlags</code></h3>
<p> <code>Enumeration values: </code></p>
<dl>
<dt><i>GGZ_OPT_MODULES </i></p>
<dd> Load the default configuration file (unused).</p>
<dt><i>GGZ_OPT_THREADED_IO </i></p>
<dd> Load the game module list.</p>
<dt><i>GGZ_OPT_EMBEDDED </i></p>
<dd> Provide multi-threaded network IO (unused).</p>
<dt><i>GGZ_OPT_RECONNECT </i></p>
<dd> Reconnect automatically after connection loss.</dl>
<h3>enum <code>GGZRoomEvent</code></h3>
<p> A GGZRoomEvent is an event associated with the room, that is triggered by a communication from the server. When a room event occurs, the associated event handler will be called, and will be passed the event data (a void*), along with the (optional) user data. All room events apply to the current room unless a room number is given. Room events are almost always triggered by calling ggzcore_server_read_data. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_room_add_event_hook</code> </p>
<p> <code>ggzcore_server_read_data</code></dl>
<p> <code>Enumeration values: </code></p>
<dl>
<dt><i>GGZ_PLAYER_LIST </i></p>
<dd> The list of players in a room has arrived.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The room id (int *)</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This will only be issued for the current room.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_room_list_players</code></dl>
<dl>
<dt><i>GGZ_TABLE_LIST </i></p>
<dd> Received the list of active tables.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> NULL</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_room_list_tables</code></dl>
<dl>
<dt><i>GGZ_CHAT_EVENT </i></p>
<dd> Received a chat message of any kind. This can happen at any time when you&#8217;re in a room.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The <code>GGZChatEventData</code> associated with the chat.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>GGZChatEventData</code></dl>
<dl>
<dt><i>GGZ_ROOM_ENTER </i></p>
<dd> A player has entered the room with you.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> A <code>GGZRoomChangeEventData</code> structure.</dl>
<dl>
<dt><i>GGZ_ROOM_LEAVE </i></p>
<dd> A player has left your room.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> A <code>GGZRoomChangeEventData</code> structure.</dl>
<dl>
<dt><i>GGZ_TABLE_UPDATE </i></p>
<dd> One of the tables in the current room has changed.</dl>
<p> <code>Todo</code></p>
<dl>
<dt>
<dd> How are you supposed to know which table has changed? </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> NULL</dl>
</dl>
<dl>
<dt><i>GGZ_TABLE_LAUNCHED </i></p>
<dd> The table you tried to launch has launched!</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_room_launch_table</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> NULL</dl>
<dl>
<dt><i>GGZ_TABLE_LAUNCH_FAIL </i></p>
<dd> The table you tried to launch couldn&#8217;t be launched</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>GGZ_TABLE_LAUNCHED</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> A pointer to a <code>GGZErrorEventData</code></dl>
<dl>
<dt><i>GGZ_TABLE_JOINED </i></p>
<dd> Your table join attempt has succeeded.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_room_join_table</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The table index (int*) of the table we joined.</dl>
<dl>
<dt><i>GGZ_TABLE_JOIN_FAIL </i></p>
<dd> Joining a table did not succeed.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>GGZ_TABLE_JOINED</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> A helpful error string.</dl>
<dl>
<dt><i>GGZ_TABLE_LEFT </i></p>
<dd> You have successfully left the table you were at.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_room_leave_table</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The <code>GGZTableLeaveEventData</code> associated with the leave.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>GGZTableLeaveEventData</code></dl>
<dl>
<dt><i>GGZ_TABLE_LEAVE_FAIL </i></p>
<dd> Your attempt to leave the table has failed.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>GGZ_TABLE_LEFT</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> A helpful error string.</dl>
<dl>
<dt><i>GGZ_PLAYER_LAG </i></p>
<dd> A player&#8217;s lag (measure of connection speed) has been updated</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_player_get_lag</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The name of the player whose lag has changed.</dl>
<dl>
<dt><i>GGZ_PLAYER_STATS </i></p>
<dd> A player&#8217;s stats have been updated.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>GGZ_PLAYER_LIST</code> </p>
<p> <code>ggzcore_player_get_record</code> </p>
<p> <code>ggzcore_player_get_rating</code> </p>
<p> <code>ggzcore_player_get_ranking</code> </p>
<p> <code>ggzcore_player_get_highscore</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The name of the player whose stats have changed.</dl>
<dl>
<dt><i>GGZ_PLAYER_COUNT </i></p>
<dd> The number of players in a room has arrived.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> The room id (int *)</dl>
<h3>enum <code>GGZServerEvent</code></h3>
<p> A GGZServerEvent is an event triggered by a communication from the server. Each time an event occurs, the associated event handler will be called, and will be passed the event data (a void*). Most events are generated as a result of ggzcore_server_read_data. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_add_event_hook</code></dl>
<p> <code>Enumeration values: </code></p>
<dl>
<dt><i>GGZ_CONNECTED </i></p>
<dd> We have just made a connection to the server. After this point the server&#8217;s socket should be accessible and should be monitored for data. It happens in direct response to ggzcore_server_connect. Note that most events after this will only happen by calling ggzcore_server_read_data on the server&#8217;s FD!</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> NULL</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_connect</code></dl>
<dl>
<dt><i>GGZ_CONNECT_FAIL </i></p>
<dd> Error: we have failed to connect to the server. This is generated in place of GGZ_CONNECTED if the connection could not be made. The server object is otherwise unaffected.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> An error string (created by strerror)</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_connect</code></dl>
<dl>
<dt><i>GGZ_NEGOTIATED </i></p>
<dd> We have negotiated a connection to the server. This will happen automatically once a connection has been established, if the server socket is monitored.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This just means we&#8217;ve determined ggzd is at the other end.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> NULL</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_read_data</code></dl>
<dl>
<dt><i>GGZ_NEGOTIATE_FAIL </i></p>
<dd> Error: negotiation failure. Could be the wrong version. This will happen in place of a GGZ_NEGOTIATED if the server could not be negotiated with.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> A useless error string.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_read_data</code></dl>
<dl>
<dt><i>GGZ_LOGGED_IN </i></p>
<dd> We have successfully logged in. We can now start doing stuff. This will not happen until the client sends their login information.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_login</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> NULL</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_read_data</code></dl>
<dl>
<dt><i>GGZ_LOGIN_FAIL </i></p>
<dd> Error: login failure. This will happen in place of GGZ_LOGGED_IN if the login failed. The server object will be otherwise unaffected.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> A pointer to a <code>GGZErrorEventData</code>.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>GGZErrorEventData</code> </p>
<p> <code>ggzcore_server_read_data</code></dl>
<dl>
<dt><i>GGZ_MOTD_LOADED </i></p>
<dd> The MOTD has been read from the server and can be displayed. The server will send us the MOTD automatically after login; it can also be requested by ggzcore_server_motd. It is up to the client whether or not to display it. See the online documentation (somewhere?) about the MOTD markup format.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> Pointer to a <code>GGZMotdEventData</code> including the full MOTD text.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_motd</code></dl>
<p> <code>Todo</code></p>
<dl>
<dt>
<dd> The MOTD cannot be accessed outside of this event </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> ggzcore_server_read_data!</dl>
</dl>
<dl>
<dt><i>GGZ_ROOM_LIST </i></p>
<dd> The room list arrived. This will only happen after the list is requested by <code>ggzcore_server_list_rooms()</code>. The list may be accessed through <code>ggzcore_server_get_num_rooms()</code> and <code>ggzcore_server_get_nth_room()</code>. Until this event arrives these functions will be useless!</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> NULL</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_read_data</code></dl>
<dl>
<dt><i>GGZ_TYPE_LIST </i></p>
<dd> The list of game types is available. This will only happen after the list is requested by ggzcore_server_list_types(). The list may be accessed through <code>ggzcore_server_get_num_gametypes()</code> and <code>ggzcore_server_get_nth_gametype()</code>. Until this event arrives these functions will be useless!</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> NULL</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_read_data</code></dl>
<dl>
<dt><i>GGZ_SERVER_PLAYERS_CHANGED </i></p>
<dd> The number of players on the server has changed. This event is issued rather frequently every time players enter or leave.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> NULL</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_get_num_players</code> </p>
<p> <code>ggzcore_server_read_data</code></dl>
<dl>
<dt><i>GGZ_ENTERED </i></p>
<dd> We have successfully entered a room. This will be issued to tell us a room join has succeeded, after it has been requested.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> NULL</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_join_room</code> </p>
<p> <code>ggzcore_server_read_data</code></dl>
<dl>
<dt><i>GGZ_ENTER_FAIL </i></p>
<dd> Error: we have tried to enter a room and failed. This will be issued to tell us a room join has failed.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> A pointer to a <code>GGZErrorEventData</code>.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>GGZErrorEventData</code> </p>
<p> <code>ggzcore_server_join_room</code> </p>
<p> <code>ggzcore_server_read_data</code></dl>
<dl>
<dt><i>GGZ_LOGOUT </i></p>
<dd> Logged out of the server. This will happen when the server completes the communication; usually after ggzcore_net_send_logout is called.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> NULL</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_read_data</code></dl>
<dl>
<dt><i>GGZ_NET_ERROR </i></p>
<dd> Error: a network (transmission) error occurred. The server will automatically disconnect.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> A generally unhelpful error string.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_read_data</code></dl>
<dl>
<dt><i>GGZ_PROTOCOL_ERROR </i></p>
<dd> Error: a communication protocol error occured. This can happen in a variety of situations when the server sends us something we can&#8217;t handle. The server will be automatically disconnected.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> A technical error string.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_read_data</code></dl>
<dl>
<dt><i>GGZ_CHAT_FAIL </i></p>
<dd> Error: A chat message could not be sent. This will happen when we try to send a chat and the server rejects it.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> A pointer to a <code>GGZErrorEventData</code>.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>GGZErrorEventData</code> </p>
<p> <code>ggzcore_server_read_data</code></dl>
<dl>
<dt><i>GGZ_STATE_CHANGE </i></p>
<dd> The internal state of ggzcore has changed. This may happen at any time.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> NULL</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>GGZStateID</code> </p>
<p> <code>ggzcore_server_get_state</code></dl>
<dl>
<dt><i>GGZ_CHANNEL_CONNECTED </i></p>
<dd> Status event: a requested direct game connection has been established. To start a game (table), a channel must be created. This event will alert that the channel has been established. The channel&#8217;s FD should then be monitored for input, which should then be passed back to the server object for handling.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> NULL</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This event is deprecated and should not be used.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_get_channel</code> </p>
<p> <code>ggzcore_server_read_data</code></dl>
<dl>
<dt><i>GGZ_CHANNEL_READY </i></p>
<dd> Game channel is ready for read/write operations. After the channel has been connected, if we continue to monitor the socket eventually it will be negotiated and ready to use. At this point it is ready for the game client to use.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> NULL</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This event is deprecated and should not be used.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_read_data</code></dl>
<dl>
<dt><i>GGZ_CHANNEL_FAIL </i></p>
<dd> Error: Failure during setup of direct connection to game server. If the channel could not be prepared, this event will happen instead of GGZ_CHANNEL_READY or GGZ_CHANNEL_CONNECTED event. At this point the channel is no longer useful (I think).</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> An unhelpful error string</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This event is deprecated and should not be used.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_read_data</code></dl>
<dl>
<dt><i>GGZ_NUM_SERVER_EVENTS </i></p>
<dd> Terminator. Do not use.</dl>
<h3>enum <code>GGZStateID</code></h3>
<p> The states a server connection may be in. </p>
<p> On the client side, a simplistic state maching is used to tell what&#8217;s going on. A game client should usually consult the current state when determining what actions are possible. </p>
<p> <code>Enumeration values: </code></p>
<dl>
<dt><i>GGZ_STATE_OFFLINE </i></p>
<dd> Not connected (at all)</p>
<dt><i>GGZ_STATE_CONNECTING </i></p>
<dd> In the process of connecting.</p>
<dt><i>GGZ_STATE_RECONNECTING </i></p>
<dd> Continuous reconnection attempts.</p>
<dt><i>GGZ_STATE_ONLINE </i></p>
<dd> Connected, but not doing anything.</p>
<dt><i>GGZ_STATE_LOGGING_IN </i></p>
<dd> In the process of logging in.</p>
<dt><i>GGZ_STATE_LOGGED_IN </i></p>
<dd> Online and logged in!</p>
<dt><i>GGZ_STATE_ENTERING_ROOM </i></p>
<dd> Moving into a room.</p>
<dt><i>GGZ_STATE_IN_ROOM </i></p>
<dd> Online, logged in, and in a room.</p>
<dt><i>GGZ_STATE_BETWEEN_ROOMS </i></p>
<dd> Moving between rooms.</p>
<dt><i>GGZ_STATE_LAUNCHING_TABLE </i></p>
<dd> Trying to launch a table.</p>
<dt><i>GGZ_STATE_JOINING_TABLE </i></p>
<dd> Trying to join a table.</p>
<dt><i>GGZ_STATE_AT_TABLE </i></p>
<dd> Online, loggied in, in a room, at a table.</p>
<dt><i>GGZ_STATE_LEAVING_TABLE </i></p>
<dd> Waiting to leave a table.</p>
<dt><i>GGZ_STATE_LOGGING_OUT </i></p>
<dd> In the process of logging out.</dl>
<h2>Function Documentation</h2>
<h3>int ggzcore_conf_commit (void)</h3>
<p> <code>ggzcore_conf_commit()</code> &#8211; Commits the core user config file to disk </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> : int : 0 if successful, -1 on error</dl>
<h3>int ggzcore_conf_initialize (const char * g_path, const char * u_path)</h3>
<p> <code>ggzcore_conf_initialize()</code> Opens the global and/or user configuration files for the frontend. Either g_path or u_path can be NULL if the file is not to be used. The user config file will be created if it does not exist. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> : 0 on success, negative on failure</dl>
<h3>int ggzcore_conf_read_int (const char * section, const char * key, int def)</h3>
<p> <code>ggzcore_conf_read_int()</code> &#8211; Read a integer from the configuration file(s) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>section</i> section to get value from<br />
 <i>key</i> key value was stored under<br />
 <i>def</i> default value to return if none is found</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> an integer from the configuration file OR the default value</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> There is no guaranteed way to find if the call failed. If you must know, call ggzcore_conf_read_string with a NULL default value and check for the NULL return.</dl>
<h3>int ggzcore_conf_read_list (const char * section, const char * key, int * argcp, char *** argvp)</h3>
<p> <code>ggzcore_conf_read_list()</code> &#8211; Read a list from the configuration file(s) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>section</i> section to get value from<br />
 <i>key</i> key value was stored under<br />
 <i>argcp</i> ptr to int which will receive the list entry count<br />
 <i>argvp</i> a pointer to a dynamically allocated array that <code>ggzcore_conf_read_list()</code> will build</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> int : 0 if successful, -1 on error</dl>
<h3>char* ggzcore_conf_read_string (const char * section, const char * key, const char * def)</h3>
<p> <code>ggzcore_conf_read_string()</code> &#8211; Read a string from the configuration file(s) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>section</i> section to get value from<br />
 <i>key</i> key value was stored under<br />
 <i>def</i> default value to return if none is found</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> a dynamically allocated string from the configuration file OR a dynamically allocated copy of the default string</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The default may be set to NULL, in which case a NULL will be returned if the value could not be found in either configuration file.</dl>
<h3>int ggzcore_conf_remove_key (const char * section, const char * key)</h3>
<p> <code>ggzcore_conf_remove_key()</code> &#8211; Removes a key entry from the user config file </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>section</i> section to remove<br />
 <i>key</i> key entry to remove</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> int : 0 if success, -1 on error, 1 on soft error (section/key didn&#8217;t exist)</dl>
<h3>int ggzcore_conf_remove_section (const char * section)</h3>
<p> <code>ggzcore_conf_remove_section()</code> &#8211; Removes a section from the user config file </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>section</i> section to remove</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> int : 0 if successful, -1 on error, 1 on soft error (section did not exist)</dl>
<h3>int ggzcore_conf_write_int (const char * section, const char * key, int value)</h3>
<p> <code>ggzcore_conf_write_int()</code> &#8211; Write a integer to the user config file </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>section</i> section to store value in<br />
 <i>key</i> key to store value under<br />
 <i>value</i> value to store</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> int : 0 if successful, -1 on error</dl>
<h3>int ggzcore_conf_write_list (const char * section, const char * key, int argc, char ** argv)</h3>
<p> <code>ggzcore_conf_write_list()</code> &#8211; Write a list to the user config file </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>section</i> section to store value in<br />
 <i>key</i> key to store value under<br />
 <i>argc</i> count of string arguments in list<br />
 <i>argv</i> array of NULL terminated strings</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> int : 0 if successful, -1 on error</dl>
<h3>int ggzcore_conf_write_string (const char * section, const char * key, const char * value)</h3>
<p> <code>ggzcore_conf_write_string()</code> &#8211; Write a string to the user config file </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>section</i> section to store value in<br />
 <i>key</i> key to store value under<br />
 <i>value</i> value to store</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> int : 0 if successful, -1 on error</dl>
<h3>void ggzcore_destroy (void)</h3>
<p> <code>ggzcore_destroy()</code> &#8211; Cleanup function for ggzcore lib.</p>
<h3>int ggzcore_game_add_event_hook (<code>GGZGame</code> * game, const <code>GGZGameEvent</code> event, const <code>GGZHookFunc</code> func)</h3>
<p> Register a hook for a game event. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_add_event_hook</code> </p>
<p> <code>ggzcore_room_add_event_hook</code></dl>
<h3>int ggzcore_game_add_event_hook_full (<code>GGZGame</code> * game, const <code>GGZGameEvent</code> event, const <code>GGZHookFunc</code> func, const void * data)</h3>
<p> Register a hook for a game event. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_add_event_hook_full</code> </p>
<p> <code>ggzcore_room_add_event_hook_full</code></dl>
<h3>int ggzcore_game_read_data (<code>GGZGame</code> * game)</h3>
<p> Read data from the game. When data is pending on the control socket, call this function. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> negative on error</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_game_get_control_fd</code></dl>
<h3>int ggzcore_game_remove_event_hook (<code>GGZGame</code> * game, const <code>GGZGameEvent</code> event, const <code>GGZHookFunc</code> func)</h3>
<p> Remove a hook from a game event. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_remove_event_hook</code> </p>
<p> <code>ggzcore_room_remove_event_hook</code></dl>
<h3>int ggzcore_game_remove_event_hook_id (<code>GGZGame</code> * game, const <code>GGZGameEvent</code> event, const unsigned int hook_id)</h3>
<p> Remove a specified hook from a game event. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_remove_event_hook_id</code> </p>
<p> <code>ggzcore_room_remove_event_hook_id</code></dl>
<h3>unsigned int ggzcore_gametype_get_id (const <code>GGZGameType</code> * type)</h3>
<p> Get the ID of this gametype. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This is not normally useful for a GGZ client to know.</dl>
<h3>int ggzcore_gametype_get_max_bots (const <code>GGZGameType</code> * type)</h3>
<p> Get the maximum number of bots the game can support. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> ggzcore_gametype_bots_is_valid</dl>
<h3>int ggzcore_gametype_get_max_players (const <code>GGZGameType</code> * type)</h3>
<p> Get the maximum number of players the game can support. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_gametype_num_players_is_valid</code></dl>
<h3>int ggzcore_init (<code>GGZOptions</code> options)</h3>
<p> <code>ggzcore_init()</code> &#8211; Initializtion function for ggzcore lib. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>options</i> options structure</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> int : 0 if successful, -1 on failure</dl>
<h3>int ggzcore_module_add (const char * name, const char * version, const char * prot_engine, const char * prot_version, const char * author, const char * frontend, const char * url, const char * exe_path, const char * icon_path, const char * help_path, <code>GGZModuleEnvironment</code> environment)</h3>
<p> This adds a local module to the list. It returns 0 if successful or -1 on failure.</p>
<h3>const char* ggzcore_module_get_icon_path (<code>GGZModule</code> * module)</h3>
<p> This is (intended to be) an optional xpm file that the module can provide to use for representing the game graphically.</p>
<h3>int ggzcore_player_get_highscore (const <code>GGZPlayer</code> * player, int * highscore)</h3>
<p> Get the player&#8217;s highscore. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE if there is a highscore; FALSE if not or on error.</dl>
<h3>int ggzcore_player_get_ranking (const <code>GGZPlayer</code> * player, int * ranking)</h3>
<p> Get the player&#8217;s ranking. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE if there is a ranking; FALSE if not or on error.</dl>
<h3>int ggzcore_player_get_rating (const <code>GGZPlayer</code> * player, int * rating)</h3>
<p> Get the player&#8217;s rating. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE if there is a rating; FALSE if not or on error.</dl>
<h3>int ggzcore_player_get_record (const <code>GGZPlayer</code> * player, int * wins, int * losses, int * ties, int * forfeits)</h3>
<p> Get the player&#8217;s win-loss record. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE if there is a record; FALSE if not or on error.</dl>
<h3>void ggzcore_reload (void)</h3>
<p> <code>ggzcore_reload()</code> &#8211; Reload game module database</p>
<h3>int ggzcore_room_add_event_hook (<code>GGZRoom</code> * room, const <code>GGZRoomEvent</code> event, const <code>GGZHookFunc</code> func)</h3>
<p> Register a handler (hook) for the room event. </p>
<p> A room event will happen when data is received from the server. To make updates to the frontend, the client will need to register a hook function to handle the event. This hook function will be called each time the room event occurrs. More than one hook function may be specified, in which case they will all be called (in FIFO order). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>room</i> The room object to associate the hook with.<br />
 <i>event</i> The event the handler is going to be &#8216;hooked&#8217; onto.<br />
 <i>func</i> The event handler itself. This is called during the event.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The hook ID, or negative on error.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_room_add_event_hook_full</code> </p>
<p> <code>ggzcore_room_remove_event_hook</code> </p>
<p> <code>ggzcore_room_remove_event_hook_id</code></dl>
<h3>int ggzcore_room_add_event_hook_full (<code>GGZRoom</code> * room, const <code>GGZRoomEvent</code> event, const <code>GGZHookFunc</code> func, const void * data)</h3>
<p> Register a handler (hook) for thee room event, with data. </p>
<p> This function is similar to ggzcore_room_add_event_hook, except that user data will be associated with the hook. This data will be passed back to the function each time it is invoked on this event. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>room</i> The room object to associate the hook with.<br />
 <i>event</i> The event the handler is going to be &#8216;hooked&#8217; onto.<br />
 <i>func</i> The event handler itself. This is called during the event.<br />
 <i>data</i> The user data associated with the hook.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The hook ID, or negative on error.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_room_add_event_hook</code></dl>
<h3>int ggzcore_room_chat (<code>GGZRoom</code> * room, const GGZChatType opcode, const char * player, const char * msg)</h3>
<p> Chat! </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>room</i> Your current room.<br />
 <i>opcode</i> The chat type.<br />
 <i>player</i> The name of the target player (only for certain chat types)<br />
 <i>msg</i> The text of the chat message (some chat types don&#8217;t need it)</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, negative on (any) failure</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The chat message should be in UTF-8.</dl>
<h3>int ggzcore_room_join_table (<code>GGZRoom</code> * room, const unsigned int table_id, int spectator)</h3>
<p> Join a table in the room, so that you can then play at it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>room</i> Your current room.<br />
 <i>table_id</i> The table to join.<br />
 <i>spectator</i> TRUE if you wish to spectate, FALSE if you want to play</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, negative on (any) failure</dl>
<h3>int ggzcore_room_launch_table (<code>GGZRoom</code> * room, <code>GGZTable</code> * table)</h3>
<p> Launch a table in the room. </p>
<p> When a player wants to launch a new table, this is the function to do it. You must first create the table and set up the number and type of seats. Then call this function to initiate the launch. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>room</i> Your current room.<br />
 <i>table</i> The table to launch.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, negative on (any) failure</dl>
<h3>int ggzcore_room_leave_table (<code>GGZRoom</code> * room, int force)</h3>
<p> Leave the table you are currently playing at. </p>
<p> This function tries to leave your current table. You should &#8216;force&#8217; the leave only if the game client is inoperable, since for some games this will destroy the game server as well. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>room</i> Your current room.<br />
 <i>force</i> TRUE to force the leave, FALSE to leave it up to ggzd</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, negative on (any) failure</dl>
<h3>int ggzcore_room_list_players (<code>GGZRoom</code> * room)</h3>
<p> Call to request a list of players in the room. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>GGZ_PLAYER_LIST</code></dl>
<h3>int ggzcore_room_list_tables (<code>GGZRoom</code> * room, const int type, const char global)</h3>
<p> Call to request a list of tables in the room. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>room</i> Your current room<br />
 <i>type</i> currently ignored (???)<br />
 <i>global</i> currently ignored (???)</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>GGZ_TABLE_LIST</code></dl>
<h3>int ggzcore_room_remove_event_hook (<code>GGZRoom</code> * room, const <code>GGZRoomEvent</code> event, const <code>GGZHookFunc</code> func)</h3>
<p> Remove a hook from an event. </p>
<p> Removes a specific hook function from the hook list for the given room event. If more than one copy of the function exists in the list, the oldest one will be removed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>room</i> The room object to associate the hook with.<br />
 <i>event</i> The event the handler is to be unhooked from.<br />
 <i>func</i> The event handler function to remove.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, negative on failure.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_room_add_event_hook</code></dl>
<h3>int ggzcore_room_remove_event_hook_id (<code>GGZRoom</code> * room, const <code>GGZRoomEvent</code> event, const unsigned int hook_id)</h3>
<p> Remove a hook from an event, by ID. </p>
<p> Removes a specific hook from the hook list for the given room. The &#8216;ID&#8217; should be the same as that returned when the hook was added. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>room</i> The room object to associate the hook with.<br />
 <i>event</i> The event the handler is to be unhooked from.<br />
 <i>id</i> The ID of the hook to remove, as returned by the add function return 0 on success, negative on failure</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_room_add_event_hook</code></dl>
<h3>int ggzcore_server_add_event_hook (<code>GGZServer</code> * server, const <code>GGZServerEvent</code> event, const <code>GGZHookFunc</code> func)</h3>
<p> Register a callback handler for a server event. </p>
<p> Call this function to register the given GGZHookFunc as a handler for the given event. Then any time that event happens the handler function will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object.<br />
 <i>event</i> The server event to be handled.<br />
 <i>func</i> The handler function to be called when the event occurs.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A hook ID value to identify this handler.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Equivalent to ggzcore_server_add_event_hook_full with data==NULL. </p>
<p> More than one handler can be registered for each event.</dl>
<h3>int ggzcore_server_add_event_hook_full (<code>GGZServer</code> * server, const <code>GGZServerEvent</code> event, const <code>GGZHookFunc</code> func, const void * data)</h3>
<p> Register a callback handler for a server event. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_add_event_hook</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>data</i> An arbitrary pointer that will be passed to the hook function.</dl>
<h3>int ggzcore_server_connect (<code>GGZServer</code> * server)</h3>
<p> Connect to the server. </p>
<p> Call this function to initially connect to a GGZ server. Connection info is set using the ggzcore_server_set_hostinfo function. </p>
<p> The function is asynchronous and will return very quickly. After the connection is (hopefully) established we will receive either a GGZ_CONNECTED or GGZ_CONNECT_FAIL server event. If the connection succeeds, negotiations with the GGZ server will begin automatically. Once this is complete, we will receive either a GGZ_NEGOTIATED or GGZ_NEGOTIATE_FAIL event. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, -1 on failure.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> On success a GGZ_CONNECTED event will be generated. </p>
<p> On failure a GGZ_CONNECT_FAIL event may or may not be generated.</dl>
<h3>int ggzcore_server_get_fd (const <code>GGZServer</code> * server)</h3>
<p> Get the socket used for connection with the server. </p>
<p> This returns the file descriptor of the primary socket for the TCP connection to the server. All GGZ data goes across this socket. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The file descriptor of the connection socket.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_connect</code></dl>
<h3>const char* ggzcore_server_get_handle (const <code>GGZServer</code> * server)</h3>
<p> Get the handle being used for this server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A string containing the handle, or NULL on error.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_set_logininfo</code></dl>
<h3>const char* ggzcore_server_get_host (const <code>GGZServer</code> * server)</h3>
<p> Get the hostname of the server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A string containing the host name, or NULL on error.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_set_hostinfo</code></dl>
<h3>int ggzcore_server_get_num_gametypes (const <code>GGZServer</code> * server)</h3>
<p> Return the overall number of game types on the server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The number of game types on this server, or -1 on error.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This number is 0 until</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>GGZ_TYPE_LIST</code>.</dl>
<h3>int ggzcore_server_get_num_players (const <code>GGZServer</code> * server)</h3>
<p> Get the total number of players on the server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object return An approximate number of players in all rooms of the server.</dl>
<h3>int ggzcore_server_get_num_rooms (const <code>GGZServer</code> * server)</h3>
<p> Return the number of rooms on the server, or -1 on error. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Until we retrieve the list of rooms, this will return 0.</dl>
<h3>const char* ggzcore_server_get_password (const <code>GGZServer</code> * server)</h3>
<p> Get the password being used for this server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A string containing the password, or NULL on error.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_set_logininfo</code></dl>
<h3>int ggzcore_server_get_port (const <code>GGZServer</code> * server)</h3>
<p> Get the port of the server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The port number of the server, or -1 on error.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_set_hostinfo</code></dl>
<h3><code>GGZStateID</code> ggzcore_server_get_state (const <code>GGZServer</code> * server)</h3>
<p> Get the state of the server connection. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The state of the connection, or -1 on error.</dl>
<h3>int ggzcore_server_get_tls (const <code>GGZServer</code> * server)</h3>
<p> Get the current TLS status of this server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Whether TLS is active or not</dl>
<h3><code>GGZLoginType</code> ggzcore_server_get_type (const <code>GGZServer</code> * server)</h3>
<p> Get the login type being used for this server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The login type set for the server, or -1 on error.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_set_logininfo</code></dl>
<h3>int ggzcore_server_join_room (<code>GGZServer</code> * server, const unsigned int room)</h3>
<p> Join a room on the server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object.<br />
 <i>room</i> The number of the room to join.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, -1 on failure (e.g. non-existing room number).</dl>
<h3>int ggzcore_server_list_gametypes (<code>GGZServer</code> * server, const char verbose)</h3>
<p> Request game type list. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object.<br />
 <i>verbose</i> Receive detailed gametype information or not.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, -1 on failure.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> A GGZ_TYPE_LIST event will be the asynchronous response on success.</dl>
<h3>int ggzcore_server_list_rooms (<code>GGZServer</code> * server, const int type, const char verbose)</h3>
<p> Request room list. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object.<br />
 <i>type</i> Not used yet.<br />
 <i>verbose</i> Receive all information about a room or only the essentials.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, -1 on failure.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> A GGZ_ROOM_LIST might be generated thereafter.</dl>
<h3>int ggzcore_server_log_session (<code>GGZServer</code> * server, const char * filename)</h3>
<p> Initiate logging of ggzcore events. </p>
<p> Normally, ggzcore traffic is not logged anywhere. With this functions, such output can be directed into a file. It contains all the network messages received from the server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object.<br />
 <i>filename</i> The file the messages are written to.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, -1 on error.</dl>
<h3>int ggzcore_server_login (<code>GGZServer</code> * server)</h3>
<p> Log in to the server. </p>
<p> Call this function to log in to the server once a connection has been established. Typically you must first connect to the server, then wait to receive the GGZ_CONNECTED and GGZ_NEGOTIATED events before attempting to log in. Login info is set using the ggzcore_server_set_logininfo function. </p>
<p> The function is asynchronous and will return immediately. After the login request is sent, we will wait to receive either a GGZ_LOGGED_IN or GGZ_LOGIN_FAIL server event. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, -1 on failure.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> On failure no events will be generated.</dl>
<h3><code>GGZServer</code>* ggzcore_server_new (void)</h3>
<p> Create a new server object. </p>
<p> Call this function to create a server object. This object holds all state data for communicating with a ggz server. It is necessary for any kind of connection.</p>
<h3>int ggzcore_server_read_data (<code>GGZServer</code> * server, int fd)</h3>
<p> Read data for the server on the specified FD. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> negative on error</dl>
<h3>int ggzcore_server_remove_event_hook (<code>GGZServer</code> * server, const <code>GGZServerEvent</code> event, const <code>GGZHookFunc</code> func)</h3>
<p> Remove a single hook function from an event&#8217;s hook list. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object.<br />
 <i>event</i> The server event the hook is associated with.<br />
 <i>func</i> The function to be removed from the hook list.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success (hook removed); -1 on failure (no hook removed)</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> At most one copy of the function will be removed.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_remove_event_hook_id</code></dl>
<h3>int ggzcore_server_remove_event_hook_id (<code>GGZServer</code> * server, const <code>GGZServerEvent</code> event, const unsigned int hook_id)</h3>
<p> Remove a hook function with given ID from the event&#8217;s hook list. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object.<br />
 <i>event</i> The server event the hook is associated with.<br />
 <i>hook_id</i> The ID of the hook event.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success (hook removed); -1 on failure (no hook removed)</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The hook ID is given by ggzcore_server_add_event_hook</dl>
<h3>int ggzcore_server_reset (<code>GGZServer</code> * server)</h3>
<p> Reset the server object. </p>
<p> After you&#8217;ve disconnected, call this function to discard all state data and reset the state of the server object. You can then connect again. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> You should disconnect before resetting.</dl>
<h3>int ggzcore_server_set_hostinfo (<code>GGZServer</code> * server, const char * host, const unsigned int port, const unsigned int use_tls)</h3>
<p> Set host info for connecting to the server. </p>
<p> Call this function to set host info for the GGZ server before trying to connect to it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object.<br />
 <i>host</i> A string containing the hostname.<br />
 <i>port</i> The port to connect to.<br />
 <i>use_tls</i> If set, the connection will be encrypted.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, -1 on error.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Should never fail when given valid input.</dl>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> <code>ggzcore_server_connect</code></dl>
<h3>int ggzcore_server_set_logininfo (<code>GGZServer</code> * server, const <code>GGZLoginType</code> type, const char * handle, const char * password, const char * email)</h3>
<p> Set login info for logging in to the server. </p>
<p> Call this function to set login info for the GGZ server before trying to login. This should only be called when the server is in certain states. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>server</i> The GGZ server object.<br />
 <i>type</i> The type of login to attempt.<br />
 <i>handle</i> The username to use with the server.<br />
 <i>password</i> The password to use (may be NULL with some login types).<br />
 <i>email</i> The email address to use (may be NULL with some login types).</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, -1 on error.</dl>
<h3>int ggzcore_table_get_seat_count (const <code>GGZTable</code> * table, GGZSeatType type)</h3>
<p> Count the seats of the given type. </p>
<p> Given a table and a seat type, this function returns the number of seats at the table that match the type. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>table</i> A GGZ table.<br />
 <i>type</i> A GGZSeatType.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The number of seats matching the type, or -1 on error.</dl>
<h3>int ggzcore_table_init (<code>GGZTable</code> * table, const <code>GGZGameType</code> * gametype, const char * desc, const unsigned int num_seats)</h3>
<p> Set data on a table object. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Useful when launching a game.</dl>
<h3><code>GGZTable</code>* ggzcore_table_new (void)</h3>
<p> Create a new table object. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Useful when launching a game.</dl>
<h3>int ggzcore_table_set_seat (<code>GGZTable</code> * table, const unsigned int seat, GGZSeatType type, const char * name)</h3>
<p> Set a seat type at a table, pre-launch. </p>
<p> When launching a table, call this function to set up a particular seat at the table. It can also be used to fiddle with already existing tables, but that would be extremely unwise. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>table</i> The table object to change.<br />
 <i>seat</i> The seat number at the table to change.<br />
 <i>type</i> The type of seat to make it (open, reserved, or bot).<br />
 <i>name</i> The name of the seat (must be valid for reserved seats).</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success, -1 on error.</dl>
<p> <code>Todo</code></p>
<dl>
<dt>
<dd> How do we stop the GGZ client from fiddling with random tables?</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for GGZCore from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAP">Enumeration Type Documentation</a></p>
<dd>
<dt><a href="#lbAY">Function Documentation</a></p>
<dd>
<dt><a href="#lbDO">Author</a></p>
<dd></dl>
