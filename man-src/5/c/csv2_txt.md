---
title: "csv2_txt(5)"
name: "csv2_txt"
section: "5"
letter: "c"
url: "/docs/linux/man/5-csv2_txt/"
description: "csv2_txt – Description of txt and raw resource records in the csv2 zone file"
---

<p>csv2_txt &#8211; Description of txt and raw resource records in the csv2 zone file</p>
<h2>Description</h2>
<p>Due to the complexity of TXT and RAW records, this man page is dedicated to describing the csv2 format of this RR. TXT and RAW rrs in MaraDNSaq csv2 zone files can store any arbitrary binary data. Additionally, it is possible to arbitrarily divide up TXT records in to chunks (chunks, which RFC1035 call &quot;character-string&quot;s, are described below). <code>ASCII AND UTF-8 DATA</code> If a given TXT field or RAW record contains only ASCII data, creating a record is easy: Place the full data between single quotes, like this: </p>
<pre>a.example.com. TXT aqThis is some textaq ~</pre>
<p>It is also possible, to place almost any printable ASCII characters between quotes. The aq~aq (tilde) character is not allowed unless csv2_tilde_handling has a value of 0; the aq|aq (pipe), aq#aq (hash) and non-printable ASCII control characters are not allowed in TXT data if the ~ is used to separate records. If there are any bytes with a value of 0x80 or more, the data must be UTF-8 encoded Unicode. The printable ASCII characters not allowed in quotes are the aq character, the aq|aq character, the aq~aq (tilde) character, and the aq#aq character. See BACKSLASH ESCAPE SEQUENCES below for information on adding these characters to TXT or RAW fields. <code>UNQUOTED DATA</code> Note that the record does not have to be quoted. As long as the record only contains ASCII alphanumeric data, and/or the characters aq-aq, aq_aq, aq+aq, aq%aq, aq!aq, aq^aq, and aq=aq, the data can be unquoted as follows: </p>
<pre>c.example.com. TXT This_is_100%_unquoted_text_+symbols!</pre>
<p>It is also possible to mix quoted and unquoted text, such as this: </p>
<pre>d.example.com. TXT Thisaq is a mix aqof_unquotedaq and quoted aqtext!</pre>
<p>Which will have its data look like this: </p>
<pre>This is a mix of_unquoted and quoted text!</pre>
<p>When mixing quoted and unquoted data, it is important to have all whitespace <i>inside</i> quotes. <code>BACKSLASH ESCAPE SEQUENCES</code> In order to accommodate storing non-UTF-8 high bit characters, the single quote character, non-printable ASCII control codes, the aq|aq, aq~aq, and aq#aq characters, and to permit multi-line TXT/RAW records (with comments allowed mid-record), the TXT/RAW RR allows backslashes. These backslashes only have significance <i>outside</i> of quoted text; if they are placed inside single quotes, they are not interpreted and result in a literal backslash being added to the resource record data. The following characters can be backslashed:</p>
<dl>
<dt>aq</p>
<dd>When backslashed, the adds a literal quote to the resource record.</p>
<dt>whitespace</p>
<dd>When any whitespace is backslashed (space, newline, cr, and tab), this indicates that the record has not ended, and that more data for this recource will follow. This also allows comments to be placed in TXT and RAW resource records. What happens is that the backslash indicates that any whitespace characters (space, tab, carraige return, and line feed) are to be ignored until the next non-whitespace character that is not a # (hash). If a # is seen, this indicates that we ignore any and all characters until the next carriage return or line feed, and continue to ignore everything until the next non-whitespace character. See the section on multi-line and commented records for examples.</p>
<dt>0123</p>
<dd>When a number between 0 and 3 is backslashed, this indicates the beginning of a three-digit octal number.</p>
<dt>x</p>
<dd>When an x is backslashed, this indicates the beginning of a two-digit hexadecimal number.</dl>
<p> Note that, with the exception of the single quote, the backslash character is <i>not</i> used to remove the meta-significance of a given character. In particular, unlike other environments, it is not possible to backslash spaces. Spaces can be represented either as aq aq in quotes,  , or as  . Here are some examples of backslashed data. In this example, we see backslash sequences being used to store non-UTF-8 hi-bit data: </p>
<pre>e.example.com. TXT ���� ~</pre>
<p>This same data can also be created as follows: </p>
<pre>f.example.com. TXT \200\201\202\203 ~</pre>
<p>Octal and hex information can be mixed: </p>
<pre>g.example.com. TXT \200�\202� ~</pre>
<p>Literal single quotes can be placed in resource records: </p>
<pre>h.example.com. TXT aqperl -e aqqaqprint &quot;A Perl of a TXT record!
&quot;aqq ~</pre>
<p>The above example produces this record: </p>
<pre>perl -e aqprint &quot;A Perl of a TXT record!
&quot;aq ~</pre>
<p>To render the aq~aq character, use the escape sequence ~ (outside of quotes). For example: </p>
<pre>h1.example.com. TXT <a href="aqhttp://ocf.berkeley.edu/aq~aqsetaq">aqhttp://ocf.berkeley.edu/aq~aqsetaq</a> ~</pre>
<p>Produces this record: </p>
<pre><a rel="nofollow" href="http://ocf.berkeley.edu/~set">http://ocf.berkeley.edu/~set</a></pre>
<p>To render the aq|aq character, use the escape sequence |: </p>
<pre>h2.example.com. TXT aqls aq|aq moreaq ~</pre>
<p>Produces this record: </p>
<pre>ls | more</pre>
<p>To render the aq#aq character, use the escape sequence #: </p>
<pre>h3.example.com. TXT aqPress aq#aq for customer serviceaq ~</pre>
<p>Produces this record: </p>
<pre>Press # for customer service</pre>
<p><code>MULTI-LINE AND COMMENTED RECORDS</code> By utilizing backslashes followed by comments, it is possible to have multi-line and commented TXT and RAW records. The following resource record will span more than one line on an 80-column display: </p>
<pre>i.example.com. TXT aqNot only did the quick brown fox jump over the lazy dog, but the lazy dog jumped over the cat.aq ~</pre>
<p>Without affecting this resource record, the same data can be split over multiple lines: </p>
<pre>j.example.com. TXT aqNot only did the quick brown fox jump aq\
 aqover the lazy dog, but the lazy dogaq\
 aq jumped over the cat.aq ~</pre>
<p>Some points:</p>
<dl>
<dt>*</p>
<dd>The backslash must be outsize of the quotes (or a literal backslash will be added to the record)</p>
<dt>*</p>
<dd>The backslash must be present <i>before</i> any unquoted white space. Usually, the backslash is placed immediately after the quote character.</p>
<dt>*</p>
<dd>Unlike other environments, it does not matter whether or not there is invisible whitespace after the backslash.</dl>
<p> It is also possible to add comments after such a backslash as follows: </p>
<pre>k.example.com. TXT aqNot only did the quick brown fox jump aq\ # The fox
 aqover the lazy dog, but the lazy dogaq\ # The dog
 aq jumped over the cat.aq ~ # The cat</pre>
<p>Note that, since the third comment is not preceeded by a backslash, this indicates the end of the resource record. There can also be multiple lines dedicated to comments (and, optionally, even blank lines) in the middle of TXT and RAW record data: </p>
<pre>k2.example.com. TXT aqThis is some data aq\
# Here we have some comments followed by a blank line
# Now we have some more comments, 
# followed by the rest of the data
 aqand this is the rest of the dataaq ~</pre>
<p><code>MULTIPLE TXT CHUNKS</code> TXT RRs may be divided up in to multiple &quot;chunks&quot; (RFC1035 calls these &quot;character-string&quot;s). A single chunk can be anywhere from zero to 255 bytes long. The default is to have one chunk, as follows: </p>
<pre>o.example.com. TXT aqTXT record with only one chunkaq ~</pre>
<p>It is also possible to have a record with multiple chunks. Chunks are delimited by an unquoted aq;aq character: </p>
<pre>p.example.com. TXT aqThis is chunk oneaq;aqThis is chunk twoaq ~</pre>
<p>Or: </p>
<pre>q.example.com. TXT aqThis is chunk oneaq;\ # Our first chunk
 This_is_chunk_two;\ # Our second chunk
 aqThis is chunk threeaq ~ # Our final chunk</pre>
<p>Quoted ; characters simply add a ; to the record data. If a single TXT chunk is longer than 255 bytes long, the csv2 parser will report an error in the zone file: Single TXT chunk too long In order to resolve this, place unquoted ; characters in the record data so that each chunk is under 255 octets (bytes or characters) in length. It is possible to have zero length chunks: </p>
<pre>r.example.com. TXT aqchunk oneaq;;aqchunk threeaq ~ # Chunk two zero-length</pre>
<p>In particular, is is possible to have zero length chunks at the beginning and end of a TXT record: </p>
<pre>s.example.com. TXT ;aqchunk twoaq; ~ # Chunks one and three zero-length</pre>
<p>Do not place semicolons at the beginning nor end of TXT records unless you wish to have these zero-length chunks. Chunk support only exists for TXT records. An unquoted ; character will cause a syntax error in a RAW record. <code>RAW RECORDS</code> With the exception of no support for chunk delimiters, and the addition of a numeric record type before the record data, the format for RAW records is identical to text records. For example, if we wish to have a &quot;Kitchen Sink&quot; RR record, which has the 8-bit binary numbers &quot;16&quot;, &quot;1&quot;, and &quot;2&quot;, followed by the ASCII string &quot;Kitchen sink+ data&quot;, we can specify this in any of the following manners: </p>
<pre>t1.example.com. RAW 40 aqKitchen sinkaq+aq dataaq ~</pre>
<pre>t.example.com. RAW 40 Kitchenaq sink+ dataaq ~</pre>
<pre>u.example.com. RAW 40 Kitchen sink+ data ~</pre>
<pre>v.example.com. RAW 40 \
 aqKitchen sink+ dataaq ~</pre>
<pre>w.example.com. RAW 40 \ # Meaning: 16
 \ # Coding: 1
 \ # Sub-coding: 2
 aqKitchen sink+ dataaq ~ # Data: aqKitchen sink+ dataaq</pre>
<h2>Legal Disclaimer</h2>
<p>THIS SOFTWARE IS PROVIDED BY THE AUTHORS aqaqAS ISaqaq AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHORS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</p>
<h2>Author</h2>
<p>Sam Trenholme <a rel="nofollow" href="http://www.samiam.org/">http://www.samiam.org/</a></p>
