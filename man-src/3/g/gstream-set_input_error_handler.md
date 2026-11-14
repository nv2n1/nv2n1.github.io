---
title: "gstream-set_input_error_handler(3)"
name: "gstream-set_input_error_handler"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gstream-set_input_error_handler/"
description: "set_input_error_handler"
---

<h2>NAME</h2>
<p> set_input_error_handler</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gstream.h">gstream.h</a>&gt;</code> </p>
<p> <code>void set_input_error_handler(int error);</code></p>
<h2>DESCRIPTION</h2>
<p> Sets an error handler that will be called of the inputter encounter any unusual, erratic behaviour, e.g. the user trying to move the cursor off the string or pressing invalid keys. The handler is passed a constant which currently can be one of the following: </p>
<p> IE_UNRECOGNIZED_KEY </p>
<p> The inputted key couldn&#8217;t be used for anything, i.e. it wasn&#8217;t one of the recognized control keys (for example KEY_LEFT, but not KEY_PGDN) and the input approver didn&#8217;t accept it as a valid char either. </p>
<p> IE_CURSOR_EXCEEDING_LIMITS </p>
<p> The user tried to move the cursor off the input string, e.g. if the cursor is at the beginning of the string and the user presses KEY_LEFT or KEY_HOME. Note that pressing KEY_UP and KEY_DOWN currently returns IE_CURSOR_EXCEEDING_LIMITS, no matter where the cursor is. </p>
<p> IE_NO_ROOM_FOR_CHAR </p>
<p> There was no room for the inputted char. This often occurs if the length of the input string has been limited to a certain maximum with set_max_input_length, but may also happen if the buffer that the inputter puts the data in is full. The latter is not likely to happen unless you, for instance, force the gstream to use your own buffer, as the standard buffer is rather large. </p>
<p> Note that these constants are defined in &#8216;gbuf&#8217; so you have to put </p>
<pre><code>
int stupid_mistakes = 0;

void ieh_for_my_number_inputter(int e)
{
    switch (e) {
    case gbuf::IE_UNRECOGNIZED_KEY: // note: gbuf::
        if (stupid_mistakes &gt; MUST_BE_BRAIN_DEAD) {
            say_to_user("Sorry, you can only input numbers!");
            user_characteristics = FOOL;
            stupid_mistakes = 0;
        } else
            ++stupid_mistakes;
        break;
    case gbuf::IE_NO_ROOM_FOR_CHAR:
        play_quiet_beep();
        break;
    } // in all other situations: do nothing
}
</code></pre>
<p> You should be aware that the inputter automatically will take care of any problems encountered and solve them with much elegance (often simply by ignoring the user if the result of the action would be illegal), so your error handler doesn&#8217;t really deal with the problem or handle the situation &#8211; it is merely a way for you to warn or tell the user that he is doing something wrong. </p>
<p> Some advices concerning the style is given here &#8211; of course, you don&#8217;t have to follow them, you are free to have you own opinion and the advices are general so they might not fit your particular situation, but please at least read them through before you begin designing your own error handler: </p>
<p> Often the best thing to do is not to do anything. For example, simply ignoring that the user is pressing an unrecognized key is often better than complaining, unless you have a specific reason for warning him &#8211; in the example above the user should be aware that he was supposed to enter a number </p>
<p> If you decide to do something, remember the KISS principle: keep it simple. If you as a user have made a mistake, you&#8217;re probably already irritated because of that and then it doesn&#8217;t help the situation that you have to watch the screen go beserk (or hear an entire symphony) before you can continue </p>
<p> If you play a sound, such as a beep, make it a short, quiet one. Personally I can&#8217;t stand a hysterical &quot;BEEEEEEEEEP&quot; if I accidentally hit the wrong key </p>
<p> Generally don&#8217;t use large special effects. If you have invented a new kind of plasma generator, you&#8217;re probably better off releasing a demo that shows it, instead of making your users annoyed by forcing them to look at it everytime they make the slightest fault </p>
<p> If you display a message, consider implementing a system like in the example above where the user is given a few tries before the message is displayed, to ensure it is only (or mostly) sent to newbies. If the example should be perfect, it would even reset the mistake counter now and then </p>
<p> At last a practical advice: keep in mind that future versions of gstream may have more error codes added, so design the function in a way that it won&#8217;t break as soon as that happens (e.g. don&#8217;t count on that if you test for the first constants, then the remaining has to be the last) </p>
<p> There is a typedef, &#8216;input_error_handler&#8217;, in &#8216;gbuf&#8217; for the type of a pointer to a handler function: </p>
<pre><code>
gbuf::input_error_handler tmp_ieh;

//...

tmp_ieh = gs1.get_input_error_handler();
gs1.set_input_error_handler(gs2.get_input_error_handler());
gs2.set_input_error_handler(tmp_ieh);
</code></pre>
<p> The default input error handler is &#8216;ieh_never_complain&#8217;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gstream-get_input_error_handler/">gstream-get_input_error_handler</a></code>(3), <code><a href="/docs/linux/man/3-gstream-set_input_approver/">gstream-set_input_approver</a></code>(3), <code><a href="/docs/linux/man/3-gstream-set_max_input_length/">gstream-set_max_input_length</a></code>(3), <code><a href="/docs/linux/man/3-gstream-ieh_never_complain/">gstream-ieh_never_complain</a></code>(3) </p>
<h2>Index</h2>
