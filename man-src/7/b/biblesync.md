---
title: "biblesync(7)"
name: "biblesync"
section: "7"
letter: "b"
url: "/docs/linux/man/7-biblesync/"
description: "biblesync – multicast navigation synchronization in Bible programs"
---

<p>biblesync &#8211; multicast navigation synchronization in Bible programs</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;biblesync.hh&gt;

typedef enum_BibleSync_mode{

    BSP_MODE_DISABLE,

    BSP_MODE_PERSONAL,

    BSP_MODE_SPEAKER,

    BSP_MODE_AUDIENCE,

    N_BSP_MODE

} BibleSync_mode;

typedef enum_BibleSync_xmit_status{

    BSP_XMIT_OK,

    BSP_XMIT_FAILED,

    BSP_XMIT_NO_SOCKET,

    BSP_XMIT_BAD_TYPE,

    BSP_XMIT_NO_AUDIENCE_XMIT,

    BSP_XMIT_RECEIVING,

    N_BSP_XMIT

} BibleSync_xmit_status;

#define BSP_ANNOUNCE 1

#define BSP_SYNC 2

#define BSP_BEACON 3

typedef void (*BibleSync_navigate)(char cmd, string speakerkey,

                                   string bible, string ref, string alt,

                                   string group, string domain,

                                   string info, string dump);

Public interface :

    BibleSync *object = new BibleSync(string application,

                                      string version,

                                      string user);

BibleSync_mode BibleSync::setMode(BibleSync_mode mode,

                                  BibleSync_navigate *nav_func,

                                  string passPhrase);

BibleSync_mode BibleSync::getMode(void);

string BibleSync::getVersion(void);

string BibleSync::getPassphrase(void);

BibleSync_xmit_status BibleSync::Transmit(char type,

                                          string bible, string ref, string alt,

                                          string group, string domain);

static int BibleSync::Receive(void *object);

bool BibleSync::setPrivate(bool privacy);

void BibleSync::listenToSpeaker(bool listen, string speakerkey);</code></pre>
<h2>Description</h2>
<p><i>BibleSync</i> is a published protocol specification by which cooperating Bible programs navigate together. It is implemented as a C++ class providing a small, clean interface including basic setup, take-down, transmit, polled receive, and a bare few utility methods. </p>
<p> The value of <i>BibleSync</i> is found in several examples: </p>
<p> A single user may have multiple programs, or multiple computers/devices, all of which he wishes to follow along together. </p>
<p> Similarly, a group of people working closely together, such as translators, can stay together as they work. </p>
<p> In an instructional motif, <i>BibleSync</i> takes either the active or passive mode, providing for a unidirectional navigation control.</p>
<h2>Biblesync Essentials</h2>
<p><i>BibleSync</i> communicates using local multicast. Three operational modes are provided: Personal, Speaker, or Audience. </p>
<p> In Personal mode, BibleSync operates as a peer among peers, both sending and receiving navigation synchronization on the shared local multicast network. Applications are expected to respond appropriately to navigation, and to send synchronization events of their own as the user moves about his Bible. </p>
<p> In Speaker or Audience mode, <i>BibleSync</i> either transmits only (Speaker) or receives only (Audience) navigation. The Audience is expected to follow along with the Speaker&#8217;s direction. The Speaker ignores incoming navigation; the Audience transmits no navigation. </p>
<p> The difference between Personal and Speaker/Audience is thus strictly as to whether both sides of the conversation are active for each participant. </p>
<p> On startup of the protocol, BibleSync transmits a presence announcement, informing other communication partners of the application&#8217;s participation. <i>BibleSync</i> makes this announcement available to the application; whether the application shows these announcements to the user is the application designer&#8217;s choice. </p>
<p> Thereafter, as appropriate to the operational mode selected, BibleSync is tasked with polled reception of incoming navigation event packets and transmission of navigation event packets on the user&#8217;s part. </p>
<p> Transmitters (Personal and Speaker modes) issue availability beacons every 10 seconds. Received beacons for previously-unknown Speakers are handed up to the application. These beacons provide for receivers (Personal and Audience modes) to maintain a managed list of available Speakers. Furthermore, when a transmitter ceases to issue beacons, its presence in the list of available Speakers is aged out until being removed after 30 seconds of beacon silence. The application is again informed when a Speaker goes dead. </p>
<p> Default listening behavior is that the first Speaker heard via beacon is marked for listening. Other transmitters claiming Speaker status via beacon are initially ignored, but their presence is made known to the application. This provides for the application to maintain a list from which the user can select Speakers he wishes to synchronize his application. It is useful for the application to provide blanket &quot;listen to all&quot; and &quot;listen to none&quot; functions, as well as per-Speaker selections, informing <i>BibleSync</i> of these choices. In any case, this default &quot;first Speaker only&quot; policy can be overridden by the application with any other policy desired, through the use of <code>listenToSpeaker()</code> as the application designer requires. </p>
<p> Synchronization events include 5 data elements: The Bible abbreviation; the verse reference; an alternate reference (if desired; not required) which may allow the application to interpret better based on variant versification; a synchronization group identifier; and the domain. </p>
<p> The group identifier is a single digit between 1 and 9. The specification is imprecise as to this parameter&#8217;s use. The initial implementation of <i>BibleSync</i> in <i>Xiphos</i> uses the synchronization group as an indicator of the tab number in its tabbed interface: Not only is the Bible navigated, but the tab in which to navigate is selected. </p>
<p> The domain parameter is currently fixed as &quot;BIBLE-VERSE&quot;. This will be put to greater use in future revisions of the protocol. </p>
<p> <i>BibleSync</i> transmits no packet when the application leaves the conversation. </p>
<p> Only the 3 packet types BSP_ANNOUNCE, BSP_SYNC, and BSP_BEACON are defined in the protocol.</p>
<h2>Public Interface</h2>
<h3>Object creation</h3>
<p>The application must create a single BibleSync object, identifying the application&#8217;s name, its version, and the user.</p>
<h3>setMode</h3>
<p>setMode identifies how <i>BibleSync</i> should behave. The application must provide as well the navigation callback function by which <i>BibleSync</i> will inform the application of incoming events; the callback makes all the navigation parameters provided in event packets available to the application. setMode returns the resulting mode. The application provides the passphrase to be used as well; this argument defaults to &quot;&quot; (empty string), indicating that the existing passphrase should be left in place.</p>
<h3>getMode</h3>
<p>The application may request the current mode.</p>
<h3>getVersion</h3>
<p>The version string of the library itself is returned.</p>
<h3>getPassphrase</h3>
<p>Intended for use when preparing to enter any active mode, the application may request the current passphrase, so as to provide a default.</p>
<h3>Transmit</h3>
<p>The application must provide the message type, which in the normal case should be <i>BSP_SYNC.</i> The protocol requires all the indicated parameters, but all have defaults in <code>Transmit:</code> KJV, Gen.1.1, empty alternate, 1, and BIBLE-VERSE.</p>
<h3>Receive</h3>
<p>This is a static method accessible from either C or C++. It must be called with the object pointer so as to re-enter object context for the private internal receiver. <code>Receive()</code> must be called regularly (i.e. polled) as long as it continues to return TRUE. When it returns FALSE, it means that the mode has changed to BSP_MODE_DISABLE, and the scheduled polling should stop. See also the note below on polled reception.</p>
<h3>setPrivate</h3>
<p>In the circumstance where the user has multiple programs running on a single computer and does not want his navigation broadcast outside that single system, when in Personal mode, the application may also request privacy. The effect is to set multicast TTL to zero, meaning that packets will not go out on the wire.</p>
<h3>listenToSpeaker</h3>
<p>Aside from default listen behavior detailed above, the application specifically asks to listen or not to listen to specific Speakers. The key is as provided during the notification of a new Speaker.</p>
<h2>Receive Use Cases</h2>
<p>There are 6 values for the <i>cmd</i> parameter of the <i>nav_func.</i> In all cases, the <i>dump</i> parameter provides the raw content of an arriving packet.</p>
<h3>&#8216;A&#8217;</h3>
<p>Announce. A general presence message is in <i>alt,</i> and the individual elements are also available, as overloaded use of the parameters: <i>bible</i> contains the user; <i>ref</i> contains the IP address; <i>group</i> contains the application name and version; and <i>domain</i> contains the device identification.</p>
<h3>&#8216;N&#8217;</h3>
<p>Navigation. The <i>bible, ref, alt, group,</i> and <i>domain</i> parameters are presented as they arrived. <i>info</i> and <i>dump</i> are also available.</p>
<h3>&#8216;S&#8217;</h3>
<p>Speaker&#8217;s initial recognition from beacon receipt. Overloaded parameters are available as for presence announcements.</p>
<h3>&#8216;D&#8217;</h3>
<p>Dead Speaker. <i>speakerkey</i> holds the UUID key of a previously-identified application which is no longer a candidate for listening.</p>
<h3>&#8216;M&#8217;</h3>
<p>Mismatch. The incoming event packet is mismatched, either against the current passphrase or for a navigation synchronization packet when <i>BibleSync</i> is in Speaker mode. The <i>info</i> parameter begins with either &quot;announce&quot; or &quot;sync&quot;, plus the user and IP address from whom the packet came. As well, in the sync case, the regular <i>bible, ref, alt, group,</i> and <i>domain</i> parameters are available. In the announce case, the presence message is in <i>alt,</i> with overloaded individual parameters as previously described.</p>
<h3>&#8216;E&#8217;</h3>
<p>Error. This indicates network errors and malformed packets. The application&#8217;s <i>nav_func</i> is provided only the <i>info</i> and <i>dump</i> parameters.</p>
<h2>Notes</h2>
<h3>Polled reception</h3>
<p>The application must provide a means by which to poll regularly for incoming packets. In <i>Xiphos,</i> which is built on GTK and GLib, this is readily provided by mechanisms like g_timeout_add(), which sets a regular interval call of the indicated function. GLib will re-schedule the call as long as the called function returns TRUE. When it returns FALSE, GLib un-schedules the call. <code>Receive()</code> adheres to this straightforward convention. Therefore, it is imperative that every time the application moves from disabled to any non-disabled mode, Receive is again scheduled for polled use. </p>
<p> A 1-second poll interval is expected. Brief experience during development has shown that longer intervals lead to a perception of lag. </p>
<p> During every <code>Receive()</code> call, all waiting packets are processed.</p>
<h3>No datalink security</h3>
<p><i>BibleSync</i> is a protocol defined for a friendly environment. It offers no security in its current specification, and any packet sniffer such as <a href="/docs/linux/man/1-wireshark/">wireshark</a>(1) or <a href="/docs/linux/man/8-tcpdump/">tcpdump</a>(8) can see the entire conversation. The specification makes passing reference to future encryption, but at this time none is implemented.</p>
<h3>Managed Speaker lists</h3>
<p>The addition of transmitter beacons was a result of initial experience showing that it can be too easy for a user to mis-start BibleSync, or for a malicious user to interject himself into serious work. The goal of beacons is to provide a means by which, on the one hand, the user can be made aware of who is attempting to be a Speaker and, on the other hand, confine the set of Speakers whom the user will permit to make synchronization changes in the application. The simplest use of &#8216;S&#8217; new Speaker notification events is to respond with <code>listenToSpeaker(</code><i>true</i><code>, </code><i>speakerkey</i><code>)</code> which in effect makes <i>BibleSync</i> behave as though there are no beacons. More serious use of &#8216;S&#8217;/&#8217;D&#8217; is for the application to manage its own sense of available Speakers, providing a means by which the user can make sensible selections about how to react to each Speaker&#8217;s presence. <i>BibleSync</i> can be told to listen to legitimate Speakers, and to ignore interlopers, whether intended maliciously or merely due to other users&#8217; inadvertent behavior.</p>
<h3>Sending verse lists</h3>
<p>One of the better uses of <i>BibleSync</i> is in sharing verse lists. Consider a relatively weak application, perhaps on a mobile device, and a desktop-based application with strong search capability. Run searches on the desktop, and send the result via <i>BibleSync</i> to the mobile app. The <i>ref</i> parameter is not confined to a single reference. In normal citation syntax, the verse reference may consist of semicolon-separated references, comma-separated verses, and hyphen-separated ranges. Be aware that the specification has a relatively short limit on packet size, so that at most a few dozen references will be sent.</p>
<h3>Standard reference syntax</h3>
<p>It is the responsibility of the application to transmit references in standard format. <i>BibleSync</i> neither validates nor converts the application&#8217;s incoming <i>bible, ref,</i> and <i>alt</i> parameters. The specification references the BibleRef and OSIS specifications.</p>
<h2>See Also</h2>
<p><a rel="nofollow" href="http://biblesyncprotocol.wikispaces.com">http://biblesyncprotocol.wikispaces.com</a> (user &quot;General_Public&quot;, password &quot;password&quot;), <a rel="nofollow" href="http://semanticbible.com/bibleref/bibleref-specification.html,">http://semanticbible.com/bibleref/bibleref-specification.html,</a> <code><a href="/docs/linux/man/2-socket/">socket</a>(2),</code> <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a>(2),</code> <code><a href="/docs/linux/man/2-select/">select</a>(2),</code> <code><a href="/docs/linux/man/2-recvfrom/">recvfrom</a>(2),</code> <code><a href="/docs/linux/man/2-sendto/">sendto</a>(2),</code> and <code><a href="/docs/linux/man/7-ip/">ip</a>(7),</code> especially sections on <i>IP_ADD_MEMBERSHIP,</i> <i>IP_MULTICAST_IF,</i> <i>IP_MULTICAST_LOOP,</i> and <i>IP_MULTICAST_TTL.</i> </p>
