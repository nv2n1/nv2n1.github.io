---
title: "globus_ftp_control_tcpbuffer_mode_t(3)"
name: "globus_ftp_control_tcpbuffer_mode_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_control_tcpbuffer_mode_t/"
description: "globus_ftp_control.h – GridFTP Control Connection API."
---

<h2 class="name">NAME</h2>
<p> globus_ftp_control.h &#8211; GridFTP Control Connection API.</p>
<h2>SYNOPSIS</h2>
<p> #include &#8216;globus_common.h&#8217;<br />
 #include &#8216;globus_error_string.h&#8217;<br />
 #include &#8216;globus_io.h&#8217;<br />
 #include &#8216;globus_gss_assist.h&#8217;<br />
 #include &#8216;globus_handle_table.h&#8217; </p>
<h3>Data Structures</h3>
<p> struct <code>globus_ftp_control_dcau_subject_s</code><br />
 <i>Control DCAU subject authentication type. </i><br />
 struct <code>globus_ftp_control_round_robin_s</code><br />
 <i>Control striping round robin attribute structure. </i><br />
 union <code>globus_ftp_control_dcau_u</code><br />
 <i>Control DCAU union. </i><br />
 union <code>globus_ftp_control_layout_u</code><br />
 <i>Control striping attribute union. </i><br />
 union <code>globus_ftp_control_parallelism_u</code><br />
 <i>Control parallelism attribute structure. </i><br />
 struct <code>globus_ftp_control_tcpbuffer_default_t</code><br />
 <i>Don&#8217;t change the TCP buffer/window size from the system default. </i><br />
 struct <code>globus_ftp_control_tcpbuffer_fixed_t</code><br />
 <i>Set the TCP buffer/window size to a fixed value. </i><br />
 struct <code>globus_ftp_control_tcpbuffer_automatic_s</code><br />
 <i>Automatically set the TCP buffer/window size. </i><br />
 union <code>globus_ftp_control_tcpbuffer_t</code><br />
 <i>Control tcpbuffer attribute structure. </i><br />
 struct <code>globus_ftp_control_auth_info_s</code><br />
 <i>Authentication Values. </i></p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_FTP_CONTROL_MODULE</code> (&amp;globus_i_ftp_control_module)<br />
 <i>Module descriptor. </i></p>
<h3>Typedefs</h3>
<p> typedef enum<br />
 <code>globus_ftp_control_type_e</code> <code>globus_ftp_control_type_t</code>&quot;<br />
 <i>GridFTP TYPE values. </i><br />
 typedef enum<br />
 <code>globus_ftp_control_mode_e</code> <code>globus_ftp_control_mode_t</code>&quot;<br />
 <i>GridFTP MODE values. </i><br />
 typedef enum<br />
 <code>globus_ftp_control_dcau_mode_e</code> <code>globus_ftp_control_dcau_mode_t</code>&quot;<br />
 <i>GridFTP DCAU values. </i><br />
 typedef struct<br />
 <code>globus_ftp_control_dcau_subject_s</code> <code>globus_ftp_control_dcau_subject_t</code>&quot;<br />
 <i>Control DCAU subject authentication type. </i><br />
 typedef enum<br />
 <code>globus_ftp_control_striping_mode_e</code> <code>globus_ftp_control_striping_mode_t</code>&quot;<br />
 <i>GridFTP Striping Types. </i><br />
 typedef struct<br />
 <code>globus_ftp_control_round_robin_s</code> <code>globus_ftp_control_round_robin_t</code>&quot;<br />
 <i>Control striping round robin attribute structure. </i><br />
 typedef union<br />
 <code>globus_ftp_control_dcau_u</code> <code>globus_ftp_control_dcau_t</code>&quot;<br />
 <i>Control DCAU union. </i><br />
 typedef union<br />
 <code>globus_ftp_control_layout_u</code> <code>globus_ftp_control_layout_t</code>&quot;<br />
 <i>Control striping attribute union. </i><br />
 typedef enum<br />
 <code>globus_ftp_control_structure_e</code> <code>globus_ftp_control_structure_t</code>&quot; </p>
<p> typedef enum<br />
 <code>globus_ftp_control_parallelism_mode_e</code> <code>globus_ftp_control_parallelism_mode_t</code>&quot; </p>
<p> typedef union<br />
 <code>globus_ftp_control_parallelism_u</code> <code>globus_ftp_control_parallelism_t</code>&quot;<br />
 <i>Control parallelism attribute structure. </i><br />
 typedef enum<br />
 <code>globus_ftp_control_tcpbuffer_mode_e</code> <code>globus_ftp_control_tcpbuffer_mode_t</code>&quot; </p>
<p> typedef struct<br />
 <code>globus_ftp_control_tcpbuffer_automatic_s</code> <code>globus_ftp_control_tcpbuffer_automatic_t</code>&quot;<br />
 <i>Automatically set the TCP buffer/window size. </i><br />
 typedef union<br />
 <code>globus_ftp_control_tcpbuffer_t</code> <code>globus_ftp_control_tcpbuffer_t</code>&quot;<br />
 <i>Control tcpbuffer attribute structure. </i><br />
 typedef struct<br />
 <code>globus_ftp_control_auth_info_s</code> <code>globus_ftp_control_auth_info_t</code>&quot;<br />
 <i>Authentication Values. </i><br />
 typedef void(* <code>globus_ftp_control_response_callback_t</code> )(void *callback_arg, struct globus_ftp_control_handle_s *handle, globus_object_t *error, globus_ftp_control_response_t *ftp_response) </p>
<p> typedef void(* <code>globus_ftp_control_callback_t</code> )(void *callback_arg, struct globus_ftp_control_handle_s *handle, globus_object_t *error) </p>
<p> typedef void(* <code>globus_ftp_control_command_callback_t</code> )(void *callback_arg, struct globus_ftp_control_handle_s *handle, globus_object_t *error, union globus_ftp_control_command_u *command) </p>
<p> typedef void(* <code>globus_ftp_control_auth_callback_t</code> )(void *callback_arg, struct globus_ftp_control_handle_s *handle, globus_object_t *error, <code>globus_ftp_control_auth_info_t</code> *auth_result) </p>
<p> typedef unsigned long <code>globus_ftp_control_auth_requirements_t</code> </p>
<p> typedef void(* <code>globus_ftp_control_data_callback_t</code> )(void *callback_arg, globus_ftp_control_handle_t *handle, globus_object_t *error, globus_byte_t *buffer, globus_size_t length, globus_off_t offset, globus_bool_t eof) </p>
<p> typedef void(* <code>globus_ftp_control_server_callback_t</code> )(void *callback_arg, struct globus_ftp_control_server_s *server_handle, globus_object_t *error)<br />
 <i>Server callback</i> </p>
<p> A function with this signature can be used as general callbacks for the GridFTP server API. &quot;</p>
<h3>Enumerations</h3>
<p> enum <code>globus_ftp_control_type_e</code> { <code>GLOBUS_FTP_CONTROL_TYPE_NONE</code>, <code>GLOBUS_FTP_CONTROL_TYPE_ASCII</code> = &#8216;A&#8217;, <code>GLOBUS_FTP_CONTROL_TYPE_EBCDIC</code> = &#8216;E&#8217;, <code>GLOBUS_FTP_CONTROL_TYPE_IMAGE</code> = &#8216;I&#8217;, <code>GLOBUS_FTP_CONTROL_TYPE_LOCAL</code> = &#8216;L&#8217; }<br />
 <i>GridFTP TYPE values. </i><br />
 enum <code>globus_ftp_control_mode_e</code> { <code>GLOBUS_FTP_CONTROL_MODE_NONE</code>, <code>GLOBUS_FTP_CONTROL_MODE_STREAM</code> = &#8216;S&#8217;, <code>GLOBUS_FTP_CONTROL_MODE_BLOCK</code> = &#8216;B&#8217;, <code>GLOBUS_FTP_CONTROL_MODE_EXTENDED_BLOCK</code> = &#8216;E&#8217;, <code>GLOBUS_FTP_CONTROL_MODE_COMPRESSED</code> = &#8216;C&#8217; }<br />
 <i>GridFTP MODE values. </i><br />
 enum <code>globus_ftp_control_dcau_mode_e</code> { <code>GLOBUS_FTP_CONTROL_DCAU_NONE</code> = &#8216;N&#8217;, <code>GLOBUS_FTP_CONTROL_DCAU_SELF</code> = &#8216;A&#8217;, <code>GLOBUS_FTP_CONTROL_DCAU_SUBJECT</code> = &#8216;S&#8217;, <code>GLOBUS_FTP_CONTROL_DCAU_DEFAULT</code> }<br />
 <i>GridFTP DCAU values. </i><br />
 enum <code>globus_ftp_control_striping_mode_e</code><br />
 <i>GridFTP Striping Types. </i><br />
 enum <code>globus_ftp_control_protection_t</code> { <code>GLOBUS_FTP_CONTROL_PROTECTION_CLEAR</code> = &#8216;C&#8217;, <code>GLOBUS_FTP_CONTROL_PROTECTION_SAFE</code> = &#8216;S&#8217;, <code>GLOBUS_FTP_CONTROL_PROTECTION_CONFIDENTIAL</code> = &#8216;E&#8217;, <code>GLOBUS_FTP_CONTROL_PROTECTION_PRIVATE</code> = &#8216;P&#8217; }<br />
 <i>GridFTP Protection Types. </i><br />
 enum <code>globus_ftp_control_delay_passive_t</code> </p>
<p> enum <code>globus_ftp_control_structure_e</code> </p>
<p> enum <code>globus_ftp_control_parallelism_mode_e</code> </p>
<p> enum <code>globus_ftp_control_tcpbuffer_mode_e</code> { <code>GLOBUS_FTP_CONTROL_TCPBUFFER_DEFAULT</code>, <code>GLOBUS_FTP_CONTROL_TCPBUFFER_FIXED</code>, <code>GLOBUS_FTP_CONTROL_TCPBUFFER_AUTOMATIC</code> } </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_ftp_control_local_layout</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_layout_t</code> *layout, globus_size_t data_size)<br />
 <i>Set data layout. </i><br />
 globus_result_t <code>globus_ftp_control_data_set_interface</code> (globus_ftp_control_handle_t *handle, const char *interface_addr)<br />
 <i>Create an outgoing FTP data connection. </i><br />
 globus_result_t <code>globus_ftp_control_create_data_info</code> (globus_ftp_control_handle_t *handle, globus_ftp_control_data_write_info_t *data_info, globus_byte_t *buffer, globus_size_t length, globus_off_t offset, globus_bool_t eof, <code>globus_ftp_control_data_callback_t</code> callback, void *callback_arg)<br />
 <i>Create a globus_ftp_control_data_write_info_t structure. </i><br />
 globus_result_t <code>globus_ftp_control_release_data_info</code> (globus_ftp_control_handle_t *handle, globus_ftp_control_data_write_info_t *data_info)<br />
 <i>Release a data_info structure. </i><br />
 globus_result_t <code>globus_ftp_control_data_write_stripe</code> (globus_ftp_control_handle_t *handle, globus_byte_t *buffer, globus_size_t length, globus_off_t offset, globus_bool_t eof, int stripe_ndx, <code>globus_ftp_control_data_callback_t</code> callback, void *callback_arg)<br />
 <i>Write FTP data to a stripe. </i><br />
 globus_result_t <code>globus_X_ftp_control_data_write_stripe</code> (globus_ftp_control_handle_t *handle, globus_byte_t *buffer, globus_size_t length, globus_off_t offset, globus_bool_t eof, int stripe_ndx, globus_ftp_control_data_write_info_t *data_info)<br />
 <i>Write data to a stripe from an enqueue callback. </i><br />
 globus_result_t <code>globus_ftp_control_auth_info_init</code> (<code>globus_ftp_control_auth_info_t</code> *auth_info, gss_cred_id_t credential_handle, globus_bool_t encrypt, char *user, char *password, char *account, char *subject)<br />
 <i>Initialize authentication information. </i><br />
 int <code>globus_ftp_control_auth_info_compare</code> (<code>globus_ftp_control_auth_info_t</code> *auth_info_1, <code>globus_ftp_control_auth_info_t</code> *auth_info_2)<br />
 <i>Compare authentication information. </i><br />
 globus_result_t <code>globus_ftp_control_handle_init</code> (globus_ftp_control_handle_t *handle)<br />
 <i>Initialize a globus ftp handle. </i><br />
 globus_result_t <code>globus_ftp_control_handle_destroy</code> (globus_ftp_control_handle_t *handle)<br />
 <i>Destroy a globus ftp handle. </i><br />
 globus_result_t <code>globus_ftp_control_server_handle_init</code> (globus_ftp_control_server_t *handle)<br />
 <i>Initialize a GridFTP server handle. </i><br />
 globus_result_t <code>globus_ftp_control_server_handle_destroy</code> (globus_ftp_control_server_t *handle)<br />
 <i>Destroy a GridFTP server handle. </i><br />
 globus_result_t <code>globus_ftp_control_response_destroy</code> (globus_ftp_control_response_t *response)<br />
 <i>Free the memory associated with a response. </i><br />
 globus_result_t <code>globus_ftp_control_response_copy</code> (globus_ftp_control_response_t *src, globus_ftp_control_response_t *dest)<br />
 <i>Copy a response structure. </i><br />
 globus_result_t <code>globus_ftp_control_connect</code> (globus_ftp_control_handle_t *handle, char *host, unsigned short port, <code>globus_ftp_control_response_callback_t</code> callback, void *callback_arg)<br />
 <i>Create a new control connection to an FTP server. </i><br />
 globus_result_t <code>globus_ftp_control_authenticate</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_auth_info_t</code> *auth_info, globus_bool_t use_auth, <code>globus_ftp_control_response_callback_t</code> callback, void *callback_arg)<br />
 <i>Authenticate the user to the FTP server. </i><br />
 globus_result_t <code>globus_ftp_control_authenticate_ex</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_auth_info_t</code> *auth_info, globus_bool_t use_auth, <code>globus_ftp_control_response_callback_t</code> callback, void *callback_arg)<br />
 <i>Authenticate the user to the FTP server. </i><br />
 globus_result_t <code>globus_ftp_control_abort</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_response_callback_t</code> callback, void *callback_arg)<br />
 <i>Send a GridFTP ABORT. </i><br />
 globus_result_t <code>globus_ftp_control_quit</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_response_callback_t</code> callback, void *callback_arg)<br />
 <i>Send a GridFTP QUIT. </i><br />
 globus_result_t <code>globus_ftp_control_force_close</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_response_callback_t</code> callback, void *callback_arg)<br />
 <i>Force a control connection to close. </i><br />
 globus_result_t <code>globus_ftp_control_send_command</code> (globus_ftp_control_handle_t *handle, const char *cmdspec, <code>globus_ftp_control_response_callback_t</code> callback, void *callback_arg,&#8230;)<br />
 <i>Send an FTP protocol command. </i><br />
 globus_result_t <code>globus_ftp_control_local_pbsz</code> (globus_ftp_control_handle_t *handle, unsigned long bufsize)<br />
 <i>Set data channel protection buffer size. </i><br />
 globus_result_t <code>globus_ftp_control_get_pbsz</code> (globus_ftp_control_handle_t *handle, unsigned long *bufsize)<br />
 <i>Get data channel protection buffer size. </i><br />
 globus_result_t <code>globus_ftp_control_server_listen</code> (globus_ftp_control_server_t *handle, unsigned short *port, <code>globus_ftp_control_server_callback_t</code> callback, void *callback_arg)<br />
 <i>Listen on for FTP Client Connections. </i><br />
 globus_result_t <code>globus_ftp_control_server_listen_ex</code> (globus_ftp_control_server_t *handle, globus_io_attr_t *attr, unsigned short *port, <code>globus_ftp_control_server_callback_t</code> callback, void *callback_arg)<br />
 <i>Listen on for FTP Client Connections. </i><br />
 globus_result_t <code>globus_ftp_control_server_stop</code> (globus_ftp_control_server_t *listener, <code>globus_ftp_control_server_callback_t</code> callback, void *callback_arg)<br />
 <i>Stop listening for GridFTP client connections. </i><br />
 globus_result_t <code>globus_ftp_control_server_accept</code> (globus_ftp_control_server_t *listener, globus_ftp_control_handle_t *handle, <code>globus_ftp_control_callback_t</code> callback, void *callback_arg)<br />
 <i>Accept a Client Connection. </i><br />
 globus_result_t <code>globus_ftp_control_server_authenticate</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_auth_requirements_t</code> auth_requirements, <code>globus_ftp_control_auth_callback_t</code> callback, void *callback_arg)<br />
 <i>Authenticate a GridFTP Client Connection. </i><br />
 globus_result_t <code>globus_ftp_control_read_commands</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_command_callback_t</code> callback, void *callback_arg)<br />
 <i>Read GridFTP commands. </i><br />
 globus_result_t <code>globus_ftp_control_send_response</code> (globus_ftp_control_handle_t *handle, const char *respspec, <code>globus_ftp_control_callback_t</code> callback, void *callback_arg,&#8230;)<br />
 <i>Send a GridFTP response. </i><br />
 globus_result_t <code>globus_ftp_control_command_copy</code> (globus_ftp_control_command_t *dest, globus_ftp_control_command_t *src)<br />
 <i>Copy of GridFTP command. </i><br />
 globus_result_t <code>globus_ftp_control_command_init</code> (globus_ftp_control_command_t *command, char *raw_command, <code>globus_ftp_control_auth_info_t</code> *auth_info)<br />
 <i>Initialize a GridFTP command. </i><br />
 globus_result_t <code>globus_ftp_control_command_destroy</code> (globus_ftp_control_command_t *command)<br />
 <i>Destroy a GridFTP command. </i><br />
 globus_result_t <code>globus_ftp_control_data_force_close</code> (globus_ftp_control_handle_t *control_handle, <code>globus_ftp_control_callback_t</code> destroy_callback, void *destroy_callback_arg)<br />
 <i>Close data connections. </i><br />
 globus_result_t <code>globus_ftp_control_local_send_eof</code> (globus_ftp_control_handle_t *handle, globus_bool_t send_eof)<br />
 <i>Enable or disable automatic EOF handling. </i><br />
 globus_result_t <code>globus_ftp_control_data_send_eof</code> (globus_ftp_control_handle_t *handle, int count[], int array_size, globus_bool_t eof_message, <code>globus_ftp_control_callback_t</code> cb, void *user_arg)<br />
 <i>Send EOF. </i><br />
 globus_result_t <code>globus_ftp_control_data_connect_read</code> (globus_ftp_control_handle_t *handle, globus_ftp_control_data_connect_callback_t callback, void *user_arg)<br />
 <i>Create an incoming FTP data connection. </i><br />
 globus_result_t <code>globus_ftp_control_data_connect_write</code> (globus_ftp_control_handle_t *handle, globus_ftp_control_data_connect_callback_t callback, void *user_arg)<br />
 <i>Create an outgoing FTP data connection. </i><br />
 globus_result_t <code>globus_ftp_control_data_add_channels</code> (globus_ftp_control_handle_t *handle, unsigned int num_channels, unsigned int stripe)<br />
 <i>Add data channels. </i><br />
 globus_result_t <code>globus_ftp_control_data_remove_channels</code> (globus_ftp_control_handle_t *handle, unsigned int num_channels, unsigned int stripe)<br />
 <i>Remove Data Channels. </i><br />
 globus_result_t <code>globus_ftp_control_data_query_channels</code> (globus_ftp_control_handle_t *handle, unsigned int *num_channels, unsigned int stripe)<br />
 <i>Number of data channels. </i><br />
 globus_result_t <code>globus_ftp_control_data_get_total_data_channels</code> (globus_ftp_control_handle_t *handle, unsigned int *num_channels, unsigned int stripe_ndx)<br />
 <i>Get Total Data Channels For a Stripe. </i><br />
 globus_result_t <code>globus_ftp_control_local_parallelism</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_parallelism_t</code> *parallelism)<br />
 <i>Set control handle parallelism. </i><br />
 globus_result_t <code>globus_ftp_control_local_pasv</code> (globus_ftp_control_handle_t *handle, globus_ftp_control_host_port_t *address)<br />
 <i>Create a passive socket. </i><br />
 globus_result_t <code>globus_ftp_control_local_spas</code> (globus_ftp_control_handle_t *handle, globus_ftp_control_host_port_t addresses[], unsigned int num_addresses)<br />
 <i>Create multiple passive sockets. </i><br />
 globus_result_t <code>globus_ftp_control_local_port</code> (globus_ftp_control_handle_t *handle, globus_ftp_control_host_port_t *address)<br />
 <i>Set remote data address. </i><br />
 globus_result_t <code>globus_ftp_control_local_spor</code> (globus_ftp_control_handle_t *handle, globus_ftp_control_host_port_t addresses[], unsigned int num_addresses)<br />
 <i>Set remote data addresses. </i><br />
 globus_result_t <code>globus_ftp_control_local_type</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_type_t</code> type, int form_code)<br />
 <i>Set control handle TYPE value. </i><br />
 globus_result_t <code>globus_ftp_control_local_tcp_buffer</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_tcpbuffer_t</code> *tcp_buffer)<br />
 <i>Set data handle TCP buffer size. </i><br />
 globus_result_t <code>globus_ftp_control_local_mode</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_mode_t</code> mode)<br />
 <i>Set data handle mode. </i><br />
 globus_result_t <code>globus_ftp_control_local_dcau</code> (globus_ftp_control_handle_t *handle, const <code>globus_ftp_control_dcau_t</code> *dcau, gss_cred_id_t delegated_credential_handle)<br />
 <i>Set data channel DCAU. </i><br />
 globus_result_t <code>globus_ftp_control_local_stru</code> (globus_ftp_control_handle_t *handle, <code>globus_ftp_control_structure_t</code> structure)<br />
 <i>Set data channel structure. </i><br />
 globus_result_t <code>globus_ftp_control_data_write</code> (globus_ftp_control_handle_t *handle, globus_byte_t *buffer, globus_size_t length, globus_off_t offset, globus_bool_t eof, <code>globus_ftp_control_data_callback_t</code> callback, void *callback_arg)<br />
 <i>Write data to data connections. </i><br />
 globus_result_t <code>globus_ftp_control_data_read</code> (globus_ftp_control_handle_t *handle, globus_byte_t *buffer, globus_size_t max_length, <code>globus_ftp_control_data_callback_t</code> callback, void *callback_arg)<br />
 <i>Read data from data connections. </i><br />
 globus_result_t <code>globus_ftp_control_set_force_order</code> (globus_ftp_control_handle_t *handle, globus_bool_t order_data, globus_off_t starting_offset)<br />
 <i>Set data handle to return read mode E data in order. </i><br />
 globus_result_t <code>globus_ftp_control_ipv6_allow</code> (globus_ftp_control_handle_t *handle, globus_bool_t allow)<br />
 <i>Not documented yet. </i><br />
 globus_result_t <code>globus_ftp_control_client_get_connection_info_ex</code> (globus_ftp_control_handle_t *handle, globus_ftp_control_host_port_t *local_info, globus_ftp_control_host_port_t *remote_info)<br />
 <i>Not documented yet. </i></p>
<h2>Detailed Description</h2>
<p> GridFTP Control Connection API. </p>
<h2>Typedef Documentation</h2>
<h3>typedef void(* globus_ftp_control_auth_callback_t)(void *callback_arg, struct globus_ftp_control_handle_s *handle, globus_object_t *error, <code>globus_ftp_control_auth_info_t</code> *auth_result)</h3>
<p> Server authentication complete callback. </p>
<p> A function with this signature is registered by calling globus_ftp_control_accept(). It is called when the authentication protocol has completed. Based on the auth_result, the server implementor should determine authorization and then send the appropriate response using <code>globus_ftp_control_send_response()</code>, indicating to the client whether authorization was successful or not. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> This structure is populated when the callback is called and represents a control connection to the client.<br />
 <i>auth_result</i> A globus_ftp_control_auth_result_t containing the values the client sent for gss authentication, user name, password and account. If any of the values were not sent by the client they will be NULL. Based on that information the user can decide if the client will be authorized for use of the server.<br />
 <i>callback_arg</i> The user argument passed to the callback.</dl>
<h3>typedef struct <code>globus_ftp_control_auth_info_s</code></h3>
<p>&nbsp;<wbr><code>globus_ftp_control_auth_info_t</code>&quot; </p>
<p> Authentication Values. This structure is populated and passed back to the user via the <code>globus_ftp_control_auth_callback_t()</code>. It contains the information needed to decide if a client may use the server.</p>
<h3>typedef unsigned long <code>globus_ftp_control_auth_requirements_t</code></h3>
<p> Authentication requirements. </p>
<p> The value of this should be a bitwise or of</p>
<dl>
<dt>&bull;</p>
<dd> GLOBUS_FTP_CONTROL_AUTH_NONE</p>
<dt>&bull;</p>
<dd> GLOBUS_FTP_CONTROL_AUTH_GSSAPI</p>
<dt>&bull;</p>
<dd> GLOBUS_FTP_CONTROL_AUTH_USER</p>
<dt>&bull;</p>
<dd> GLOBUS_FTP_CONTROL_AUTH_PASS</p>
<dt>&bull;</p>
<dd> GLOBUS_FTP_CONTROL_AUTH_ACCT</dl>
<h3>typedef void(* globus_ftp_control_callback_t)(void *callback_arg, struct globus_ftp_control_handle_s *handle, globus_object_t *error)</h3>
<p> Asynchronous control callback. </p>
<p> This callback is used as a generic control operation callback. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_arg</i> User supplied argument to the callback function<br />
 <i>handle</i> A pointer to the GridFTP control handle. Used to identify which control connection the operation was applied to.<br />
 <i>error</i> Pointer to a globus error object containing information about any errors that occurred processing the operation</dl>
<h3>typedef void(* globus_ftp_control_command_callback_t)(void *callback_arg, struct globus_ftp_control_handle_s *handle, globus_object_t *error, union globus_ftp_control_command_u *command)</h3>
<p> Server command callback. </p>
<p> When a command from a client is received on the control channel a user callback with this signature is called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_arg</i> The user argument passed to the callback function.<br />
 <i>handle</i> The control handle that the command was issued on.<br />
 <i>error</i> Indicates if a command was successful read or or if a failure occurred. This object will be freed once this callback returns. If the user wishes to have a copy of the error that persists past the life of this callback, they must make a copy using globus_object_copy(), and free it with globus_object_free().<br />
 <i>command</i> The command structure indicates what type of command the client issued. Based on the &#8216;type&#8217; further information can be extracted. This command structure will be freed once this callback returns. If the user wishes to have a copy of the error that persists past the life of this callback, they must make a copy using <code>globus_ftp_control_command_copy()</code>, and free it with globus_ftp_control_command_free().</dl>
<h3>typedef void(* globus_ftp_control_data_callback_t)(void *callback_arg, globus_ftp_control_handle_t *handle, globus_object_t *error, globus_byte_t *buffer, globus_size_t length, globus_off_t offset, globus_bool_t eof)</h3>
<p> Asynchronous data transmission operation callback. </p>
<p> This callback is called in functions that send or receive data on the data channel(s). </p>
<p> In the case of a write, this function is invoked when the entire data buffer is sent. Depending on the data transfer properties set by the globus_ftp_control_local_*() functions, the data may actually be split into multiple buffers and sent to multiple data nodes. </p>
<p> In the case of a read, this function will return a single extent of the data. The order of the data returned is not defined in an extended block mode data transfer, unless the ordered_data flag is set. It is up to the user of the API to re-construct the file order. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_arg</i> User supplied argument to the callback function<br />
 <i>handle</i> A pointer to the GridFTP control handle. Used to identify which control connection the operation was applied to.<br />
 <i>error</i> Pointer to a globus error object containing information about any errors that occurred processing the operation<br />
 <i>buffer</i> The user buffer passed as a parameter to <code>globus_ftp_control_data_read()</code> or <code>globus_ftp_control_data_write()</code>.<br />
 <i>length</i> The amount of data in the buffer. In the case of an incoming data channel, this may be less than the buffer size.<br />
 <i>offset</i> The file offset of the data which is contained in the buffer.<br />
 <i>eof</i> This is set to GLOBUS_TRUE then all of the data associated with the transfer has arrived on the data connections associated with this handle. If multiple data callbacks are registered with this handle, there is no guaranteed order of the EOF callback with respect to other data callbacks. If multiple callbacks are registered when EOF is reached on the data connections, at least one callback function will be called with eof set to GLOBUS_TRUE.</dl>
<h3>typedef enum <code>globus_ftp_control_parallelism_mode_e</code> <code>globus_ftp_control_parallelism_mode_t</code></h3>
<p> control parallelism Types</p>
<h3>typedef void(* globus_ftp_control_response_callback_t)(void *callback_arg, struct globus_ftp_control_handle_s *handle, globus_object_t *error, globus_ftp_control_response_t *ftp_response)</h3>
<p> Asynchronous operation completion callback. </p>
<p> This callback is called whenever a reply to command is received on the FTP control channel. It allows the user to handle the received reply or alternatively handle any errors that occurred during the interaction with the FTP server. This function will be called multiple times in the case when intermediate responses (1yz) are received. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_arg</i> User supplied argument to the callback function<br />
 <i>handle</i> A pointer to the GridFTP control handle. Used to identify which control connection the operation was applied to.<br />
 <i>error</i> Pointer to a globus error object containing information about any errors that occurred processing the operation<br />
 <i>ftp_response</i> Pointer to a response structure containing the FTP response to the command.</dl>
<h3>typedef enum <code>globus_ftp_control_structure_e</code> <code>globus_ftp_control_structure_t</code></h3>
<p> control structure structure</p>
<h3>typedef enum <code>globus_ftp_control_tcpbuffer_mode_e</code> <code>globus_ftp_control_tcpbuffer_mode_t</code></h3>
<p> TCP Buffer Setting Modes</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_ftp_control_delay_passive_t</code></h3>
<p> delayed passive flags</p>
<h3>enum <code>globus_ftp_control_parallelism_mode_e</code></h3>
<p> control parallelism Types</p>
<h3>enum <code>globus_ftp_control_structure_e</code></h3>
<p> control structure structure</p>
<h3>enum <code>globus_ftp_control_tcpbuffer_mode_e</code></h3>
<p> TCP Buffer Setting Modes </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>GLOBUS_FTP_CONTROL_TCPBUFFER_DEFAULT </i></p>
<dd> Don&#8217;t change the TCP buffer/window size from the system default</p>
<dt><i>GLOBUS_FTP_CONTROL_TCPBUFFER_FIXED </i></p>
<dd> Set the TCP buffer/window size to a fixed value</p>
<dt><i>GLOBUS_FTP_CONTROL_TCPBUFFER_AUTOMATIC </i></p>
<dd> Automatically set the TCP buffer/window size</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_control from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAU">Enumeration Type Documentation</a></p>
<dd>
<dt><a href="#lbAZ">Author</a></p>
<dd></dl>
