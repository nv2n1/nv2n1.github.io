---
title: "sdl_keysym(3)"
name: "sdl_keysym"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdl_keysym/"
---

SDL_keysym - Keysym structure
<h2>Structure Definition</h2><pre><tt>typedef struct{
 Uint8 scancode;
 SDLKey sym;
 SDLMod mod;
 Uint16 unicode;
} SDL_keysym;</tt></pre><h2>Structure Data</h2><dl COMPACT><dt><b>scancode</b>
<dd>Hardware specific scancode
<dt><b>sym</b>
<dd>SDL virtual keysym
<dt><b>mod</b>
<dd>Current key modifiers
<dt><b>unicode</b>
<dd>Translated character</dl><h2>Description</h2>The <b>SDL_keysym</b> structure is used by reporting key presses and releases since it is a part of the <i></i><b>SDL_KeyboardEvent</b>. 

 The <b>scancode</b> field should generally be left alone, it is the hardware dependent scancode returned by the keyboard. The <b>sym</b> field is extremely useful. It is the SDL-defined value of the key (see <i>SDL Key Syms</i>. This field is very useful when you are checking for certain key presses, like so: 

 <pre><tt>.
.
while(SDL_PollEvent(&amp;event)){
 switch(event.type){
 case SDL_KEYDOWN:
 if(event.key.keysym.sym==SDLK_LEFT)
 move_left();
 break;
 .
 .
 .
 }
}
.
.</tt></pre>&nbsp;<wbr><b>mod</b>&nbsp;<wbr>stores the current state of the keyboard modifiers as explained in&nbsp;<wbr><i></i><b>SDL_GetModState</b>. The&nbsp;<wbr><b>unicode</b>&nbsp;<wbr>is only used when UNICODE translation is enabled with&nbsp;<wbr><i></i><b>SDL_EnableUNICODE</b>. If&nbsp;<wbr><b>unicode</b>&nbsp;<wbr>is non-zero then this a the UNICODE character corresponding to the keypress. If the high 9 bits of the character are 0, then this maps to the equivalent ASCII character:&nbsp;<wbr> 

 <pre><tt>char ch;
if ( (keysym.unicode &amp; 0xFF80) == 0 ) {
 ch = keysym.unicode &amp; 0x7F;
}
else {
 printf(&quot;An International Character.
&quot;);
}</tt></pre>&nbsp;<wbr>UNICODE translation does have a slight overhead so don't enable it unless its needed.
<h2>See Also</h2><i></i><b>SDLKey</b>
