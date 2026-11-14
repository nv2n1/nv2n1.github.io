---
title: "ggz(3)"
name: "ggz"
section: "3"
letter: "g"
url: "/docs/linux/man/3-ggz/"
description: "ggz.h –"
---

<h2 class="name">NAME</h2>
<p> ggz.h &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/sys/types.h">sys/types.h</a>&gt; </p>
<h3>Defines</h3>
<p> #define <code>LIBGGZ_VERSION_MAJOR</code> 0 </p>
<p> #define <code>LIBGGZ_VERSION_MINOR</code> 0 </p>
<p> #define <code>LIBGGZ_VERSION_MICRO</code> 11 </p>
<p> #define <code>LIBGGZ_VERSION_IFACE</code> &#8216;3:1:1&#8217; </p>
<p> #define <code>ggz__attribute</code>(att)<br />
 <i>Allow easy use of GCC&#8217;s &#8216;attribute&#8217; macro for debugging. </i><br />
 #define <code>_GGZFUNCTION_</code> __FUNCTION__ </p>
<p> #define <code>GGZ_MEM_DEBUG</code> &#8216;ggz_mem&#8217;<br />
 <i>Debugging type for memory debugging. </i><br />
 #define <code>ggz_malloc</code>(size) _ggz_malloc(size, _GGZFUNCTION_ &#8216; in &#8216; __FILE__, __LINE__)<br />
 <i>Macro for memory allocation. </i><br />
 #define <code>ggz_realloc</code>(mem, size) _ggz_realloc(mem, size, _GGZFUNCTION_ &#8216; in &#8216; __FILE__, __LINE__)<br />
 <i>Macro for resizing previously allocated memory. </i><br />
 #define <code>ggz_free</code>(mem) _ggz_free(mem, _GGZFUNCTION_ &#8216; in &#8216; __FILE__, __LINE__)<br />
 <i>Macro for freeing memory previously allocated. </i><br />
 #define <code>ggz_strdup</code>(string) _ggz_strdup(string, _GGZFUNCTION_ &#8216; in &#8216; __FILE__, __LINE__)<br />
 <i>Macro for duplicating string. </i><br />
 #define <code>GGZ_CONF_DEBUG</code> &#8216;ggz_conf&#8217;<br />
 <i>Debugging type for config-file debugging. </i><br />
 #define <code>GGZ_LIST_REPLACE_DUPS</code> 0x00<br />
 <i>Overwrite duplicate values on insert. </i><br />
 #define <code>GGZ_LIST_ALLOW_DUPS</code> 0x01<br />
 <i>Allow duplicate data entries to exist in the list. </i><br />
 #define <code>GGZ_SOCKET_DEBUG</code> &#8216;socket&#8217;<br />
 <i>ggz_debug debugging type for Easysock debugging. </i></p>
<h3>Typedefs</h3>
<p> typedef int(* <code>ggzEntryCompare</code> )(const void *a, const void *b)<br />
 <i>A function type for doing data comparison on two items in a </i><code>GGZList</code>.<br />
 typedef void *(* <code>ggzEntryCreate</code> )(void *data)<br />
 <i>A function type for creating a copy of a data item for insertion into a </i><code>GGZList</code>.<br />
 typedef void(* <code>ggzEntryDestroy</code> )(void *data)<br />
 <i>A function type to destroy an entry in a </i><code>GGZList</code>.<br />
 typedef <code>_GGZListEntry</code> <code>GGZListEntry</code><br />
 <i>A single entry in a </i><code>GGZList</code>.<br />
 typedef <code>_GGZList</code> <code>GGZList</code><br />
 <i>Simple doubly-linked list. </i><br />
 typedef <code>_GGZList</code> <code>GGZStack</code><br />
 <i>Simple implementation of stacks using </i><code>GGZList</code>.<br />
 typedef <code>_GGZXMLElement</code> <code>GGZXMLElement</code><br />
 <i>Object representing a single XML element. </i><br />
 typedef void(* <code>GGZDebugHandlerFunc</code> )(int priority, const char *msg)<br />
 <i>A callback function to handle debugging output. </i><br />
 typedef _GGZFile <code>GGZFile</code><br />
 <i>Structure used internally by </i><code>ggz_read_line()</code>.<br />
 typedef void(* <code>ggzIOError</code> )(const char *msg, const <code>GGZIOType</code> type, const int fd, const <code>GGZDataType</code> data)<br />
 <i>An error function type. </i><br />
 typedef void(* <code>ggzIOExit</code> )(int status)<br />
 <i>An exit function type. </i></p>
<h3>Enumerations</h3>
<p> enum <code>GGZConfType</code> { <code>GGZ_CONF_RDONLY</code> = ((unsigned char) 0x01), <code>GGZ_CONF_RDWR</code> = ((unsigned char) 0x02), <code>GGZ_CONF_CREATE</code> = ((unsigned char) 0x04) }<br />
 <i>Specifies the mode for opening a configuration file. </i><br />
 enum <code>GGZCheckType</code> { <code>GGZ_CHECK_NONE</code> = 0x00, <code>GGZ_CHECK_MEM</code> = 0x01 }<br />
 <i>What memory checks should we do? </i><br />
 enum <code>GGZIOType</code> { <code>GGZ_IO_CREATE</code>, <code>GGZ_IO_READ</code>, <code>GGZ_IO_WRITE</code>, <code>GGZ_IO_ALLOCATE</code> }<br />
 <i>An error type for the GGZ socket functions. </i><br />
 enum <code>GGZDataType</code> { <code>GGZ_DATA_NONE</code>, <code>GGZ_DATA_CHAR</code>, <code>GGZ_DATA_INT</code>, <code>GGZ_DATA_STRING</code>, <code>GGZ_DATA_FD</code> }<br />
 <i>A data type for the GGZ socket function error handler. </i><br />
 enum <code>GGZSockType</code> { <code>GGZ_SOCK_SERVER</code>, <code>GGZ_SOCK_CLIENT</code> }<br />
 <i>A socket type. </i><br />
 enum <code>GGZTLSType</code> { <code>GGZ_TLS_CLIENT</code>, <code>GGZ_TLS_SERVER</code> }<br />
 <i>TLS operation mode. </i><br />
 enum <code>GGZTLSVerificationType</code> { <code>GGZ_TLS_VERIFY_NONE</code>, <code>GGZ_TLS_VERIFY_PEER</code> }<br />
 <i>TLS verification type. </i></p>
<h3>Functions</h3>
<p> void * <code>_ggz_malloc</code> (const size_t size, const char *tag, int line)<br />
 <i>Function to actually perform memory allocation. </i><br />
 void * <code>_ggz_realloc</code> (const void *ptr, const size_t size, const char *tag, int line)<br />
 <i>Function to perform memory reallocation. </i><br />
 int <code>_ggz_free</code> (const void *ptr, const char *tag, int line)<br />
 <i>Function to free allocated memory. </i><br />
 char * <code>_ggz_strdup</code> (const char *ptr, const char *tag, int line)<br />
 <i>Function to copy a string. </i><br />
 int <code>ggz_memory_check</code> (void)<br />
 <i>Check memory allocated against memory freed and display any discrepancies. </i><br />
 void <code>ggz_conf_cleanup</code> (void)<br />
 <i>Closes all open configuration files. </i><br />
 void <code>ggz_conf_close</code> (int handle)<br />
 <i>Closes one configuration file. </i><br />
 int <code>ggz_conf_parse</code> (const char *path, const <code>GGZConfType</code> options)<br />
 <i>Opens a configuration file and parses the variables so they can be retrieved with the access functions. </i><br />
 int <code>ggz_conf_commit</code> (int handle)<br />
 <i>Commits any changed variables to the configuration file. </i><br />
 int <code>ggz_conf_write_string</code> (int handle, const char *section, const char *key, const char *value)<br />
 <i>Writes a string value to a section and key in an open configuration file. </i><br />
 int <code>ggz_conf_write_int</code> (int handle, const char *section, const char *key, int value)<br />
 <i>Writes an integer value to a section and key in an open configuration file. </i><br />
 int <code>ggz_conf_write_list</code> (int handle, const char *section, const char *key, int argc, char **argv)<br />
 <i>Writes a list of string values to a section and key in an open configuration file. </i><br />
 char * <code>ggz_conf_read_string</code> (int handle, const char *section, const char *key, const char *def)<br />
 <i>Reads a string value from an open configuration file. </i><br />
 int <code>ggz_conf_read_int</code> (int handle, const char *section, const char *key, int def)<br />
 <i>Reads an integer value from an open configuration file. </i><br />
 int <code>ggz_conf_read_list</code> (int handle, const char *section, const char *key, int *argcp, char ***argvp)<br />
 <i>Reads a list of string values from an open configuration file. </i><br />
 int <code>ggz_conf_remove_section</code> (int handle, const char *section)<br />
 <i>This will remove an entire section and all its associated keys from a configuration file. </i><br />
 int <code>ggz_conf_remove_key</code> (int handle, const char *section, const char *key)<br />
 <i>This will remove a single key from a configuration file. </i><br />
 int <code>ggz_conf_get_sections</code> (int handle, int *argcp, char ***argvp)<br />
 <i>This function returns a list of all sections in a config file. </i><br />
 int <code>ggz_conf_get_keys</code> (int handle, const char *section, int *argcp, char ***argvp)<br />
 <i>This function returns a list of all keys within a section in a config file. </i><br />
 <code>GGZList</code> * <code>ggz_list_create</code> (<code>ggzEntryCompare</code> compare_func, <code>ggzEntryCreate</code> create_func, <code>ggzEntryDestroy</code> destroy_func, int options)<br />
 <i>Create a new </i><code>GGZList</code>.<br />
 int <code>ggz_list_insert</code> (<code>GGZList</code> *list, void *data)<br />
 <i>Insert data into a list. </i><br />
 <code>GGZListEntry</code> * <code>ggz_list_head</code> (<code>GGZList</code> *list)<br />
 <i>Get the first node of a list. </i><br />
 <code>GGZListEntry</code> * <code>ggz_list_tail</code> (<code>GGZList</code> *list)<br />
 <i>Get the last node of a list. </i><br />
 <code>GGZListEntry</code> * <code>ggz_list_next</code> (<code>GGZListEntry</code> *entry)<br />
 <i>Get the next node of a list. </i><br />
 <code>GGZListEntry</code> * <code>ggz_list_prev</code> (<code>GGZListEntry</code> *entry)<br />
 <i>Get the previous node of a list. </i><br />
 void * <code>ggz_list_get_data</code> (<code>GGZListEntry</code> *entry)<br />
 <i>Retrieve the data stored in a list entry. </i><br />
 <code>GGZListEntry</code> * <code>ggz_list_search</code> (<code>GGZList</code> *list, void *data)<br />
 <i>Search for a specified data item in the list. </i><br />
 <code>GGZListEntry</code> * <code>ggz_list_search_alt</code> (<code>GGZList</code> *list, void *data, <code>ggzEntryCompare</code> compare_func)<br />
 <i>Search for a specified data item in the list using a provided comparison function. </i><br />
 void <code>ggz_list_delete_entry</code> (<code>GGZList</code> *list, <code>GGZListEntry</code> *entry)<br />
 <i>Removes an entry from a list, calling a destructor if registered. </i><br />
 void <code>ggz_list_free</code> (<code>GGZList</code> *list)<br />
 <i>Free all resources associated with a list. </i><br />
 int <code>ggz_list_count</code> (<code>GGZList</code> *list)<br />
 <i>Get the length of the list. </i><br />
 int <code>ggz_list_compare_str</code> (void *a, void *b)<br />
 <i>Compare two character strings. </i><br />
 void * <code>ggz_list_create_str</code> (void *data)<br />
 <i>Copy a character string. </i><br />
 void <code>ggz_list_destroy_str</code> (void *data)<br />
 <i>Free a character string. </i><br />
 <code>GGZStack</code> * <code>ggz_stack_new</code> (void)<br />
 <i>Create a new stack. </i><br />
 void <code>ggz_stack_push</code> (<code>GGZStack</code> *stack, void *data)<br />
 <i>Push a data item onto the top of the stack. </i><br />
 void * <code>ggz_stack_pop</code> (<code>GGZStack</code> *stack)<br />
 <i>Pop the top item off of the stack. </i><br />
 void * <code>ggz_stack_top</code> (<code>GGZStack</code> *stack)<br />
 <i>Get the top item on the stack without popping it. </i><br />
 void <code>ggz_stack_free</code> (<code>GGZStack</code> *stack)<br />
 <i>Free the stack. </i><br />
 <code>GGZXMLElement</code> * <code>ggz_xmlelement_new</code> (const char *tag, const char *const *attrs, void(*process)(), void(*free)())<br />
 <i>Create a new </i><code>GGZXMLElement</code> element.<br />
 void <code>ggz_xmlelement_init</code> (<code>GGZXMLElement</code> *element, const char *tag, const char *const *attrs, void(*process)(), void(*free)())<br />
 <i>Initialize a </i><code>GGZXMLElement</code>.<br />
 void <code>ggz_xmlelement_set_data</code> (<code>GGZXMLElement</code> *element, void *data)<br />
 <i>Set ancillary data on a </i><code>GGZXMLElement</code> object.<br />
 const char * <code>ggz_xmlelement_get_tag</code> (<code>GGZXMLElement</code> *element)<br />
 <i>Get an XML element&#8217;s name. </i><br />
 const char * <code>ggz_xmlelement_get_attr</code> (<code>GGZXMLElement</code> *element, const char *attr)<br />
 <i>Get the value of an attribute on XML element. </i><br />
 void * <code>ggz_xmlelement_get_data</code> (<code>GGZXMLElement</code> *element)<br />
 <i>Get the user-supplied data associated with an XML element. </i><br />
 char * <code>ggz_xmlelement_get_text</code> (<code>GGZXMLElement</code> *element)<br />
 <i>Get an XML element&#8217;s content text. </i><br />
 void <code>ggz_xmlelement_add_text</code> (<code>GGZXMLElement</code> *element, const char *text, int len)<br />
 <i>Append a string to the element&#8217;s content text. </i><br />
 void <code>ggz_xmlelement_free</code> (<code>GGZXMLElement</code> *element)<br />
 <i>Free the memory associated with an XML element. </i><br />
 void <code>ggz_debug_init</code> (const char **types, const char *file)<br />
 <i>Initialize and configure debugging for the program. </i><br />
 <code>GGZDebugHandlerFunc</code> <code>ggz_debug_set_func</code> (<code>GGZDebugHandlerFunc</code> func)<br />
 <i>Set the debug handler function. </i><br />
 void <code>ggz_debug_enable</code> (const char *type)<br />
 <i>Enable a specific type of debugging. </i><br />
 void <code>ggz_debug_disable</code> (const char *type)<br />
 <i>Disable a specific type of debugging. </i><br />
 void <code>ggz_debug</code> (const char *type, const char *fmt,&#8230;) ggz__attribute((format(printf<br />
 <i>Log a debugging message. </i><br />
 void void <code>ggz_log</code> (const char *type, const char *fmt,&#8230;) ggz__attribute((format(printf<br />
 <i>Log a notice message. </i><br />
 void void void <code>ggz_error_sys</code> (const char *fmt,&#8230;) ggz__attribute((format(printf<br />
 <i>Log a syscall error. </i><br />
 void void void void <code>ggz_error_sys_exit</code> (const char *fmt,&#8230;) ggz__attribute((format(printf<br />
 <i>Log a fatal syscall error. </i><br />
 void void void void <code>ggz__attribute</code> ((noreturn)) </p>
<p> void <code>ggz_error_msg</code> (const char *fmt,&#8230;) ggz__attribute((format(printf<br />
 <i>Log an error message. </i><br />
 void void <code>ggz_error_msg_exit</code> (const char *fmt,&#8230;) ggz__attribute((format(printf<br />
 <i>Log a fatal error message. </i><br />
 void <code>ggz_debug_cleanup</code> (<code>GGZCheckType</code> check)<br />
 <i>Cleans up debugging state and prepares for exit. </i><br />
 char * <code>ggz_xml_escape</code> (const char *str)<br />
 <i>Escape XML characters in a text string. </i><br />
 char * <code>ggz_xml_unescape</code> (const char *str)<br />
 <i>Restore escaped XML characters into a text string. </i><br />
 <code>GGZFile</code> * <code>ggz_get_file_struct</code> (int fdes)<br />
 <i>Setup a file structure to use with </i><code>ggz_read_line()</code>.<br />
 char * <code>ggz_read_line</code> (<code>GGZFile</code> *file)<br />
 <i>Read a line of arbitrary length from a file. </i><br />
 void <code>ggz_free_file_struct</code> (<code>GGZFile</code> *file)<br />
 <i>Deallocate a file structure allocated via </i><code>ggz_get_file_struct()</code>.<br />
 int <code>ggz_strcmp</code> (const char *s1, const char *s2)<br />
 <i>String comparison function that is safe with NULLs. </i><br />
 int <code>ggz_strcasecmp</code> (const char *s1, const char *s2)<br />
 <i>Case-insensitive string comparison function that is safe with NULLs The function returns an integer less than, equal to, or greater than zero if s1 is found, respectively, to be less than, to match, or be greater than s2. </i><br />
 int <code>ggz_set_io_error_func</code> (<code>ggzIOError</code> func)<br />
 <i>Set the ggz/easysock error handling function. </i><br />
 <code>ggzIOError</code> <code>ggz_remove_io_error_func</code> (void)<br />
 <i>Remove the ggz/easysock error handling function. </i><br />
 int <code>ggz_set_io_exit_func</code> (<code>ggzIOExit</code> func)<br />
 <i>Set the ggz/easysock exit function. </i><br />
 <code>ggzIOExit</code> <code>ggz_remove_io_exit_func</code> (void)<br />
 <i>Remove the ggz/easysock exit function. </i><br />
 unsigned int <code>ggz_get_io_alloc_limit</code> (void)<br />
 <i>Get libggz&#8217;s limit on memory allocation. </i><br />
 unsigned int <code>ggz_set_io_alloc_limit</code> (const unsigned int limit)<br />
 <i>Set libggz&#8217;s limit on memory allocation. </i><br />
 int <code>ggz_init_network</code> (void)<br />
 <i>Initialize the network. </i><br />
 int <code>ggz_make_socket</code> (const <code>GGZSockType</code> type, const unsigned short port, const char *server)<br />
 <i>Make a socket connection. </i><br />
 int <code>ggz_make_socket_or_die</code> (const <code>GGZSockType</code> type, const unsigned short port, const char *server)<br />
 <i>Make a socket connection, exiting on error. </i><br />
 int <code>ggz_make_unix_socket</code> (const <code>GGZSockType</code> type, const char *name)<br />
 <i>Connect to a unix domain socket. </i><br />
 int <code>ggz_make_unix_socket_or_die</code> (const <code>GGZSockType</code> type, const char *name)<br />
 <i>Connect to a unix domain socket, exiting on error. </i><br />
 int <code>ggz_write_char</code> (const int sock, const char data)<br />
 <i>Write a character value to the given socket. </i><br />
 void <code>ggz_write_char_or_die</code> (const int sock, const char data)<br />
 <i>Write a character value to the given socket, exiting on error. </i><br />
 int <code>ggz_read_char</code> (const int sock, char *data)<br />
 <i>Read a character value from the given socket. </i><br />
 void <code>ggz_read_char_or_die</code> (const int sock, char *data)<br />
 <i>Read a character value from the given socket, exiting on error. </i><br />
 int <code>ggz_write_int</code> (const int sock, const int data)<br />
 <i>Write an integer to the socket in network byte order. </i><br />
 void <code>ggz_write_int_or_die</code> (const int sock, const int data)<br />
 <i>Write an integer to the socket, exiting on error. </i><br />
 int <code>ggz_read_int</code> (const int sock, int *data)<br />
 <i>Read an integer from the socket in network byte order. </i><br />
 void <code>ggz_read_int_or_die</code> (const int sock, int *data)<br />
 <i>Read an integer from the socket, exiting on error. </i><br />
 int <code>ggz_write_string</code> (const int sock, const char *data)<br />
 <i>Write a string to the given socket. </i><br />
 void <code>ggz_write_string_or_die</code> (const int sock, const char *data)<br />
 <i>Write a string to the given socket, exiting on error. </i><br />
 int <code>ggz_va_write_string</code> (const int sock, const char *fmt,&#8230;) ggz__attribute((format(printf<br />
 <i>Write a printf-style formatted string to the given socket. </i><br />
 int void <code>ggz_va_write_string_or_die</code> (const int sock, const char *fmt,&#8230;) ggz__attribute((format(printf<br />
 <i>Write a formatted string to the socket, exiting on error. </i><br />
 int void int <code>ggz_read_string</code> (const int sock, char *data, const unsigned int len)<br />
 <i>Read a string from the given socket. </i><br />
 void <code>ggz_read_string_or_die</code> (const int sock, char *data, const unsigned int len)<br />
 <i>Read a string from the given socket, exiting on error. </i><br />
 int <code>ggz_read_string_alloc</code> (const int sock, char **data)<br />
 <i>Read and allocate a string from the given socket. </i><br />
 void <code>ggz_read_string_alloc_or_die</code> (const int sock, char **data)<br />
 <i>Read and allocate string from the given socket, exiting on error. </i><br />
 int <code>ggz_write_fd</code> (const int sock, int sendfd)<br />
 <i>Write a file descriptor to the given (local) socket. </i><br />
 int <code>ggz_read_fd</code> (const int sock, int *recvfd)<br />
 <i>Read a file descriptor from the given (local) socket. </i><br />
 int <code>ggz_writen</code> (const int sock, const void *vdata, size_t n)<br />
 <i>Write a sequence of bytes to the socket. </i><br />
 int <code>ggz_readn</code> (const int sock, void *data, size_t n)<br />
 <i>Read a sequence of bytes from the socket. </i><br />
 <code>hash_t</code> <code>ggz_hash_create</code> (const char *algo, const char *text)<br />
 <i>Create a hash over a text. </i><br />
 <code>hash_t</code> <code>ggz_hmac_create</code> (const char *algo, const char *text, const char *secret)<br />
 <i>Create a HMAC hash over a text. </i><br />
 char * <code>ggz_base64_encode</code> (const char *text, int length)<br />
 <i>Encodes text to base64. </i><br />
 char * <code>ggz_base64_decode</code> (const char *text, int length)<br />
 <i>Decodes text from base64. </i><br />
 void <code>ggz_tls_init</code> (const char *certfile, const char *keyfile, const char *password)<br />
 <i>Initialize TLS support on the server side. </i><br />
 int <code>ggz_tls_support_query</code> (void)<br />
 <i>Check TLS support. </i><br />
 int <code>ggz_tls_enable_fd</code> (int fdes, <code>GGZTLSType</code> whoami, <code>GGZTLSVerificationType</code> verify)<br />
 <i>Enable TLS for a file descriptor. </i><br />
 int <code>ggz_tls_disable_fd</code> (int fdes)<br />
 <i>Disable TLS for a file descriptor. </i><br />
 size_t <code>ggz_tls_write</code> (int fd, void *ptr, size_t n)<br />
 <i>Write some bytes to a secured file descriptor. </i><br />
 size_t <code>ggz_tls_read</code> (int fd, void *ptr, size_t n)<br />
 <i>Read from a secured file descriptor. </i></p>
<h2>Detailed Description</h2>
<p> <code>Author:</code></p>
<dl>
<dt>
<dd> Brent M. Hendricks</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
<dd> Fri Nov 2 23:32:17 2001 </p>
<p> <code>Id</code>.RS 4 <code>ggz.h</code>,v 1.59 2005/05/21 10:19:22 josef Exp</dl>
<p> Header file for ggz components lib </p>
<p> Copyright (C) 2001 Brent Hendricks. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place &#8211; Suite 330, Boston, MA 02111-1307, USA</p>
<h2>Define Documentation</h2>
<h3>#define ggz__attribute(att)</h3>
<p> Allow easy use of GCC&#8217;s &#8216;attribute&#8217; macro for debugging. </p>
<p> Under gcc, we use the __attribute__ macro to check variadic arguments, for instance to printf-style functions. Other compilers may be able to do something similar, but this is generally unnecessary since it&#8217;s only realy purpose is to give warning messages when the developer compiles the code.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LibGGZ from the source code. </p>
<h2>Index</h2>
