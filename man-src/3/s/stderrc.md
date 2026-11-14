---
title: "stderrc(3)"
name: "stderrc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderrc/"
---

std::errc - std::errc

<h2>Synopsis</h2>

Defined in header &lt;system_error&gt; 
enum class errc; <i>(since C++11)</i> 
The scoped enumeration std::errc defines the values of portable error conditions that correspond to the POSIX error codes. 

<h2>Member constants</h2>

Constant Equivalent POSIX Error 
address_family_not_supported EAFNOSUPPORT 
address_in_use EADDRINUSE 
address_not_available EADDRNOTAVAIL 
already_connected EISCONN 
argument_list_too_long E2BIG 
argument_out_of_domain EDOM 
bad_address EFAULT 
bad_file_descriptor EBADF 
bad_message EBADMSG 
broken_pipe EPIPE 
connection_aborted ECONNABORTED 
connection_already_in_progress EALREADY 
connection_refused ECONNREFUSED 
connection_reset ECONNRESET 
cross_device_link EXDEV 
destination_address_required EDESTADDRREQ 
device_or_resource_busy EBUSY 
directory_not_empty ENOTEMPTY 
executable_format_error ENOEXEC 
file_exists EEXIST 
file_too_large EFBIG 
filename_too_long ENAMETOOLONG 
function_not_supported ENOSYS 
host_unreachable EHOSTUNREACH 
identifier_removed EIDRM 
illegal_byte_sequence EILSEQ 
inappropriate_io_control_operation ENOTTY 
interrupted EINTR 
invalid_argument EINVAL 
invalid_seek ESPIPE 
io_error EIO 
is_a_directory EISDIR 
message_size EMSGSIZE 
network_down ENETDOWN 
network_reset ENETRESET 
network_unreachable ENETUNREACH 
no_buffer_space ENOBUFS 
no_child_process ECHILD 
no_link ENOLINK 
no_lock_available ENOLCK 
no_message_available ENODATA 
no_message ENOMSG 
no_protocol_option ENOPROTOOPT 
no_space_on_device ENOSPC 
no_stream_resources ENOSR 
no_such_device_or_address ENXIO 
no_such_device ENODEV 
no_such_file_or_directory ENOENT 
no_such_process ESRCH 
not_a_directory ENOTDIR 
not_a_socket ENOTSOCK 
not_a_stream ENOSTR 
not_connected ENOTCONN 
not_enough_memory ENOMEM 
not_supported ENOTSUP 
operation_canceled ECANCELED 
operation_in_progress EINPROGRESS 
operation_not_permitted EPERM 
operation_not_supported EOPNOTSUPP 
operation_would_block EWOULDBLOCK 
owner_dead EOWNERDEAD 
permission_denied EACCES 
protocol_error EPROTO 
protocol_not_supported EPROTONOSUPPORT 
read_only_file_system EROFS 
resource_deadlock_would_occur EDEADLK 
resource_unavailable_try_again EAGAIN 
result_out_of_range ERANGE 
state_not_recoverable ENOTRECOVERABLE 
stream_timeout ETIME 
text_file_busy ETXTBSY 
timed_out ETIMEDOUT 
too_many_files_open_in_system ENFILE 
too_many_files_open EMFILE 
too_many_links EMLINK 
too_many_symbolic_link_levels ELOOP 
value_too_large EOVERFLOW 
wrong_protocol_type EPROTOTYPE

<h2>Non-member functions</h2>

make_error_code(std::errc) constructs an std::errc error code 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 

 
make_error_condition(std::errc) constructs an std::errc error condition 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i>

<h2>Helper classes</h2>

is_error_condition_enum&lt;std::errc&gt; extends the type trait std::is_error_condition_enum to identify the the std::errc values as error conditions 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;system_error&gt;

#include &lt;thread&gt;

int main()

{
    try {
        std::thread().detach(); // detaching a not-a-thread
    } catch (const std::system_error &amp;e) {
        std::cout &lt;&lt; &quot;Caught a system_error\n&quot;;
        if (e.code() == std::errc::invalid_argument)
            std::cout &lt;&lt; &quot;The error condition is std::errc::invalid_argument\n&quot;;
        std::cout &lt;&lt; &quot;the error description is &quot; &lt;&lt; e.what() &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Caught a system_error 
&nbsp;<wbr>&nbsp;The error condition is std::errc::invalid_argument 
&nbsp;<wbr>&nbsp;the error description is Invalid argument

<h2>See also</h2>

error_code holds a platform-dependent error code 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++11)</i> 
error_condition holds a portable error code 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++11)</i> 
