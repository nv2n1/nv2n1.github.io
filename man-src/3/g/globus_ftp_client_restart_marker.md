---
title: "globus_ftp_client_restart_marker(3)"
name: "globus_ftp_client_restart_marker"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_ftp_client_restart_marker/"
description: "Restart Markers –"
---

<h2 class="name">NAME</h2>
<p> Restart Markers &#8211; </p>
<h3>Data Structures</h3>
<p> union <code>globus_ftp_client_restart_marker_t</code><br />
 <i>Restart marker.</i> </p>
<p> This structure is may be either a stream mode transfer offset, or an extended block mode byte range. &quot;</p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_ftp_client_restart_marker_init</code> (<code>globus_ftp_client_restart_marker_t</code> *marker) </p>
<p> globus_result_t <code>globus_ftp_client_restart_marker_copy</code> (<code>globus_ftp_client_restart_marker_t</code> *new_marker, <code>globus_ftp_client_restart_marker_t</code> *marker) </p>
<p> globus_result_t <code>globus_ftp_client_restart_marker_destroy</code> (<code>globus_ftp_client_restart_marker_t</code> *marker) </p>
<p> globus_result_t <code>globus_ftp_client_restart_marker_insert_range</code> (<code>globus_ftp_client_restart_marker_t</code> *marker, globus_off_t offset, globus_off_t end_offset) </p>
<p> globus_result_t <code>globus_ftp_client_restart_marker_set_ascii_offset</code> (<code>globus_ftp_client_restart_marker_t</code> *marker, globus_off_t offset, globus_off_t ascii_offset) </p>
<p> globus_result_t <code>globus_ftp_client_restart_marker_set_offset</code> (<code>globus_ftp_client_restart_marker_t</code> *marker, globus_off_t offset) </p>
<p> globus_result_t <code>globus_ftp_client_restart_marker_get_total</code> (<code>globus_ftp_client_restart_marker_t</code> *marker, globus_off_t *total_bytes) </p>
<p> globus_result_t <code>globus_ftp_client_restart_marker_to_string</code> (<code>globus_ftp_client_restart_marker_t</code> *marker, char **marker_string) </p>
<p> globus_result_t <code>globus_ftp_client_restart_marker_from_string</code> (<code>globus_ftp_client_restart_marker_t</code> *marker, const char *marker_string) </p>
<h2>Detailed Description</h2>
<p> FTP Restart Markers </p>
<p> The Globus FTP Client library provides the ability to start a file transfer from a known location into the file. This is accomplished by passing a restart marker to the <code>globus_ftp_client_get()</code>, <code>globus_ftp_client_put()</code>, or <code>globus_ftp_client_third_party_transfer()</code> functions.</p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_ftp_client_restart_marker_copy (<code>globus_ftp_client_restart_marker_t</code> *new_marker, <code>globus_ftp_client_restart_marker_t</code> *marker)</h3>
<p> Create a copy of a restart marker. </p>
<p> This function copies the contents of marker to new_marker. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>new_marker</i> A pointer to a new restart marker.<br />
 <i>marker</i> The marker to copy.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_restart_marker_init()</code>, <code>globus_ftp_client_restart_marker_destroy()</code></dl>
<h3>globus_result_t globus_ftp_client_restart_marker_destroy (<code>globus_ftp_client_restart_marker_t</code> *marker)</h3>
<p> Destroy a restart marker. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>marker</i> Restart marker. This marker must be initialized by either calling <code>globus_ftp_client_restart_marker_init()</code> or <code>globus_ftp_client_restart_marker_copy()</code></dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_restart_marker_t</code>, <code>globus_ftp_client_restart_marker_init()</code>, <code>globus_ftp_client_restart_marker_copy()</code></dl>
<h3>globus_result_t globus_ftp_client_restart_marker_from_string (<code>globus_ftp_client_restart_marker_t</code> *marker, const char *marker_string)</h3>
<p> Initialize a restart marker from a string. </p>
<p> This function initializes a new restart, <i>marker</i>, based on the <i>marker_string</i> parameter. The string may be either a single offset for a stream-mode restart marker, or a comma-separated list of start-end ranges. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>marker</i> The restart marker to be unitialized.<br />
 <i>marker_string</i> The string containing a textual representation of a restart marker.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>Restart Markers</code></dl>
<h3>globus_result_t globus_ftp_client_restart_marker_get_total (<code>globus_ftp_client_restart_marker_t</code> *marker, globus_off_t *total_bytes)</h3>
<p> Get total bytes accounted for in restart marker </p>
<p> This funtion will return the sum of all bytes accounted for in a restart marker. If this restart marker contains a stream offset then this value is the same as the offset (not the ascii offset) that it was set with. If it is a range list, it a sum of all the bytes in the ranges. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>marker</i> A previously initialized or copied restart marker<br />
 <i>total_bytes</i> pointer to storage for total bytes in marker</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Error on NULL marker or total bytes</dl>
</dl>
<h3>globus_result_t globus_ftp_client_restart_marker_init (<code>globus_ftp_client_restart_marker_t</code> *marker)</h3>
<p> Initialize a restart marker. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>marker</i> New restart marker.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_restart_marker_t</code>, <code>globus_ftp_client_restart_marker_destroy()</code></dl>
<h3>globus_result_t globus_ftp_client_restart_marker_insert_range (<code>globus_ftp_client_restart_marker_t</code> *marker, globus_off_toffset, globus_off_tend_offset)</h3>
<p> Insert a range into a restart marker </p>
<p> This function updates a restart marker with a new byte range, suitable for using to restart an extended block mode transfer. Adjacent ranges within the marker will be combined into a single entry in the marker. </p>
<p> The marker must first be initialized by calling <code>globus_ftp_client_restart_marker_init()</code> or <code>globus_ftp_client_restart_marker_copy()</code>. </p>
<p> A marker can only hold a range list or a stream offset. Calling this function after calling <code>globus_ftp_client_restart_marker_set_offset()</code> will result in a marker suitable only for use restarting an extended block mode transfer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>marker</i> A restart marker<br />
 <i>offset</i> The starting offset of the range.<br />
 <i>end_offset</i> The ending offset of the range.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_restart_marker_set_offset()</code> <code>globus_ftp_client_operationattr_set_mode()</code></dl>
<h3>globus_result_t globus_ftp_client_restart_marker_set_ascii_offset (<code>globus_ftp_client_restart_marker_t</code> *marker, globus_off_toffset, globus_off_tascii_offset)</h3>
<p> Set the offset for a restart marker. </p>
<p> This function modifies a restart marker to contain a stream offset, suitable for using to restart a steam mode transfer. </p>
<p> The marker must first be initialized by calling <code>globus_ftp_client_restart_marker_init()</code> or <code>globus_ftp_client_restart_marker_copy()</code>. </p>
<p> A marker can only hold a range list or a stream offset. Calling this function after calling <code>globus_ftp_client_restart_marker_insert_range()</code> will delete the ranges associated with the marker, and replace it with a marker suitable only for use restarting a stream mode transfer. </p>
<p> When restarting an ASCII type transfer, use <code>globus_ftp_client_restart_marker_set_ascii_offset()</code> to set both the offset used in the local representation of an ACSII file, and the network representation of the ASCII file. For UNIX systems, the former includes counts newlines as one character towards the file offset, and the latter counts them as 2 characters (CRLF). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>marker</i> A restart marker<br />
 <i>offset</i> The local stream offset.<br />
 <i>ascii_offset</i> The network ascii representation of the offset.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_restart_marker_insert_range()</code>, <code>globus_ftp_client_restart_marker_set_offset()</code>, <code>globus_ftp_client_operationattr_set_mode()</code>, <code>globus_ftp_client_operationattr_set_type()</code></dl>
<h3>globus_result_t globus_ftp_client_restart_marker_set_offset (<code>globus_ftp_client_restart_marker_t</code> *marker, globus_off_toffset)</h3>
<p> Set the offset for a restart marker. </p>
<p> This function modifies a restart marker to contain a stream offset, suitable for using to restart a steam mode transfer. </p>
<p> The marker must first be initialized by calling <code>globus_ftp_client_restart_marker_init()</code> or <code>globus_ftp_client_restart_marker_copy()</code>. </p>
<p> A marker can only hold a range list or a stream offset. Calling this function after calling <code>globus_ftp_client_restart_marker_insert_range()</code> will delete the ranges associated with the marker, and replace it with a marker suitable only for use restarting a stream mode transfer. </p>
<p> When restarting an ASCII type transfer, the offset must take into account the additional carriage return characters added to the data stream. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>marker</i> A restart marker<br />
 <i>offset</i> The stream offset</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_ftp_client_restart_marker_insert_range()</code>, <code>globus_ftp_client_operationattr_set_mode()</code>, <code>globus_ftp_client_operationattr_set_type()</code></dl>
<h3>globus_result_t globus_ftp_client_restart_marker_to_string (<code>globus_ftp_client_restart_marker_t</code> *marker, char **marker_string)</h3>
<p> Create a string representation of a restart marker. </p>
<p> This function sets the <i>marker_string</i> parameter to point to a freshly allocated string suitable for sending as an argument to the FTP REST command, or for a later call to <code>globus_ftp_client_restart_marker_from_string()</code>. </p>
<p> The string pointed to by marker_string must be freed by the caller. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>marker</i> An initialized FTP client restart marker.<br />
 <i>marker_string</i> A pointer to a char * to be set to a freshly allocated marker string.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>Restart Markers</code></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_ftp_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAP">Author</a></p>
<dd></dl>
