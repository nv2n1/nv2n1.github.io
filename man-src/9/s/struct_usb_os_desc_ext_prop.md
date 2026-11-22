---

title: "struct_usb_os_desc_ext_prop(9)"
name: "struct_usb_os_desc_ext_prop"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_os_desc_ext_prop/"
description: "struct_usb_os_desc_ext_prop – describes one “Extended Property”"
---

<p>struct_usb_os_desc_ext_prop &#8211; describes one "Extended Property" </p>

<pre><code>struct usb_os_desc_ext_prop {
  struct list_head entry;
  u8 type;
  int name_len;
  char * name;
  int data_len;
  char * data;
  struct config_item item;
};
</code></pre>
<h2>MEMBERS</h2>
<p>entry </p>
<dl>
<dd> <p> used to keep a list of extended properties </p>
 </dd></dl>
<p>type </p>
<dl>
<dd> <p> Extended Property type </p>
 </dd></dl>
<p>name_len </p>
<dl>
<dd> <p> Extended Property unicode name length, including terminating &#8216;\0&#8217; </p>
 </dd></dl>
<p>name </p>
<dl>
<dd> <p> Extended Property name </p>
 </dd></dl>
<p>data_len </p>
<dl>
<dd> <p> Length of Extended Property blob (for unicode store double len) </p>
 </dd></dl>
<p>data </p>
<dl>
<dd> <p> Extended Property blob </p>
 </dd></dl>
<p>item </p>
<dl>
<dd> <p> Represents this Extended Property in configfs </p>
 </dd></dl>
<h2>AUTHOR</h2>
<p> <code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt; </p>
<dl>
<dd> <p> Author. </p>
 </dd></dl>
<h2>COPYRIGHT</h2>
<p> <br/>
 </p>
