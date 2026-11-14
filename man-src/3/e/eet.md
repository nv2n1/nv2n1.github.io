---
title: "eet(3)"
name: "eet"
section: "3"
letter: "e"
url: "/docs/linux/man/3-eet/"
description: "Eet.h – The file that provides the eet functions."
---

<p>Eet.h &#8211; The file that provides the eet functions. </p>
<h2>Synopsis</h2>
<h3>Defines</h3>
<p>#define <code>EET_T_UNKNOW</code> 0<br />
 <i>Unknown data encoding type. </i><br />
 #define <code>EET_T_CHAR</code> 1<br />
 <i>Data type: char. </i><br />
 #define <code>EET_T_SHORT</code> 2<br />
 <i>Data type: short. </i><br />
 #define <code>EET_T_INT</code> 3<br />
 <i>Data type: int. </i><br />
 #define <code>EET_T_LONG_LONG</code> 4<br />
 <i>Data type: long long. </i><br />
 #define <code>EET_T_FLOAT</code> 5<br />
 <i>Data type: float. </i><br />
 #define <code>EET_T_DOUBLE</code> 6<br />
 <i>Data type: double. </i><br />
 #define <code>EET_T_UCHAR</code> 7<br />
 <i>Data type: unsigned char. </i><br />
 #define <code>EET_T_USHORT</code> 8<br />
 <i>Data type: unsigned short. </i><br />
 #define <code>EET_T_UINT</code> 9<br />
 <i>Data type: unsigned int. </i><br />
 #define <code>EET_T_ULONG_LONG</code> 10<br />
 <i>Data type: unsigned long long. </i><br />
 #define <code>EET_T_STRING</code> 11<br />
 <i>Data type: char *. </i><br />
 #define <code>EET_T_INLINED_STRING</code> 12<br />
 <i>Data type: char * (but compressed inside the resulting eet). </i><br />
 #define <code>EET_T_LAST</code> 13<br />
 <i>Last data type. </i><br />
 #define <code>EET_G_UNKNOWN</code> 100<br />
 <i>Unknown group data encoding type. </i><br />
 #define <code>EET_G_ARRAY</code> 101<br />
 <i>Fixed size array group type. </i><br />
 #define <code>EET_G_VAR_ARRAY</code> 102<br />
 <i>Variable size array group type. </i><br />
 #define <code>EET_G_LIST</code> 103<br />
 <i>Linked list group type. </i><br />
 #define <code>EET_G_HASH</code> 104<br />
 <i>Hash table group type. </i><br />
 #define <code>EET_G_LAST</code> 105<br />
 <i>Last group type. </i><br />
 #define <code>EET_DATA_DESCRIPTOR_ADD_BASIC</code>(edd, struct_type, name, member, type)<br />
 <i>Add a basic data element to a data descriptor. </i><br />
 #define <code>EET_DATA_DESCRIPTOR_ADD_SUB</code>(edd, struct_type, name, member, subtype)<br />
 <i>Add a sub-element type to a data descriptor. </i><br />
 #define <code>EET_DATA_DESCRIPTOR_ADD_LIST</code>(edd, struct_type, name, member, subtype)<br />
 <i>Add a linked list type to a data descriptor. </i><br />
 #define <code>EET_DATA_DESCRIPTOR_ADD_HASH</code>(edd, struct_type, name, member, subtype)<br />
 <i>Add a hash type to a data descriptor. </i><br />
 #define <code>EET_DATA_DESCRIPTOR_ADD_ARRAY</code>(edd, struct_type, name, member, subtype)<br />
 <i>Add a fixed size array type to a data descriptor. </i><br />
 #define <code>EET_DATA_DESCRIPTOR_ADD_VAR_ARRAY</code>(edd, struct_type, name, member, subtype)<br />
 <i>Add a variable size array type to a data descriptor. </i></p>
<h3>Typedefs</h3>
<p>typedef int(* <code>Eet_Key_Password_Callback</code> )(char *buffer, int size, int rwflag, void *data)<br />
 <i>Callback used to request if needed the password of a private key. </i></p>
<h3>Functions</h3>
<p>EAPI int <code>eet_init</code> (void)<br />
 <i>Initialize the EET library. </i><br />
 EAPI int <code>eet_shutdown</code> (void)<br />
 <i>Shut down the EET library. </i><br />
 EAPI void <code>eet_clearcache</code> (void)<br />
 <i>Clear eet cache. </i><br />
 EAPI Eet_File * <code>eet_open</code> (const char *file, Eet_File_Mode mode)<br />
 <i>Open an eet file on disk, and returns a handle to it. </i><br />
 EAPI Eet_File * <code>eet_memopen_read</code> (const void *data, size_t size)<br />
 <i>Open an eet file directly from a memory location. </i><br />
 EAPI Eet_File_Mode <code>eet_mode_get</code> (Eet_File *ef)<br />
 <i>Get the mode an Eet_File was opened with. </i><br />
 EAPI Eet_Error <code>eet_close</code> (Eet_File *ef)<br />
 <i>Close an eet file handle and flush and writes pending. </i><br />
 EAPI Eet_Key * <code>eet_identity_open</code> (const char *certificate_file, const char *private_key_file, <code>Eet_Key_Password_Callback</code> cb)<br />
 <i>Create an Eet_Key needed for signing an eet file. </i><br />
 EAPI void <code>eet_identity_close</code> (Eet_Key *key)<br />
 <i>Close and release all ressource used by an Eet_Key. </i><br />
 EAPI Eet_Error <code>eet_identity_set</code> (Eet_File *ef, Eet_Key *key)<br />
 <i>Set a key to sign a file. </i><br />
 EAPI void <code>eet_identity_print</code> (Eet_Key *key, FILE *out)<br />
 <i>Display both private and public key of an Eet_Key. </i><br />
 EAPI const void * <code>eet_identity_x509</code> (Eet_File *ef, int *der_length)<br />
 <i>Get the x509 der certificate associated with an Eet_File. </i><br />
 EAPI void <code>eet_identity_certificate_print</code> (const unsigned char *certificate, int der_length, FILE *out)<br />
 <i>Display the x509 der certificate to out. </i><br />
 EAPI Eet_Dictionary * <code>eet_dictionary_get</code> (Eet_File *ef)<br />
 <i>Return a handle to the shared string dictionary of the Eet file. </i><br />
 EAPI int <code>eet_dictionary_string_check</code> (Eet_Dictionary *ed, const char *string)<br />
 <i>Check if a given string comes from a given dictionary. </i><br />
 EAPI void * <code>eet_read</code> (Eet_File *ef, const char *name, int *size_ret)<br />
 <i>Read a specified entry from an eet file and return data. </i><br />
 EAPI const void * <code>eet_read_direct</code> (Eet_File *ef, const char *name, int *size_ret)<br />
 <i>Read a specified entry from an eet file and return data. </i><br />
 EAPI int <code>eet_write</code> (Eet_File *ef, const char *name, const void *data, int size, int compress)<br />
 <i>Write a specified entry to an eet file handle. </i><br />
 EAPI int <code>eet_delete</code> (Eet_File *ef, const char *name)<br />
 <i>Delete a specified entry from an Eet file being written or re-written. </i><br />
 EAPI char ** <code>eet_list</code> (Eet_File *ef, const char *glob, int *count_ret)<br />
 <i>List all entries in eet file matching shell glob. </i><br />
 EAPI int <code>eet_num_entries</code> (Eet_File *ef)<br />
 <i>Return the number of entries in the specified eet file. </i><br />
 EAPI int <code>eet_data_image_header_read</code> (Eet_File *ef, const char *name, unsigned int *w, unsigned int *h, int *alpha, int *compress, int *quality, int *lossy)<br />
 <i>Read just the header data for an image and dont decode the pixels. </i><br />
 EAPI void * <code>eet_data_image_read</code> (Eet_File *ef, const char *name, unsigned int *w, unsigned int *h, int *alpha, int *compress, int *quality, int *lossy)<br />
 <i>Read image data from the named key in the eet file. </i><br />
 EAPI int <code>eet_data_image_read_to_surface</code> (Eet_File *ef, const char *name, unsigned int src_x, unsigned int src_y, unsigned int *d, unsigned int w, unsigned int h, unsigned int row_stride, int *alpha, int *compress, int *quality, int *lossy)<br />
 <i>Read image data from the named key in the eet file. </i><br />
 EAPI int <code>eet_data_image_write</code> (Eet_File *ef, const char *name, const void *data, unsigned int w, unsigned int h, int alpha, int compress, int quality, int lossy)<br />
 <i>Write image data to the named key in an eet file. </i><br />
 EAPI int <code>eet_data_image_header_decode</code> (const void *data, int size, unsigned int *w, unsigned int *h, int *alpha, int *compress, int *quality, int *lossy)<br />
 <i>Decode Image data header only to get information. </i><br />
 EAPI void * <code>eet_data_image_decode</code> (const void *data, int size, unsigned int *w, unsigned int *h, int *alpha, int *compress, int *quality, int *lossy)<br />
 <i>Decode Image data into pixel data. </i><br />
 EAPI int <code>eet_data_image_decode_to_surface</code> (const void *data, int size, unsigned int src_x, unsigned int src_y, unsigned int *d, unsigned int w, unsigned int h, unsigned int row_stride, int *alpha, int *compress, int *quality, int *lossy)<br />
 <i>Decode Image data into pixel data. </i><br />
 EAPI void * <code>eet_data_image_encode</code> (const void *data, int *size_ret, unsigned int w, unsigned int h, int alpha, int compress, int quality, int lossy)<br />
 <i>Encode image data for storage or transmission. </i><br />
 EAPI Eet_Data_Descriptor * <code>eet_data_descriptor_new</code> (const char *name, int size, void *(*func_list_next)(void *l), void *(*func_list_append)(void *l, void *d), void *(*func_list_data)(void *l), void *(*func_list_free)(void *l), void(*func_hash_foreach)(void *h, int(*func)(void *h, const char *k, void *dt, void *fdt), void *fdt), void *(*func_hash_add)(void *h, const char *k, void *d), void(*func_hash_free)(void *h))<br />
 <i>Create a new empty data structure descriptor. </i><br />
 EAPI void <code>eet_data_descriptor_free</code> (Eet_Data_Descriptor *edd)<br />
 <i>This function frees a data descriptor when it is not needed anymore. </i><br />
 EAPI void <code>eet_data_descriptor_element_add</code> (Eet_Data_Descriptor *edd, const char *name, int type, int group_type, int offset, int count, const char *counter_name, Eet_Data_Descriptor *subtype)<br />
 <i>This function is an internal used by macros. </i><br />
 EAPI void * <code>eet_data_read</code> (Eet_File *ef, Eet_Data_Descriptor *edd, const char *name)<br />
 <i>Read a data structure from an eet file and decodes it. </i><br />
 EAPI int <code>eet_data_write</code> (Eet_File *ef, Eet_Data_Descriptor *edd, const char *name, const void *data, int compress)<br />
 <i>Write a data structure from memory and store in an eet file. </i><br />
 EAPI int <code>eet_data_text_dump</code> (const void *data_in, int size_in, void(*dumpfunc)(void *data, const char *str), void *dumpdata)<br />
 <i>Dump an eet encoded data structure into ascii text. </i><br />
 EAPI void * <code>eet_data_text_undump</code> (const char *text, int textlen, int *size_ret)<br />
 <i>Take an ascii encoding from </i><code>eet_data_text_dump()</code> and re-encode in binary.<br />
 EAPI int <code>eet_data_dump</code> (Eet_File *ef, const char *name, void(*dumpfunc)(void *data, const char *str), void *dumpdata)<br />
 <i>Dump an eet encoded data structure from an eet file into ascii text. </i><br />
 EAPI int <code>eet_data_undump</code> (Eet_File *ef, const char *name, const char *text, int textlen, int compress)<br />
 <i>Take an ascii encoding from </i><code>eet_data_dump()</code> and re-encode in binary.<br />
 EAPI void * <code>eet_data_descriptor_decode</code> (Eet_Data_Descriptor *edd, const void *data_in, int size_in)<br />
 <i>Decode a data structure from an arbitary location in memory. </i><br />
 EAPI void * <code>eet_data_descriptor_encode</code> (Eet_Data_Descriptor *edd, const void *data_in, int *size_ret)<br />
 <i>Encode a dsata struct to memory and return that encoded data. </i></p>
<h2>Detailed Description</h2>
<p>The file that provides the eet functions. </p>
<p> This header provides the Eet management functions.</p>
<h2>Define Documentation</h2>
<h3>#define EET_DATA_DESCRIPTOR_ADD_ARRAY(edd, struct_type, name, member, subtype)</h3>
<p><code>Value:</code> </p>
<pre>{ struct_type ___ett; eet_data_descriptor_element_add(edd, name, EET_T_UNKNOW, EET_G_ARRAY, (char *)(&amp;(___ett.member)) - (char *)(&amp;(___ett)), /* 0, */sizeof(___ett.member)/sizeof(___ett.member[0]), NULL, subtype); }</pre>
<p>Add a fixed size array type to a data descriptor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>edd</i> The data descriptor to add the type to.<br />
 <i>struct_type</i> The type of the struct.<br />
 <i>name</i> The string name to use to encode/decode this member (must be a constant global and never change).<br />
 <i>member</i> The struct member itself to be encoded.<br />
 <i>subtype</i> The type of hash member to add.</dl>
<p> This macro lets you easily add a fixed size array of other data types. All the parameters are the same as for <code>EET_DATA_DESCRIPTOR_ADD_BASIC()</code>, with the subtype being the exception. This must be the data descriptor of the element that is in each member of the hash to be stored. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.2</dl>
<h3>#define EET_DATA_DESCRIPTOR_ADD_BASIC(edd, struct_type, name, member, type)</h3>
<p><code>Value:</code> </p>
<pre>{ struct_type ___ett; eet_data_descriptor_element_add(edd, name, type, EET_G_UNKNOWN, (char *)(&amp;(___ett.member)) - (char *)(&amp;(___ett)), 0, /* 0, */NULL, NULL); }</pre>
<p>Add a basic data element to a data descriptor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>edd</i> The data descriptor to add the type to.<br />
 <i>struct_type</i> The type of the struct.<br />
 <i>name</i> The string name to use to encode/decode this member (must be a constant global and never change).<br />
 <i>member</i> The struct member itself to be encoded.<br />
 <i>type</i> The type of the member to encode.</dl>
<p> This macro is a convenience macro provided to add a member to the data descriptor edd. The type of the structure is provided as the struct_type parameter (for example: struct my_struct). The name parameter defines a string that will be used to uniquely name that member of the struct (it is suggested to use the struct member itself). The member parameter is the actual struct member itself (for eet_dictionary_string_check * example: values), and type is the basic data type of the member which must be one of: EET_T_CHAR, EET_T_SHORT, EET_T_INT, EET_T_LONG_LONG, EET_T_FLOAT, EET_T_DOUBLE, EET_T_UCHAR, EET_T_USHORT, EET_T_UINT, EET_T_ULONG_LONG or EET_T_STRING. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>#define EET_DATA_DESCRIPTOR_ADD_HASH(edd, struct_type, name, member, subtype)</h3>
<p><code>Value:</code> </p>
<pre>{ struct_type ___ett; eet_data_descriptor_element_add(edd, name, EET_T_UNKNOW, EET_G_HASH, (char *)(&amp;(___ett.member)) - (char *)(&amp;(___ett)), 0, /* 0, */NULL, subtype); }</pre>
<p>Add a hash type to a data descriptor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>edd</i> The data descriptor to add the type to.<br />
 <i>struct_type</i> The type of the struct.<br />
 <i>name</i> The string name to use to encode/decode this member (must be a constant global and never change).<br />
 <i>member</i> The struct member itself to be encoded.<br />
 <i>subtype</i> The type of hash member to add.</dl>
<p> This macro lets you easily add a hash of other data types. All the parameters are the same as for <code>EET_DATA_DESCRIPTOR_ADD_BASIC()</code>, with the subtype being the exception. This must be the data descriptor of the element that is in each member of the hash to be stored. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>#define EET_DATA_DESCRIPTOR_ADD_LIST(edd, struct_type, name, member, subtype)</h3>
<p><code>Value:</code> </p>
<pre>{ struct_type ___ett; eet_data_descriptor_element_add(edd, name, EET_T_UNKNOW, EET_G_LIST, (char *)(&amp;(___ett.member)) - (char *)(&amp;(___ett)), 0, /* 0, */NULL, subtype); }</pre>
<p>Add a linked list type to a data descriptor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>edd</i> The data descriptor to add the type to.<br />
 <i>struct_type</i> The type of the struct.<br />
 <i>name</i> The string name to use to encode/decode this member (must be a constant global and never change).<br />
 <i>member</i> The struct member itself to be encoded.<br />
 <i>subtype</i> The type of linked list member to add.</dl>
<p> This macro lets you easily add a linked list of other data types. All the parameters are the same as for <code>EET_DATA_DESCRIPTOR_ADD_BASIC()</code>, with the subtype being the exception. This must be the data descriptor of the element that is in each member of the linked list to be stored. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>#define EET_DATA_DESCRIPTOR_ADD_SUB(edd, struct_type, name, member, subtype)</h3>
<p><code>Value:</code> </p>
<pre>{ struct_type ___ett; eet_data_descriptor_element_add(edd, name, EET_T_UNKNOW, EET_G_UNKNOWN, (char *)(&amp;(___ett.member)) - (char *)(&amp;(___ett)), 0, /* 0, */NULL, subtype); }</pre>
<p>Add a sub-element type to a data descriptor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>edd</i> The data descriptor to add the type to.<br />
 <i>struct_type</i> The type of the struct.<br />
 <i>name</i> The string name to use to encode/decode this member (must be a constant global and never change).<br />
 <i>member</i> The struct member itself to be encoded.<br />
 <i>subtype</i> The type of sub-type struct to add.</dl>
<p> This macro lets you easily add a sub-type (a struct that&#8217;s pointed to by this one). All the parameters are the same as for <code>EET_DATA_DESCRIPTOR_ADD_BASIC()</code>, with the subtype being the exception. This must be the data descriptor of the struct that is pointed to by this element. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>#define EET_DATA_DESCRIPTOR_ADD_VAR_ARRAY(edd, struct_type, name, member, subtype)</h3>
<p><code>Value:</code> </p>
<pre>{ struct_type ___ett; eet_data_descriptor_element_add(edd, name, EET_T_UNKNOW, EET_G_VAR_ARRAY, (char *)(&amp;(___ett.member)) - (char *)(&amp;(___ett)), (char *)(&amp;(___ett.member ## _count)) - (char *)(&amp;(___ett)), /* 0, */NULL, subtype); }</pre>
<p>Add a variable size array type to a data descriptor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>edd</i> The data descriptor to add the type to.<br />
 <i>struct_type</i> The type of the struct.<br />
 <i>name</i> The string name to use to encode/decode this member (must be a constant global and never change).<br />
 <i>member</i> The struct member itself to be encoded.<br />
 <i>subtype</i> The type of hash member to add.</dl>
<p> This macro lets you easily add a fixed size array of other data types. All the parameters are the same as for <code>EET_DATA_DESCRIPTOR_ADD_BASIC()</code>, with the subtype being the exception. This must be the data descriptor of the element that is in each member of the hash to be stored. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.2</dl>
<h2>Typedef Documentation</h2>
<h3>typedef int(* <code>Eet_Key_Password_Callback</code>)(char *buffer, int size, int rwflag, void *data)</h3>
<p>Callback used to request if needed the password of a private key. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>2.0.0</dl>
<h2>Function Documentation</h2>
<h3>EAPI void eet_clearcache (void)</h3>
<p>Clear eet cache. </p>
<p> Eet didn&#8217;t free items by default. If you are under memory presure, just call this function to recall all memory that are not yet referenced anymore. The cache take care of modification on disk. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI Eet_Error eet_close (Eet_File * ef)</h3>
<p>Close an eet file handle and flush and writes pending. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ef</i> A valid eet file handle.</dl>
<p> This function will flush any pending writes to disk if the eet file was opened for write, and free all data associated with the file handle and file, and close the file. </p>
<p> If the eet file handle is not valid nothing will be done. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI void* eet_data_descriptor_decode (Eet_Data_Descriptor * edd, const void * data_in, int size_in)</h3>
<p>Decode a data structure from an arbitary location in memory. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>edd</i> The data descriptor to use when decoding.<br />
 <i>data_in</i> The pointer to the data to decode into a struct.<br />
 <i>size_in</i> The size of the data pointed to in bytes.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>NULL on failure, or a valid decoded struct pointer on success.</dl>
<p> This function will decode a data structure that has been encoded using <code>eet_data_descriptor_encode()</code>, and return a data structure with all its elements filled out, if successful, or NULL on failure. </p>
<p> The data to be decoded is stored at the memory pointed to by data_in, and is described by the descriptor pointed to by edd. The data size is passed in as the value to size_in, ande must be greater than 0 to succeed. </p>
<p> This function is useful for decoding data structures delivered to the application by means other than an eet file, such as an IPC or socket connection, raw files, shared memory etc. </p>
<p> Please see <code>eet_data_read()</code> for more information. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI void eet_data_descriptor_element_add (Eet_Data_Descriptor * edd, const char * name, int type, int group_type, int offset, int count, const char * counter_name, Eet_Data_Descriptor * subtype)</h3>
<p>This function is an internal used by macros. </p>
<p> This function is used by macros <code>EET_DATA_DESCRIPTOR_ADD_BASIC()</code>, <code>EET_DATA_DESCRIPTOR_ADD_SUB()</code> and <code>EET_DATA_DESCRIPTOR_ADD_LIST()</code>. It is complex to use by hand and should be left to be used by the macros, and thus is not documented. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI void* eet_data_descriptor_encode (Eet_Data_Descriptor * edd, const void * data_in, int * size_ret)</h3>
<p>Encode a dsata struct to memory and return that encoded data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>edd</i> The data descriptor to use when encoding.<br />
 <i>data_in</i> The pointer to the struct to encode into data.<br />
 <i>size_ret</i> A pointer to the an int to be filled with the decoded size.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>NULL on failure, or a valid encoded data chunk on success.</dl>
<p> This function takes a data structutre in memory and encodes it into a serialised chunk of data that can be decoded again by <code>eet_data_descriptor_decode()</code>. This is useful for being able to transmit data structures across sockets, pipes, IPC or shared file mechanisms, without having to worry about memory space, machine type, endianess etc. </p>
<p> The parameter edd must point to a valid data descriptor, and data_in must point to the right data structure to encode. If not, the encoding may fail. </p>
<p> On success a non NULL valid pointer is returned and what size_ret points to is set to the size of this decoded data, in bytes. When the encoded data is no longer needed, call free() on it. On failure NULL is returned and what size_ret points to is set to 0. </p>
<p> Please see <code>eet_data_write()</code> for more information. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI void eet_data_descriptor_free (Eet_Data_Descriptor * edd)</h3>
<p>This function frees a data descriptor when it is not needed anymore. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>edd</i> The data descriptor to free.</dl>
<p> This function takes a data descriptor handle as a parameter and frees all data allocated for the data descriptor and the handle itself. After this call the descriptor is no longer valid. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI Eet_Data_Descriptor* eet_data_descriptor_new (const char * name, int size, void *(*)(void *l) func_list_next, void *(*)(void *l, void *d) func_list_append, void *(*)(void *l) func_list_data, void *(*)(void *l) func_list_free, void(*)(void *h, int(*func)(void *h, const char *k, void *dt, void *fdt), void *fdt) func_hash_foreach, void *(*)(void *h, const char *k, void *d) func_hash_add, void(*)(void *h) func_hash_free)</h3>
<p>Create a new empty data structure descriptor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> The string name of this data structure (most be a global constant and never change).<br />
 <i>size</i> The size of the struct (in bytes).<br />
 <i>func_list_next</i> The function to get the next list node.<br />
 <i>func_list_append</i> The function to append a member to a list.<br />
 <i>func_list_data</i> The function to get the data from a list node.<br />
 <i>func_list_free</i> The function to free an entire linked list.<br />
 <i>func_hash_foreach</i> The function to iterate through all hash table entries.<br />
 <i>func_hash_add</i> The function to add a member to a hash table.<br />
 <i>func_hash_free</i> The function to free an entire hash table.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new empty data descriptor.</dl>
<p> This function creates a new data descriptore and returns a handle to the new data descriptor. On creation it will be empty, containing no contents describing anything other than the shell of the data structure. </p>
<p> You add structure members to the data descriptor using the macros <code>EET_DATA_DESCRIPTOR_ADD_BASIC()</code>, <code>EET_DATA_DESCRIPTOR_ADD_SUB()</code> and <code>EET_DATA_DESCRIPTOR_ADD_LIST()</code>, depending on what type of member you are adding to the description. </p>
<p> Once you have described all the members of a struct you want loaded, or saved eet can load and save those members for you, encode them into endian-independant serialised data chunks for transmission across a a network or more. </p>
<p> The function pointers to the list and hash table functions are only needed if you use those data types, else you can pass NULL instead. </p>
<p> Example: </p>
<pre> #include &lt;<a href="file:/usr/include/Eet.h">Eet.h</a>&gt;
 #include &lt;<a href="file:/usr/include/Evas.h">Evas.h</a>&gt;
 typedef struct _blah2
 {
 char *string;
 }
 Blah2;
 typedef struct _blah3
 {
 char *string;
 }
 Blah3;
 typedef struct _blah
 {
 char character;
 short sixteen;
 int integer;
 long long lots;
 float floating;
 double floating_lots;
 char *string;
 Blah2 *blah2;
 Evas_List *blah3;
 }
 Blah;
 int
 main(int argc, char **argv)
 {
 Blah blah;
 Blah2 blah2;
 Blah3 blah3;
 Eet_Data_Descriptor *edd, *edd2, *edd3;
 void *data;
 int size;
 FILE *f;
 Blah *blah_in;
 edd3 = eet_data_descriptor_new('blah3', sizeof(Blah3),
 evas_list_next,
 evas_list_append,
 evas_list_data,
 evas_list_free,
 evas_hash_foreach,
 evas_hash_add,
 evas_hash_free);
 EET_DATA_DESCRIPTOR_ADD_BASIC(edd3, Blah3, 'string3', string, EET_T_STRING);
 edd2 = eet_data_descriptor_new('blah2', sizeof(Blah2),
 evas_list_next,
 evas_list_append,
 evas_list_data,
 evas_list_free,
 evas_hash_foreach,
 evas_hash_add,
 evas_hash_free);
 EET_DATA_DESCRIPTOR_ADD_BASIC(edd2, Blah2, 'string2', string, EET_T_STRING);
 edd = eet_data_descriptor_new('blah', sizeof(Blah),
 evas_list_next,
 evas_list_append,
 evas_list_data,
 evas_list_free,
 evas_hash_foreach,
 evas_hash_add,
 evas_hash_free);
 EET_DATA_DESCRIPTOR_ADD_BASIC(edd, Blah, 'character', character, EET_T_CHAR);
 EET_DATA_DESCRIPTOR_ADD_BASIC(edd, Blah, 'sixteen', sixteen, EET_T_SHORT);
 EET_DATA_DESCRIPTOR_ADD_BASIC(edd, Blah, 'integer', integer, EET_T_INT);
 EET_DATA_DESCRIPTOR_ADD_BASIC(edd, Blah, 'lots', lots, EET_T_LONG_LONG);
 EET_DATA_DESCRIPTOR_ADD_BASIC(edd, Blah, 'floating', floating, EET_T_FLOAT);
 EET_DATA_DESCRIPTOR_ADD_BASIC(edd, Blah, 'floating_lots', floating_lots, EET_T_DOUBLE);
 EET_DATA_DESCRIPTOR_ADD_BASIC(edd, Blah, 'string', string, EET_T_STRING);
 EET_DATA_DESCRIPTOR_ADD_SUB(edd, Blah, 'blah2', blah2, edd2);
 EET_DATA_DESCRIPTOR_ADD_LIST(edd, Blah, 'blah3', blah3, edd3);
 blah3.string='PANTS';
 blah2.string='subtype string here!';
 blah.character='7';
 blah.sixteen=0x7777;
 blah.integer=0xc0def00d;
 blah.lots=0xdeadbeef31337777;
 blah.floating=3.141592654;
 blah.floating_lots=0.777777777777777;
 blah.string='bite me like a turnip';
 blah.blah2 = &amp;blah2;
 blah.blah3 = evas_list_append(NULL, &amp;blah3);
 blah.blah3 = evas_list_append(blah.blah3, &amp;blah3);
 blah.blah3 = evas_list_append(blah.blah3, &amp;blah3);
 blah.blah3 = evas_list_append(blah.blah3, &amp;blah3);
 blah.blah3 = evas_list_append(blah.blah3, &amp;blah3);
 blah.blah3 = evas_list_append(blah.blah3, &amp;blah3);
 blah.blah3 = evas_list_append(blah.blah3, &amp;blah3);
 data = eet_data_descriptor_encode(edd, &amp;blah, &amp;size);
 printf('-----DECODING);
 blah_in = eet_data_descriptor_decode(edd, data, size);
 printf('-----DECODED!);
 printf('%c, blah_in-&gt;character);
 printf('%x, (int)blah_in-&gt;sixteen);
 printf('%x, blah_in-&gt;integer);
 printf('%lx, blah_in-&gt;lots);
 printf('%f, (double)blah_in-&gt;floating);
 printf('%f, (double)blah_in-&gt;floating_lots);
 printf('%s, blah_in-&gt;string);
 printf('%p, blah_in-&gt;blah2);
 printf(' %s, blah_in-&gt;blah2-&gt;string);
 {
 Evas_List *l;
 for (l = blah_in-&gt;blah3; l; l = l-&gt;next)
 {
 Blah3 *blah3_in;
 blah3_in = l-&gt;data;
 printf('%p, blah3_in);
 printf(' %s, blah3_in-&gt;string);
 }
 }
 eet_data_descriptor_free(edd);
 eet_data_descriptor_free(edd2);
 eet_data_descriptor_free(edd3);
 return 0;
 }</pre>
<p><code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI int eet_data_dump (Eet_File * ef, const char * name, void(*)(void *data, const char *str) dumpfunc, void * dumpdata)</h3>
<p>Dump an eet encoded data structure from an eet file into ascii text. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ef</i> A valid eet file handle.<br />
 <i>name</i> Name of the entry. eg: &#8216;/base/file_i_want&#8217;.<br />
 <i>dumpfunc</i> The function to call passed a string when new data is converted to text<br />
 <i>dumpdata</i> The data to pass to the dumpfunc callback.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure</dl>
<p> This function will take an open and valid eet file from <code>eet_open()</code> request the data encoded by <code>eet_data_descriptor_encode()</code> corresponding to the key name and convert it into human readable ascii text. It does this by calling the dumpfunc callback for all new text that is generated. This callback should append to any existing text buffer and will be passed the pointer dumpdata as a parameter as well as a string with new text to be appended. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI void* eet_data_image_decode (const void * data, int size, unsigned int * w, unsigned int * h, int * alpha, int * compress, int * quality, int * lossy)</h3>
<p>Decode Image data into pixel data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> The encoded pixel data.<br />
 <i>size</i> The size, in bytes, of the encoded pixel data.<br />
 <i>w</i> A pointer to the unsigned int to hold the width in pixels.<br />
 <i>h</i> A pointer to the unsigned int to hold the height in pixels.<br />
 <i>alpha</i> A pointer to the int to hold the alpha flag.<br />
 <i>compress</i> A pointer to the int to hold the compression amount.<br />
 <i>quality</i> A pointer to the int to hold the quality amount.<br />
 <i>lossy</i> A pointer to the int to hold the lossiness flag.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The image pixel data decoded</dl>
<p> This function takes encoded pixel data and decodes it into raw RGBA pixels on success. </p>
<p> The other parameters of the image (width, height etc.) are placed into the values pointed to (they must be supplied). The pixel data is a linear array of pixels starting from the top-left of the image scanning row by row from left to right. Each pixel is a 32bit value, with the high byte being the alpha channel, the next being red, then green, and the low byte being blue. The width and height are measured in pixels and will be greater than 0 when returned. The alpha flag is either 0 or 1. 0 denotes that the alpha channel is not used. 1 denotes that it is significant. Compress is filled with the compression value/amount the image was stored with. The quality value is filled with the quality encoding of the image file (0 &#8211; 100). The lossy flags is either 0 or 1 as to if the image was encoded lossily or not. </p>
<p> On success the function returns a pointer to the image data decoded. The calling application is responsible for calling free() on the image data when it is done with it. On failure NULL is returned and the parameter values may not contain any sensible data. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI int eet_data_image_decode_to_surface (const void * data, int size, unsigned int src_x, unsigned int src_y, unsigned int * d, unsigned int w, unsigned int h, unsigned int row_stride, int * alpha, int * compress, int * quality, int * lossy)</h3>
<p>Decode Image data into pixel data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> The encoded pixel data.<br />
 <i>size</i> The size, in bytes, of the encoded pixel data.<br />
 <i>src_x</i> The starting x coordinate from where to dump the stream.<br />
 <i>src_y</i> The starting y coordinate from where to dump the stream.<br />
 <i>d</i> A pointer to the pixel surface.<br />
 <i>w</i> The expected width in pixels of the pixel surface to decode.<br />
 <i>h</i> The expected height in pixels of the pixel surface to decode.<br />
 <i>row_stride</i> The length of a pixels line in the destination surface.<br />
 <i>alpha</i> A pointer to the int to hold the alpha flag.<br />
 <i>compress</i> A pointer to the int to hold the compression amount.<br />
 <i>quality</i> A pointer to the int to hold the quality amount.<br />
 <i>lossy</i> A pointer to the int to hold the lossiness flag.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> This function takes encoded pixel data and decodes it into raw RGBA pixels on success. </p>
<p> The other parameters of the image (alpha, compress etc.) are placed into the values pointed to (they must be supplied). The pixel data is a linear array of pixels starting from the top-left of the image scanning row by row from left to right. Each pixel is a 32bit value, with the high byte being the alpha channel, the next being red, then green, and the low byte being blue. The width and height are measured in pixels and will be greater than 0 when returned. The alpha flag is either 0 or 1. 0 denotes that the alpha channel is not used. 1 denotes that it is significant. Compress is filled with the compression value/amount the image was stored with. The quality value is filled with the quality encoding of the image file (0 &#8211; 100). The lossy flags is either 0 or 1 as to if the image was encoded lossily or not. </p>
<p> On success the function returns 1, and 0 on failure. On failure the parameter values may not contain any sensible data. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.2</dl>
<h3>EAPI void* eet_data_image_encode (const void * data, int * size_ret, unsigned int w, unsigned int h, int alpha, int compress, int quality, int lossy)</h3>
<p>Encode image data for storage or transmission. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> A pointer to the image pixel data.<br />
 <i>size_ret</i> A pointer to an int to hold the size of the returned data.<br />
 <i>w</i> The width of the image in pixels.<br />
 <i>h</i> The height of the image in pixels.<br />
 <i>alpha</i> The alpha channel flag.<br />
 <i>compress</i> The compression amount.<br />
 <i>quality</i> The quality encoding amount.<br />
 <i>lossy</i> The lossiness flag.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The encoded image data.</dl>
<p> This function stakes image pixel data and encodes it with compression and possible loss of quality (as a trade off for size) for storage or transmission to another system. </p>
<p> The data expected is the same format as returned by eet_data_image_read. If this is not the case weird things may happen. Width and height must be between 1 and 8000 pixels. The alpha flags can be 0 or 1 (0 meaning the alpha values are not useful and 1 meaning they are). Compress can be from 0 to 9 (0 meaning no compression, 9 meaning full compression). This is only used if the image is not lossily encoded. Quality is used on lossy compression and should be a value from 0 to 100. The lossy flag can be 0 or 1. 0 means encode losslessly and 1 means to encode with image quality loss (but then have a much smaller encoding). </p>
<p> On success this function returns a pointer to the encoded data that you can free with free() when no longer needed. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI int eet_data_image_header_decode (const void * data, int size, unsigned int * w, unsigned int * h, int * alpha, int * compress, int * quality, int * lossy)</h3>
<p>Decode Image data header only to get information. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> The encoded pixel data.<br />
 <i>size</i> The size, in bytes, of the encoded pixel data.<br />
 <i>w</i> A pointer to the unsigned int to hold the width in pixels.<br />
 <i>h</i> A pointer to the unsigned int to hold the height in pixels.<br />
 <i>alpha</i> A pointer to the int to hold the alpha flag.<br />
 <i>compress</i> A pointer to the int to hold the compression amount.<br />
 <i>quality</i> A pointer to the int to hold the quality amount.<br />
 <i>lossy</i> A pointer to the int to hold the lossiness flag.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure.</dl>
<p> This function takes encoded pixel data and decodes it into raw RGBA pixels on success. </p>
<p> The other parameters of the image (width, height etc.) are placed into the values pointed to (they must be supplied). The pixel data is a linear array of pixels starting from the top-left of the image scanning row by row from left to right. Each pixel is a 32bit value, with the high byte being the alpha channel, the next being red, then green, and the low byte being blue. The width and height are measured in pixels and will be greater than 0 when returned. The alpha flag is either 0 or 1. 0 denotes that the alpha channel is not used. 1 denotes that it is significant. Compress is filled with the compression value/amount the image was stored with. The quality value is filled with the quality encoding of the image file (0 &#8211; 100). The lossy flags is either 0 or 1 as to if the image was encoded lossily or not. </p>
<p> On success the function returns 1 indicating the header was read and decoded properly, or 0 on failure. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI int eet_data_image_header_read (Eet_File * ef, const char * name, unsigned int * w, unsigned int * h, int * alpha, int * compress, int * quality, int * lossy)</h3>
<p>Read just the header data for an image and dont decode the pixels. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ef</i> A valid eet file handle opened for reading.<br />
 <i>name</i> Name of the entry. eg: &#8216;/base/file_i_want&#8217;.<br />
 <i>w</i> A pointer to the unsigned int to hold the width in pixels.<br />
 <i>h</i> A pointer to the unsigned int to hold the height in pixels.<br />
 <i>alpha</i> A pointer to the int to hold the alpha flag.<br />
 <i>compress</i> A pointer to the int to hold the compression amount.<br />
 <i>quality</i> A pointer to the int to hold the quality amount.<br />
 <i>lossy</i> A pointer to the int to hold the lossiness flag.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on successfull decode, 0 otherwise</dl>
<p> This function reads an image from an eet file stored under the named key in the eet file and return a pointer to the decompressed pixel data. </p>
<p> The other parameters of the image (width, height etc.) are placed into the values pointed to (they must be supplied). The pixel data is a linear array of pixels starting from the top-left of the image scanning row by row from left to right. Each pile is a 32bit value, with the high byte being the alpha channel, the next being red, then green, and the low byte being blue. The width and height are measured in pixels and will be greater than 0 when returned. The alpha flag is either 0 or 1. 0 denotes that the alpha channel is not used. 1 denotes that it is significant. Compress is filled with the compression value/amount the image was stored with. The quality value is filled with the quality encoding of the image file (0 &#8211; 100). The lossy flags is either 0 or 1 as to if the image was encoded lossily or not. </p>
<p> On success the function returns 1 indicating the header was read and decoded properly, or 0 on failure. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI void* eet_data_image_read (Eet_File * ef, const char * name, unsigned int * w, unsigned int * h, int * alpha, int * compress, int * quality, int * lossy)</h3>
<p>Read image data from the named key in the eet file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ef</i> A valid eet file handle opened for reading.<br />
 <i>name</i> Name of the entry. eg: &#8216;/base/file_i_want&#8217;.<br />
 <i>w</i> A pointer to the unsigned int to hold the width in pixels.<br />
 <i>h</i> A pointer to the unsigned int to hold the height in pixels.<br />
 <i>alpha</i> A pointer to the int to hold the alpha flag.<br />
 <i>compress</i> A pointer to the int to hold the compression amount.<br />
 <i>quality</i> A pointer to the int to hold the quality amount.<br />
 <i>lossy</i> A pointer to the int to hold the lossiness flag.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The image pixel data decoded</dl>
<p> This function reads an image from an eet file stored under the named key in the eet file and return a pointer to the decompressed pixel data. </p>
<p> The other parameters of the image (width, height etc.) are placed into the values pointed to (they must be supplied). The pixel data is a linear array of pixels starting from the top-left of the image scanning row by row from left to right. Each pile is a 32bit value, with the high byte being the alpha channel, the next being red, then green, and the low byte being blue. The width and height are measured in pixels and will be greater than 0 when returned. The alpha flag is either 0 or 1. 0 denotes that the alpha channel is not used. 1 denotes that it is significant. Compress is filled with the compression value/amount the image was stored with. The quality value is filled with the quality encoding of the image file (0 &#8211; 100). The lossy flags is either 0 or 1 as to if the image was encoded lossily or not. </p>
<p> On success the function returns a pointer to the image data decoded. The calling application is responsible for calling free() on the image data when it is done with it. On failure NULL is returned and the parameter values may not contain any sensible data. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI int eet_data_image_read_to_surface (Eet_File * ef, const char * name, unsigned int src_x, unsigned int src_y, unsigned int * d, unsigned int w, unsigned int h, unsigned int row_stride, int * alpha, int * compress, int * quality, int * lossy)</h3>
<p>Read image data from the named key in the eet file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ef</i> A valid eet file handle opened for reading.<br />
 <i>name</i> Name of the entry. eg: &#8216;/base/file_i_want&#8217;.<br />
 <i>src_x</i> The starting x coordinate from where to dump the stream.<br />
 <i>src_y</i> The starting y coordinate from where to dump the stream.<br />
 <i>d</i> A pointer to the pixel surface.<br />
 <i>w</i> The expected width in pixels of the pixel surface to decode.<br />
 <i>h</i> The expected height in pixels of the pixel surface to decode.<br />
 <i>row_stride</i> The length of a pixels line in the destination surface.<br />
 <i>alpha</i> A pointer to the int to hold the alpha flag.<br />
 <i>compress</i> A pointer to the int to hold the compression amount.<br />
 <i>quality</i> A pointer to the int to hold the quality amount.<br />
 <i>lossy</i> A pointer to the int to hold the lossiness flag.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> This function reads an image from an eet file stored under the named key in the eet file and return a pointer to the decompressed pixel data. </p>
<p> The other parameters of the image (width, height etc.) are placed into the values pointed to (they must be supplied). The pixel data is a linear array of pixels starting from the top-left of the image scanning row by row from left to right. Each pile is a 32bit value, with the high byte being the alpha channel, the next being red, then green, and the low byte being blue. The width and height are measured in pixels and will be greater than 0 when returned. The alpha flag is either 0 or 1. 0 denotes that the alpha channel is not used. 1 denotes that it is significant. Compress is filled with the compression value/amount the image was stored with. The quality value is filled with the quality encoding of the image file (0 &#8211; 100). The lossy flags is either 0 or 1 as to if the image was encoded lossily or not. </p>
<p> On success the function returns 1, and 0 on failure. On failure the parameter values may not contain any sensible data. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.2</dl>
<h3>EAPI int eet_data_image_write (Eet_File * ef, const char * name, const void * data, unsigned int w, unsigned int h, int alpha, int compress, int quality, int lossy)</h3>
<p>Write image data to the named key in an eet file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ef</i> A valid eet file handle opened for writing.<br />
 <i>name</i> Name of the entry. eg: &#8216;/base/file_i_want&#8217;.<br />
 <i>data</i> A pointer to the image pixel data.<br />
 <i>w</i> The width of the image in pixels.<br />
 <i>h</i> The height of the image in pixels.<br />
 <i>alpha</i> The alpha channel flag.<br />
 <i>compress</i> The compression amount.<br />
 <i>quality</i> The quality encoding amount.<br />
 <i>lossy</i> The lossiness flag.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Success if the data was encoded and written or not.</dl>
<p> This function takes image pixel data and encodes it in an eet file stored under the supplied name key, and returns how many bytes were actually written to encode the image data. </p>
<p> The data expected is the same format as returned by eet_data_image_read. If this is not the case weird things may happen. Width and height must be between 1 and 8000 pixels. The alpha flags can be 0 or 1 (0 meaning the alpha values are not useful and 1 meaning they are). Compress can be from 0 to 9 (0 meaning no compression, 9 meaning full compression). This is only used if the image is not lossily encoded. Quality is used on lossy compression and should be a value from 0 to 100. The lossy flag can be 0 or 1. 0 means encode losslessly and 1 means to encode with image quality loss (but then have a much smaller encoding). </p>
<p> On success this function returns the number of bytes that were required to encode the image data, or on failure it returns 0. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI void* eet_data_read (Eet_File * ef, Eet_Data_Descriptor * edd, const char * name)</h3>
<p>Read a data structure from an eet file and decodes it. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ef</i> The eet file handle to read from.<br />
 <i>edd</i> The data descriptor handle to use when decoding.<br />
 <i>name</i> The key the data is stored under in the eet file.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to the decoded data structure.</dl>
<p> This function decodes a data structure stored in an eet file, returning a pointer to it if it decoded successfully, or NULL on failure. This can save a programmer dozens of hours of work in writing configuration file parsing and writing code, as eet does all that work for the program and presents a program-friendly data structure, just as the programmer likes. Eet can handle members being added or deleted from the data in storage and safely zero-fills unfilled members if they were not found in the data. It checks sizes and headers whenever it reads data, allowing the programmer to not worry about corrupt data. </p>
<p> Once a data structure has been described by the programmer with the fields they wish to save or load, storing or retrieving a data structure from an eet file, or from a chunk of memory is as simple as a single function call. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI int eet_data_text_dump (const void * data_in, int size_in, void(*)(void *data, const char *str) dumpfunc, void * dumpdata)</h3>
<p>Dump an eet encoded data structure into ascii text. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data_in</i> The pointer to the data to decode into a struct.<br />
 <i>size_in</i> The size of the data pointed to in bytes.<br />
 <i>dumpfunc</i> The function to call passed a string when new data is converted to text<br />
 <i>dumpdata</i> The data to pass to the dumpfunc callback.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure</dl>
<p> This function will take a chunk of data encoded by <code>eet_data_descriptor_encode()</code> and convert it into human readable ascii text. It does this by calling the dumpfunc callback for all new text that is generated. This callback should append to any existing text buffer and will be passed the pointer dumpdata as a parameter as well as a string with new text to be appended. </p>
<p> Example: </p>
<pre> void output(void *data, const char *string)
 {
 printf('%s', string);
 }
 void dump(const char *file)
 {
 FILE *f;
 int len;
 void *data;
 f = fopen(file, 'r');
 fseek(f, 0, SEEK_END);
 len = ftell(f);
 rewind(f);
 data = malloc(len);
 fread(data, len, 1, f);
 fclose(f);
 eet_data_text_dump(data, len, output, NULL);
 }</pre>
<p><code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI void* eet_data_text_undump (const char * text, int textlen, int * size_ret)</h3>
<p>Take an ascii encoding from <code>eet_data_text_dump()</code> and re-encode in binary. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>text</i> The pointer to the string data to parse and encode.<br />
 <i>textlen</i> The size of the string in bytes (not including 0 byte terminator).<br />
 <i>size_ret</i> This gets filled in with the encoded data blob size in bytes.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The encoded data on success, NULL on failure.</dl>
<p> This function will parse the string pointed to by text and return an encoded data lump the same way <code>eet_data_descriptor_encode()</code> takes an in-memory data struct and encodes into a binary blob. text is a normal C string. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI int eet_data_undump (Eet_File * ef, const char * name, const char * text, int textlen, int compress)</h3>
<p>Take an ascii encoding from <code>eet_data_dump()</code> and re-encode in binary. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ef</i> A valid eet file handle.<br />
 <i>name</i> Name of the entry. eg: &#8216;/base/file_i_want&#8217;.<br />
 <i>text</i> The pointer to the string data to parse and encode.<br />
 <i>textlen</i> The size of the string in bytes (not including 0 byte terminator).<br />
 <i>compress</i> Compression flags (1 == compress, 0 = don&#8217;t compress).</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 on failure</dl>
<p> This function will parse the string pointed to by text, encode it the same way <code>eet_data_descriptor_encode()</code> takes an in-memory data struct and encodes into a binary blob. </p>
<p> The data (optionally compressed) will be in ram, pending a flush to disk (it will stay in ram till the eet file handle is closed though). </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI int eet_data_write (Eet_File * ef, Eet_Data_Descriptor * edd, const char * name, const void * data, int compress)</h3>
<p>Write a data structure from memory and store in an eet file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ef</i> The eet file handle to write to.<br />
 <i>edd</i> The data descriptor to use when encoding.<br />
 <i>name</i> The key to store the data under in the eet file.<br />
 <i>data</i> A pointer to the data structure to ssave and encode.<br />
 <i>compress</i> Compression flags for storage.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on successful write, 0 on failure.</dl>
<p> This function is the reverse of <code>eet_data_read()</code>, saving a data structure to an eet file. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI int eet_delete (Eet_File * ef, const char * name)</h3>
<p>Delete a specified entry from an Eet file being written or re-written. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ef</i> A valid eet file handle opened for writing.<br />
 <i>name</i> Name of the entry. eg: &#8216;/base/file_i_want&#8217;.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Success or failure of the delete.</dl>
<p> This function will delete the specified chunk of data from the eet file and return greater than 0 on success. 0 will be returned on failure. </p>
<p> The eet file handle must be a valid file handle for an eet file opened for writing. If it is not, 0 will be returned and no action will be performed. </p>
<p> Name, must not be NULL, otherwise 0 will be returned. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI Eet_Dictionary* eet_dictionary_get (Eet_File * ef)</h3>
<p>Return a handle to the shared string dictionary of the Eet file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ef</i> A valid eet file handle.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A handle to the dictionary of the file</dl>
<p> This function returns a handle to the dictionary of an Eet file whose handle is ef, if a dictionary exists. NULL is returned otherwise or if the file handle is known to be invalid. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI int eet_dictionary_string_check (Eet_Dictionary * ed, const char * string)</h3>
<p>Check if a given string comes from a given dictionary. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ed</i> A valid dictionary handle<br />
 <i>string</i> A valid 0 byte terminated C string</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if it is in the dictionary, 0 otherwise</dl>
<p> This checks the given dictionary to see if the given string is actually inside that dictionary (i.e. comes from it) and returns 1 if it does. If the dictionary handle is invlide, the string is NULL or the string is not in the dictionary, 0 is returned. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI void eet_identity_certificate_print (const unsigned char * certificate, int der_length, FILE * out)</h3>
<p>Display the x509 der certificate to out. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>2.0.0</dl>
<h3>EAPI void eet_identity_close (Eet_Key * key)</h3>
<p>Close and release all ressource used by an Eet_Key. </p>
<p> An reference counter prevent it from being freed until all file using it are also closed. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>2.0.0</dl>
<h3>EAPI Eet_Key* eet_identity_open (const char * certificate_file, const char * private_key_file, <code>Eet_Key_Password_Callback</code> cb)</h3>
<p>Create an Eet_Key needed for signing an eet file. </p>
<p> The certificate should provide the public that match the private key. No verification is done to ensure that. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>2.0.0</dl>
<h3>EAPI void eet_identity_print (Eet_Key * key, FILE * out)</h3>
<p>Display both private and public key of an Eet_Key. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>2.0.0</dl>
<h3>EAPI Eet_Error eet_identity_set (Eet_File * ef, Eet_Key * key)</h3>
<p>Set a key to sign a file. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>2.0.0</dl>
<h3>EAPI const void* eet_identity_x509 (Eet_File * ef, int * der_length)</h3>
<p>Get the x509 der certificate associated with an Eet_File. </p>
<p> Will return NULL if the file is not signed. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>2.0.0</dl>
<h3>EAPI int eet_init (void)</h3>
<p>Initialize the EET library. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The new init count.</dl>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI char** eet_list (Eet_File * ef, const char * glob, int * count_ret)</h3>
<p>List all entries in eet file matching shell glob. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ef</i> A valid eet file handle.<br />
 <i>glob</i> A shell glob to match against.<br />
 <i>count_ret</i> Number of entries found to match.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Pointer to an array of strings.</dl>
<p> This function will list all entries in the eet file matching the supplied shell glob and return an allocated list of their names, if there are any, and if no memory errors occur. </p>
<p> The eet file handle must be valid and glob must not be NULL, or NULL will be returned and count_ret will be filled with 0. </p>
<p> The calling program must call free() on the array returned, but NOT on the string pointers in the array. They are taken as read-only internals from the eet file handle. They are only valid as long as the file handle is not closed. When it is closed those pointers in the array are now not valid and should not be used. </p>
<p> On success the array returned will have a list of string pointers that are the names of the entries that matched, and count_ret will have the number of entries in this array placed in it. </p>
<p> Hint: an easy way to list all entries in an eet file is to use a glob value of &#8216;*&#8217;. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI Eet_File* eet_memopen_read (const void * data, size_t size)</h3>
<p>Open an eet file directly from a memory location. </p>
<p> The data are not copied, so you must keep them around as long as the eet file is open. Their is currently no cache for this kind of Eet_File, so it&#8217;s reopen every time you do use eet_memopen_read. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>2.0.0</dl>
<h3>EAPI Eet_File_Mode eet_mode_get (Eet_File * ef)</h3>
<p>Get the mode an Eet_File was opened with. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ef</i> A valid eet file handle.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The mode ef was opened with.</dl>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI int eet_num_entries (Eet_File * ef)</h3>
<p>Return the number of entries in the specified eet file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ef</i> A valid eet file handle.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Number of entries in ef or -1 if the number of entries cannot be read due to open mode restrictions.</dl>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI Eet_File* eet_open (const char * file, Eet_File_Mode mode)</h3>
<p>Open an eet file on disk, and returns a handle to it. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>file</i> The file path to the eet file. eg: &#8216;/tmp/file.eet&#8217;.<br />
 <i>mode</i> The mode for opening. Either EET_FILE_MODE_READ, EET_FILE_MODE_WRITE or EET_FILE_MODE_READ_WRITE.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An opened eet file handle.</dl>
<p> This function will open an exiting eet file for reading, and build the directory table in memory and return a handle to the file, if it exists and can be read, and no memory errors occur on the way, otherwise NULL will be returned. </p>
<p> It will also open an eet file for writing. This will, if successful, delete the original file and replace it with a new empty file, till the eet file handle is closed or flushed. If it cannot be opened for writing or a memory error occurs, NULL is returned. </p>
<p> You can also open the file for read/write. If you then write a key that does not exist it will be created, if the key exists it will be replaced by the new data. </p>
<p> Example: </p>
<pre> #include &lt;<a href="file:/usr/include/Eet.h">Eet.h</a>&gt;
 #include &lt;<a href="file:/usr/include/stdio.h">stdio.h</a>&gt;
 int
 main(int argc, char **argv)
 {
 Eet_File *ef;
 char buf[1024], *ret, **list;
 int size, num, i;
 strcpy(buf, 'Here is a string of data to save!');
 ef = eet_open('/tmp/my_file.eet', EET_FILE_MODE_WRITE);
 if (!ef) return -1;
 if (!eet_write(ef, '/key/to_store/at', buf, 1024, 1))
 fprintf(stderr, 'Error writing data!);
 eet_close(ef);
 ef = eet_open('/tmp/my_file.eet', EET_FILE_MODE_READ);
 if (!ef) return -1;
 list = eet_list(ef, '*', &amp;num);
 if (list)
 {
 for (i = 0; i &lt; num; i++)
 printf('Key stored: %s, list[i]);
 free(list);
 }
 ret = eet_read(ef, '/key/to_store/at', &amp;size);
 if (ret)
 {
 printf('Data read (%i bytes):s, size, ret);
 free(ret);
 }
 eet_close(ef);
 return 0;
 }</pre>
<p><code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI void* eet_read (Eet_File * ef, const char * name, int * size_ret)</h3>
<p>Read a specified entry from an eet file and return data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ef</i> A valid eet file handle opened for reading.<br />
 <i>name</i> Name of the entry. eg: &#8216;/base/file_i_want&#8217;.<br />
 <i>size_ret</i> Number of bytes read from entry and returned.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data stored in that entry in the eet file.</dl>
<p> This function finds an entry in the eet file that is stored under the name specified, and returns that data, decompressed, if successful. NULL is returned if the lookup fails or if memory errors are encountered. It is the job of the calling program to call free() on the returned data. The number of bytes in the returned data chunk are placed in size_ret. </p>
<p> If the eet file handle is not valid NULL is returned and size_ret is filled with 0. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI const void* eet_read_direct (Eet_File * ef, const char * name, int * size_ret)</h3>
<p>Read a specified entry from an eet file and return data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ef</i> A valid eet file handle opened for reading.<br />
 <i>name</i> Name of the entry. eg: &#8216;/base/file_i_want&#8217;.<br />
 <i>size_ret</i> Number of bytes read from entry and returned.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data stored in that entry in the eet file.</dl>
<p> This function finds an entry in the eet file that is stored under the name specified, and returns that data if not compressed and successful. NULL is returned if the lookup fails or if memory errors are encountered or if the data is comrpessed. The calling program must never call free() on the returned data. The number of bytes in the returned data chunk are placed in size_ret. </p>
<p> If the eet file handle is not valid NULL is returned and size_ret is filled with 0. </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI int eet_shutdown (void)</h3>
<p>Shut down the EET library. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The new init count.</dl>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h3>EAPI int eet_write (Eet_File * ef, const char * name, const void * data, int size, int compress)</h3>
<p>Write a specified entry to an eet file handle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ef</i> A valid eet file handle opened for writing.<br />
 <i>name</i> Name of the entry. eg: &#8216;/base/file_i_want&#8217;.<br />
 <i>data</i> Pointer to the data to be stored.<br />
 <i>size</i> Length in bytes in the data to be stored.<br />
 <i>compress</i> Compression flags (1 == compress, 0 = don&#8217;t compress).</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Success or failure of the write.</dl>
<p> This function will write the specified chunk of data to the eet file and return greater than 0 on success. 0 will be returned on failure. </p>
<p> The eet file handle must be a valid file handle for an eet file opened for writing. If it is not, 0 will be returned and no action will be performed. </p>
<p> Name, and data must not be NULL, and size must be &gt; 0. If these conditions are not met, 0 will be returned. </p>
<p> The data will be copied (and optionally compressed) in ram, pending a flush to disk (it will stay in ram till the eet file handle is closed though). </p>
<p> <code>Since:</code></p>
<dl COMPACT>
<dd>1.0.0</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Eet from the source code.</p>
