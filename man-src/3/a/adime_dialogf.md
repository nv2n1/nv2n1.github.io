---
title: "adime_dialogf(3)"
name: "adime_dialogf"
section: "3"
letter: "a"
url: "/docs/linux/man/3-adime_dialogf/"
description: "adime_dialogf"
---

<h2>NAME</h2>
<p> adime_dialogf</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/adime.h">adime.h</a>&gt;</code> </p>
<p> <code>int adime_dialogf(const char *title, int x, y, w, const char *format, &#8230;);</code></p>
<h2>DESCRIPTION</h2>
<p> Displays a dialog letting the user edit several different kinds of data. `title&#8217; specifies the caption of the dialog while `x&#8217; and `y&#8217; specify the top left corner of the dialog. Alternatively, either `x&#8217; or `y&#8217; or both can be set to `ADIME_ALIGN_CENTRE&#8217; or `ADIME_ALIGN_RIGHT&#8217;, in which case the dialog will be centred respectively right aligned. `w&#8217; specifies the width of the input field. The total width of the dialog depends on this number, and on the length of the strings given to the dialog. </p>
<p> The format string consists of one or more field descriptions, each followed be exactly one format specifier. The field description is a hint text used to help the user know what the field should contain. The format specifier is a percent sign, followed by an identifier, followed by a pair of square brackets (possibly with some extra options between (which I will refer to as &quot;format modifier&quot;)) and can be any of the following: </p>
<p> %bool[] </p>
<p> A check box, which can be either on or off. Next argument should be an `int *&#8217;, which will be set to 0 for off and 1 for on. Don&#8217;t use other values! </p>
<p> %greybool[] </p>
<p> A three-state greyable check box. Next argument should be an `int *&#8217;, which will be set to 0 for off, 1 for on, or 2 for greyed. Don&#8217;t use other values! </p>
<p> %double[x,y], %float[x,y], </p>
<p> %int[x,y], %short[x,y], %char[x,y], </p>
<p> %uint[x,y], %ushort[x,y], %uchar[x,y], </p>
<p> A number in the given format (uchar, ushort and uint are unsigned). The number will be clamped to the interval `x&#8217; to `y&#8217;, inclusive. You may omit `x&#8217; or `y&#8217; or both (but keep the comma!) to make it be the minimum respectively maximum for the data type. Next argument should be a pointer to the given data type. </p>
<p> %pdouble[x,y], %pfloat[x,y], </p>
<p> %pint[x,y], %pshort[x,y], %pchar[x,y], </p>
<p> %puint[x,y], %pushort[x,y], %puchar[x,y], </p>
<p> &quot;Plain&quot; number formats: With the corresponding formats not prefixed by &quot;p&quot;, the user can actually enter any mathematical expression, but these formats disable that feature so he can only enter numbers. Otherwise equal to their non-p-prefixed counterparts. </p>
<p> %string[bytes] </p>
<p> A string of length &lt;= `bytes&#8217; (in bytes). Next argument should be a `char *&#8217; with room for at least the given number of characters. Remember that the number of characters that fit in the string will be less if you use Unicode. With UTF-8, a character may be as long as six bytes, and with Unicode they are always 2 bytes. </p>
<p> %filename[len,extension,title] </p>
<p> A filename of length &lt;= `len&#8217;. Next argument should be a `char *&#8217; with room for at least the given number of bytes (this really is bytes, not characters, and a UTF-8 string can have characters that are 6 bytes long, so you should allocate six times as many bytes as you want characters!). The user will be able to enter the filename as a text or click a button to bring up a file selector. `extension&#8217; is a semicolon-separated list of file extensions (ie in the format &quot;bmp;pcx;tga;foo&quot;) which will be accepted by the file selector. You may omit `extension&#8217; (but keep the commas!), meaning that all file formats will be accepted. `title&#8217; is the title of the file selector dialog. You may also omit `title&#8217; (but keep the commas!), meaning that the description text for this field will be used. </p>
<p> %list[lines,list] </p>
<p> The user can select an element in a list of strings. `lines&#8217; specifies the height, in lines, of the list box (this can be omitted to let the function calculate the height for you). `list&#8217; is a semicolon-separated list of strings (if one or more strings needs to contain a semicolon (&#8216;;&#8217;) or an end bracket (&#8216;]&#8217;), the character can be escaped by a percent sign (&#8216;%&#8217;)). Next argument should be an `int *&#8217;, which will be set to the index of the string. </p>
<p> %vlist[lines] </p>
<p> The user can select an element in a list of strings. `lines&#8217; specifies the height, in lines, of the list box (this can be omitted to let the function calculate the height for you). Next argument should be an `int *&#8217;, which will be set to the index of the selected string, and then a `char **&#8217; which specifies the strings to choose among, then an `int&#8217; which tells how many strings the list contains. </p>
<p> %datafile[lines,types] </p>
<p> The user can select an element in an Allegro DATAFILE. You should pass first an `int *&#8217;, which will be set to the index of the datafile that was selected, and then a `DATAFILE *&#8217;, which should be the datafile to look in. `lines&#8217; specifies the height, in lines, of the list box (this can be omitted to let the function calculate the height for you). `types&#8217; is a semicolon-separated list of datafile types. You must include all four characters in each type, so it could for example look like this: </p>
<pre><code>
"%datafile[7,BMP ;RLE ;XCMP; CMP]"
</code></pre>
<p> %wlist[lines,title,list] </p>
<p> %wvlist[lines,title] </p>
<p> %wdatafile[lines,title,types] </p>
<p> Like %list[], %vlist[] and %datafile, but rather than having the list box in the window, a button will be displayed. When the user clicks the button, a new window with the actual list in (and with the given title) will be opened. </p>
<p> %nothing[] </p>
<p> No input data. Will only display the preceding description text as usually. This can be used if you want a section of the dialog to have a special header. </p>
<p> %line[] </p>
<p> No input data. Will only display the preceding description text (if there is any) as usually, and then a horizontal delimitor line. Like %nothing[], this can be used if you want a section of the dialog to be delimited from the rest of the dialog. </p>
<p> %button[text] </p>
<p> A button (with the given text on) which calls your custom callback. Next argument should be a function pointer, pointing to a function of the type </p>
<p>int my_callback(DIALOG *d);<br />
 This will be called when the user clicks the button. It will be given the dialog object representing the button. Its return value is a bit special: If it is 0, then nothing happens. If it is ADIME_REDRAW (which is defined to be the smallest negative number), then the dialog will be redrawn. If it is any other positive number, then the dialog will exit with that return value not saving the results of the dialog (the usual behavior of a cancel button). If it is any other negative number, then the sign will be removed and the unsigned number returned, and the contents of the dialog will be saved (the usual behavior of the ok button). </p>
<p> You are allowed to open a new dialog inside your callback, which may be a less messy and more flexible alternative to %dialogf[]. </p>
<p> %buttonrow[BUTTONS] </p>
<p> One or more buttons in a horizontal row. These are displayed the same way as the OK and Cancel buttons (actually, the OK and Cancel buttons are implemented by appending a %buttonrow[] to the end of the dialog). Next argument should be a function pointer, pointing to a function of the type: </p>
<p>int my_callback(DIALOG *d, int n);<br />
 This will be called with the dialog object for the clicked button as the first argument and the index of this button as the second (i.e., n=1 for the first button, n=2 for the second and so on). The return value works the same way as for %button[] (see above). </p>
<p> The modifier (BUTTONS) is itself a format string, consisting of a comma-separated list of buttons. Each button begins with the text which will appear on the button. Then comes an optional semicolon-separated list of shortcuts to this button. An example may help to clarify: </p>
<p>% buttonrow[OK; CTRL + O; ENTER, Cancel; ESC, Help; F1; ALT + H]<br />
 This format will display four buttons: OK, Cancel and Help. The OK button has the shortcuts CTRL-O and ENTER. The Cancel button has the shortcut ESC. The Help button has the shortcuts F1 and ALT-H. Shortcuts are specified in uppercase, with the state of shift, ctrl, alt etc preceding the key to press. The key has the same name as the `KEY_*&#8217; macro defined by Allegro (i.e., &quot;ENTER&quot; for `KEY_ENTER&#8217;, &quot;3&quot; for `KEY_3&#8242; and &quot;NUMLOCK&quot; for `KEY_NUMLOCK&#8217;). The state consists of zero or more key shift flags separated by plus signs. The names of these are the same as Allegro&#8217;s `KB_*_FLAG&#8217; macros (i.e., &quot;SHIFT&quot; for `KB_SHIFT_FLAG&#8217; and &quot;CAPSLOCK&quot; for `KB_CAPSLOCK_FLAG&#8217;). If you write e.g. CTRL+O, it means that CTRL must be held down while pressing O in order to activate the shortcut, while it is optional to hold down other key modifiers, e.g., SHIFT. If you don&#8217;t want the shortcut to be activated when SHIFT is down (for instance), then you can write CTRL+-SHIFT+O, i.e., you precede the forbidden key with a minus sign. </p>
<p> %dialogf[buttontext] </p>
<p> A button which opens another adime_dialogf() sub-dialog. Next argument should be the title of the dialog as a `char *&#8217;, followed by `x&#8217;, `y&#8217;, `edit_w&#8217; as `int&#8217;s and then `format&#8217; as a `char *&#8217;. These arguments correspond to the arguments given to `adime_dialogf()&#8217;. Depending on what `format&#8217; contains, you then have to add more parameters which the sub-dialog will alter. `buttontext&#8217; is the text which will be displayed on the button which opens the sub-dialog. An example may help to clarify: </p>
<p>adime_dialogf(&#8220;My dialog&#8221;,<br />
              ADIME_ALIGN_CENTRE, ADIME_ALIGN_CENTRE, 200,<br />
              &#8220;Open sub-dialog:%dialog[Click me!]&#8221;,<br />
              &#8220;My sub-dialog&#8221;,<br />
              ADIME_ALIGN_CENTRE, ADIME_ALIGN_CENTRE, 200,<br />
              &#8220;Save in text format:%bool[]&#8221;,<br />
              &amp;text_format);</p>
<p> %vdialogf[buttontext] </p>
<p> This is like %dialogf[], except that the `&#8230;&#8217; arguments are given as an `adime_va_list&#8217; rather than being expanded into the same argument list. (see also `adime_va_list&#8217;) </p>
<p> %chain[] </p>
<p> This is like an &quot;inline&quot; version of %vdialogf[]: You should pass two arguments, first a format string and then an `adime_va_list&#8217;. The dialog defined by this format string and `adime_va_list&#8217; will be inserted directly into this dialog. (See exchain.c for an example.) </p>
<p> Any special characters mentioned here can be escaped by placing a percent sign (&#8216;%&#8217;) before it, e.g. if you need a literal &#8216;]&#8217; character somewhere in the format string. The field description may contain newlines. </p>
<p> Returns 1 if the user selected the OK button, and 2 if he selected the Cancel button. The `&#8230;&#8217; parameters will be left untouched if the user clicked Cancel but they will change to the new values if he clicked OK. The initial values of the parameters will be taken as default values in the dialog objects. </p>
<p> The debug library is very useful when you use this function: It can detect almost all illegal format strings. If it finds one, it shuts down the program with a traceback and writes a description of the error to the file allegro.log. </p>
<p> An example may help to clarify things (see also the programs in the examples directory): </p>
<pre><code>
char name_buffer[1024] = "";
int age = 20;
int shoe_size = 40;
int married = 0;
char filename_buffer[1024] = "";

adime_dialogf("Fill in personal data",
              ADIME_ALIGN_CENTRE, ADIME_ALIGN_CENTRE, 200,
              "Name%string[1024]"
              "Age (years)%int[0,150]"
              "%line"
              "Shoe size (Swedish units)%float[10,60]"
              "Married%bool[]"
              "Favourite text file%filename[1024,txt,Select a text file]",
              name_buffer,
              &amp;age,
              &amp;shoe_size,
              &amp;married,
              filename_buffer);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-adime_init/">adime_init</a></code>(3), <code><a href="/docs/linux/man/3-adime_vdialogf/">adime_vdialogf</a></code>(3), <code><a href="/docs/linux/man/3-adime_bmp/">adime_bmp</a></code>(3), <code><a href="/docs/linux/man/3-adime_font/">adime_font</a></code>(3), <code><a href="/docs/linux/man/3-adime_va_list/">adime_va_list</a></code>(3) </p>
<h2>Index</h2>
