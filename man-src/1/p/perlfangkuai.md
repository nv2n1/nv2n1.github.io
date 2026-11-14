---
title: "perlfangkuai(1)"
name: "perlfangkuai"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlfangkuai/"
---

<h2 class="name">NAME</h2>
 

 tetris - A tetris game 

<h2>SYNOPSIS</h2>

 perl tetris.pl

<h2>CONFIGURATION</h2>

 The configuration file should be the file with name ``.tetris'' under <font SIZE="-1">HOME</font> directory. Another option is using Tetris/Config.pm in any directory of <tt>@INC</tt>. 

 Here is an example of configuration: 
&nbsp;<wbr>#&nbsp;<wbr>-*- perl -*- 
&nbsp;<wbr><tt>%Config</tt>&nbsp;<wbr>=&nbsp;<wbr>( 
&nbsp;<wbr>&nbsp;<wbr><tt>%Config</tt>, 
&nbsp;<wbr>&nbsp;<wbr>'start_level'&nbsp;<wbr>=&gt;&nbsp;<wbr>3, 
&nbsp;<wbr>&nbsp;<wbr>'down_step'&nbsp;<wbr>=&gt;&nbsp;<wbr>2, 
&nbsp;<wbr>&nbsp;<wbr>'keybindings'&nbsp;<wbr>=&gt;&nbsp;<wbr>{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>%{$Config{keybindings}}, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ord('j')&nbsp;<wbr>=&gt;&nbsp;<wbr>\&amp;move_left, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ord('l')&nbsp;<wbr>=&gt;&nbsp;<wbr>\&amp;move_right, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ord('k')&nbsp;<wbr>=&gt;&nbsp;<wbr>\&amp;rotate, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ord('n')&nbsp;<wbr>=&gt;&nbsp;<wbr>\&amp;new_game, 
&nbsp;<wbr>&nbsp;<wbr>} 
&nbsp;<wbr>); 
&nbsp;<wbr>push&nbsp;<wbr>@$shapes, shape_from_string(&lt;&lt;<font SIZE="-1">SHAPE</font>); 
&nbsp;<wbr>0 0 8 0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 8 0 0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 8 8 8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 0 0 8 
&nbsp;<wbr>0 0 8 0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 8 8 8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 0 8 0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 8 8 8 
&nbsp;<wbr>0 8 8 8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 8 0 0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 0 8 0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 0 0 8 
&nbsp;<wbr>0 0 0 0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 0 0 0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 0 0 0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 0 0 0 
&nbsp;<wbr><font SIZE="-1">SHAPE</font> 

 <pre>
    push @$shapes, shape_from_string(&lt;&lt;SHAPE);
    0 0 9 0   0 0 0 0   0 0 0 0   0 0 9 0
    0 0 9 9   0 0 9 9   0 9 9 0   0 9 9 0
    0 0 0 0   0 0 9 0   0 0 9 0   0 0 0 0
    0 0 0 0   0 0 0 0   0 0 0 0   0 0 0 0
    SHAPE
</pre> 

 The key specification can get from this script: 

 <pre><code>
use Gtk2::Gdk::Keysyms;
use Glib qw / TRUE FALSE / ;
use Gtk2 - init;

my $window = Gtk2::Window-&gt;new ('toplevel');
$window-&gt;signal_connect(delete_event = &gt; sub{Gtk2-&gt;main_quit});
$window-&gt;signal_connect('key-press-event' = &gt; \&amp; show_key);

my $label = Gtk2::Label-&gt;new ();
$label-&gt;set_markup("&lt;span foreground=\"blue\" size=\"x-large\"&gt;Type something on the keyboard!&lt;/span&gt;");

$window-&gt;add($label);
$window-&gt;show_all;
$window-&gt;set_position('center-always');

Gtk2-&gt;main;
sub show_key
{
    my($widget, $event, $parameter) = @_;
    my $key_nr = $event-&gt;keyval();
    foreach
        my $key(keys % Gtk2::Gdk::Keysyms)
        {
            my $key_compare = $Gtk2::Gdk::Keysyms{$key};
            if ($key_compare == $key_nr) {
                print "'$key' =&gt; $key_nr,\n";
            }
        }
    return FALSE;
}
</code></pre> 

 Code to run after the <font SIZE="-1">GUI</font> setup, add to code ref <tt>$after_load_function</tt>. 

<h2>Index</h2>


