---
title: "stdgetenv(3)"
name: "stdgetenv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdgetenv/"
---

std::getenv - std::getenv

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdlib&gt;

    char *getenv(const char *env_var);</code></pre> 
Searches the environment list provided by the host environment (the OS), for a string that matches the C string pointed to by env_var and returns a pointer to the C string that is associated with the matched environment list member. 
This function is not required to be thread-safe. Another call to getenv, as well as a call to the POSIX functions setenv(), unsetenv(), and putenv() may invalidate the pointer returned by a previous call or modify the string obtained from a previous call. <i>(until C++11)</i> 
This function is thread-safe (calling it from multiple threads does not introduce a data race) as long as no other function modifies the host environment. In particular, the POSIX functions setenv(), unsetenv(), and putenv() would introduce a data race if called without synchronization. <i>(since C++11)</i> 
Modifying the string returned by getenv invokes undefined behavior. 

<h2>Parameters</h2>

env_var - null-terminated character string identifying the name of the environmental variable to look for

<h2>Return value</h2>

Character string identifying the value of the environmental variable or null pointer if such variable is not found. 

<h2>Notes</h2>

On POSIX systems, the environment_variables are also accessible through the global variable environ, declared as extern char **environ; in &lt;unistd.h&gt;, and through the optional third argument, envp, of the_main_function. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstdlib&gt;
int main()

{
    if (const char *env_p = std::getenv(&quot;PATH&quot;))
        std::cout &lt;&lt; &quot;Your PATH is: &quot; &lt;&lt; env_p &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Your PATH is: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games

<h2>See also</h2>


