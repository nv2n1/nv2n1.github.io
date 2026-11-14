---
title: "function(1)"
name: "function"
section: "1"
letter: "f"
url: "/docs/linux/man/1-function/"
---

<h2 class="name">NAME</h2>
 

 function - create a function

<h3>Synopsis</h3>

 function [OPTIONS] NAME; BODY; end

<h3>Description</h3>

<dl>
<dt>*
<dd> -d DESCRIPTION or --description=DESCRIPTION is a description of what the function does, suitable as a completion description
<dt>*
<dd> -e or --on-event EVENT_NAME tells fish to run this function when the specified named event is emitted. Fish internally generates named events e.g. when showing the prompt.
<dt>*
<dd> -j PID or --on-job-exit PID tells fish to run this function when the job with group id PID exits. Instead of PID, the string 'caller' can be specified. This is only legal when in a command substitution, and will result in the handler being triggered by the exit of the job which created this command substitution.
<dt>*
<dd> -p PID or --on-process-exit PID tells fish to run this function when the fish child process with process id PID exits
<dt>*
<dd> -s or --on-signal SIGSPEC tells fish to run this function when the signal SIGSPEC is delivered. SIGSPEC can be a signal number, or the signal name, such as SIGHUP (or just HUP)
<dt>*
<dd> -v or --on-variable VARIABLE_NAME tells fish to run this function when the variable VARIABLE_NAME changes value</dl>
 

 

 This builtin command is used to create a new function. A function is a list of commands that will be executed when the name of the function is entered. The function 

 

 <pre>
function hi
        echo hello
end
</pre> 

 

 will write hello whenever the user enters hi. 

 If the user enters any additional arguments after the function, they are inserted into the environment variable array argv. 

 By using one of the event handler switches, a function can be made to run automatically at specific events. The user may generate new events using the &lt;a href='emit'&gt;emit builtin. Fish generates the following named events: 

<dl>
<dt>*
<dd> fish_prompt, which is emitted whenever a new fish prompt is about to be displayed
<dt>*
<dd> fish_command_not_found, which is emitted whenever a command lookup failed</dl>
 

<h3>Example</h3>

 

 <pre>
function ll
        ls -l $argv
end
</pre> 

 

 will run the ls command, using the -l option, while passing on any additional files and switches to ls. 

 

 <pre><code>
function mkdir - d 'Create a directory and set CWD' mkdir $argv if test $status = 0 switch $argv[(count $argv)] case '-*'
</code></pre> 

 

 

 <pre><code>
case '*' cd $argv[(count $argv)] return end
    end
        end
</code></pre> 

 

 will run the mkdir command, and if it is successful, change the current working directory to the one just created. 

<h2>Index</h2>


