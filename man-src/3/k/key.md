---
title: "key(3)"
name: "key"
section: "3"
letter: "k"
url: "/docs/linux/man/3-key/"
description: "key – Array of flags indicating key state. Allegro game programming library."
---

<h2>NAME</h2>
<p> key &#8211; Array of flags indicating key state. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern volatile char key[KEY_MAX];</code></p>
<h2>DESCRIPTION</h2>
<p> Array of flags indicating the state of each key, ordered by scancode. Wherever possible these values will be updated asynchronously, but if keyboard_needs_poll() returns TRUE, you must manually call poll_keyboard() to update them with the current input state. The scancodes are defined in allegro/keyboard.h as a series of KEY_* constants (and are also listed below). For example, you could write: </p>
<pre><code>
if (key[KEY_SPACE])
    printf("Space is pressed
");
</code></pre>
<p> Note that the array is supposed to represent which keys are physically held down and which keys are not, so it is semantically read-only. </p>
<p> These are the keyboard scancodes: </p>
<pre>
   KEY_A ... KEY_Z,
   KEY_0 ... KEY_9,
   KEY_0_PAD ... KEY_9_PAD,
   KEY_F1 ... KEY_F12,
   
   KEY_ESC, KEY_TILDE, KEY_MINUS, KEY_EQUALS,
   KEY_BACKSPACE, KEY_TAB, KEY_OPENBRACE, KEY_CLOSEBRACE,
   KEY_ENTER, KEY_COLON, KEY_QUOTE, KEY_BACKSLASH,
   KEY_BACKSLASH2, KEY_COMMA, KEY_STOP, KEY_SLASH,
   KEY_SPACE,
   
   KEY_INSERT, KEY_DEL, KEY_HOME, KEY_END, KEY_PGUP,
   KEY_PGDN, KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN,
   
   KEY_SLASH_PAD, KEY_ASTERISK, KEY_MINUS_PAD,
   KEY_PLUS_PAD, KEY_DEL_PAD, KEY_ENTER_PAD,
   
   KEY_PRTSCR, KEY_PAUSE,
   
   KEY_ABNT_C1, KEY_YEN, KEY_KANA, KEY_CONVERT, KEY_NOCONVERT,
   KEY_AT, KEY_CIRCUMFLEX, KEY_COLON2, KEY_KANJI,
   
   KEY_LSHIFT, KEY_RSHIFT,
   KEY_LCONTROL, KEY_RCONTROL,
   KEY_ALT, KEY_ALTGR,
   KEY_LWIN, KEY_RWIN, KEY_MENU,
   KEY_SCRLOCK, KEY_NUMLOCK, KEY_CAPSLOCK
   
   KEY_EQUALS_PAD, KEY_BACKQUOTE, KEY_SEMICOLON, KEY_COMMAND
</pre>
<p> Finally, you may notice an `odd&#8217; behaviour of the KEY_PAUSE key. This key only generates an interrupt when it is pressed, not when it is released. For this reason, Allegro pretends the pause key is a `state&#8217; key, which is the only way to make it usable. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-poll_keyboard/">poll_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-key_shifts/">key_shifts</a></code>(3) </p>
<h2>Index</h2>
