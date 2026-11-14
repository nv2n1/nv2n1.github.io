---
title: "inkscape-ja(1)"
name: "inkscape-ja"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inkscape-ja/"
---

<h2>名前</h2>
<p>Inkscape &#8211; <font SIZE="-1">SVG </font>(Scalable Vector Graphics) 編集プログラム</p>
<h2>書式</h2>
<p><tt>&quot;inkscape [options] [filename ...]&quot;</tt> </p>
<p> options: </p>
<pre> -?, --help 
 --usage 
 -V, --version
 -f, --file=FILENAME 
 -e, --export-png=FILENAME 
 -a, --export-area=x0:y0:x1:y1 
 -C, --export-area-page
 -D, --export-area-drawing
 --export-area-snap
 -i, --export-id=ID 
 -j, --export-id-only 
 -t, --export-use-hints
 -b, --export-background=COLOR 
 -y, --export-background-opacity=VALUE 
 -d, --export-dpi=DPI 
 -w, --export-width=WIDTH 
 -h, --export-height=HEIGHT 
 -P, --export-ps=FILENAME
 -E, --export-eps=FILENAME
 -A, --export-pdf=FILENAME
 --export-pdf-version=VERSION-STRING
 --export-latex
 --export-ps-level {2,3}
 -T, --export-text-to-path
 --export-ignore-filters
 -l, --export-plain-svg=FILENAME 
 -p, --print=PRINTER
 -I, --query-id=ID 
 -X, --query-x
 -Y, --query-y
 -W, --query-width
 -H, --query-height
 -S, --query-all
 -x, --extension-directory
 --verb-list
 --verb=VERB-ID
 --select=OBJECT-ID
 --shell
 -g, --with-gui 
 -z, --without-gui 
 --vacuum-defs
 --g-fatal-warnings</pre>
<h2>説明</h2>
<p><code>Inkscape</code> は <code>Adobe Illustrator</code>、<code>CorelDraw</code>、<code>Xara Xtreme</code> などと同等の機能を持つ <code>Scalable Vector Graphics (</code><font SIZE="-1"><code>SVG</code></font><code>)</code> 形式の描画ファイル用 <font SIZE="-1">GUI</font> エディターです。Inkscape は多彩なシェイプ、ベジエパス、フリーハンド描画、複数行テキスト、パス上テキスト、アルファブレンディング、任意のアフィン変換、グラデーションおよびパターンフィル、ノード編集、PNG や <font SIZE="-1">PDF</font> を含む多くのファイル形式に対応するインポートおよびエクスポート、グループ化、レイヤー、ライブクローンなど多くの機能を具備しています。そのインターフェイスは熟練ユーザーにとって快適で効率的であるとともに、<font SIZE="-1"><code>GNOME</code></font> 標準にも準拠するよう設計されてもいるため、他の <font SIZE="-1">GNOME</font> アプリケーションをよく知るユーザーであれば慣れるまでに多くの時間を必要としません。 </p>
<p> <font SIZE="-1"><code>SVG</code></font> は W3C 標準の 2D ベクターグラフィック用 <font SIZE="-1">XML</font> フォーマットです。描画内でポイント、パス、および基本シェイプを使用してオブジェクトを定義できます。配色、フォント、ストローク幅などは `style&#8217; 属性としてオブジェクトに指定されます。SVG は、標準であること、そのファイルは text/xml であることを意図しているため、多くのプログラムと、そして幅広い用途での利用が可能です。 </p>
<p> <code>Inkscape</code> は <font SIZE="-1">SVG</font> をその内部フォーマットとして採用しており、オープンソースコミュニティにおいてもっとも <font SIZE="-1">SVG</font> に準拠したドローイングプログラムになることを目標としています。</p>
<h2>オプション</h2>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd>ヘルプメッセージを表示します。</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Inkscape のバージョンとビルド日時を表示します。</p>
<dt><code>-a</code> <i>x0:y0:x1:y1</i>, <code>&#8211;export-area</code>=<i>x0:y0:x1:y1</i></p>
<dd><font SIZE="-1">PNG</font> エクスポートにおいて、エクスポートする領域を <font SIZE="-1">SVG</font> ユーザー単位 (通常 Inkscape <font SIZE="-1">SVG</font> 内で使用されている長さの単位) で指定します。デフォルトではドキュメント全体をエクスポートします。座標 (0,0) は左下の角になります。</p>
<dt><code>-C</code>, <code>&#8211;export-area-page</code></p>
<dd>PNG、PDF、PS、および <font SIZE="-1">EPS</font> エクスポートにおいて、エクスポート領域はそのページになります。これは PNG、PDF、および <font SIZE="-1">PS</font> ではデフォルトになるため、&#8211;export-id を使用して指定オブジェクトをエクスポートする場合を除き指定する必要はありません。対して <font SIZE="-1">EPS</font> ではこれはデフォルトになりません。さらに <font SIZE="-1">EPS</font> では、形式の指定において境界枠を内容より拡大することができません。これは、EPS エクスポート時に &#8211;export-area-page を使用した場合、ページの内容が境界枠より小さいと境界枠もそれに合わせて小さくなることを意味します。</p>
<dt><code>-D</code>, <code>&#8211;export-area-drawing</code></p>
<dd>PNG、PDF、PS、および <font SIZE="-1">EPS</font> エクスポートにおいて、エクスポートされる領域はページではなく、その描画部分、すなわち、ドキュメント内のすべてのオブジェクト (&#8211;export-id を使用した場合はエクスポートされるオブジェクト) 全体の境界枠となります。このオプションを指定すると、エクスポートされたイメージにはマージンやクロッピングがなく、ドキュメントのすべての可視オブジェクトが含まれます。EPS ではこれがデフォルトのエクスポート領域となり、&#8211;export-use-hints とともに使用することができます。</p>
<dt><code>&#8211;export-area-snap</code></p>
<dd><font SIZE="-1">PNG</font> エクスポートにおいて、エクスポート領域を拡大方向に最も近い <font SIZE="-1">SVG</font> ユーザー単位 (px) 値にスナップします。エクスポート解像度がデフォルトの 90dpi でグラフィックが最小のアンチエイリアスにピクセルスナップされた場合、エクスポートするいくつかのオブジェクトの境界枠 (&#8211;export-id または &#8211;export-area-drawing 指定) がピクセルに揃えていない場合であっても、このスイッチで配置を維持できます。</p>
<dt><code>-b</code> <i></i><font SIZE="-1"><i>COLOR</i></font><i></i>, <code>&#8211;export-background</code>=<i></i><font SIZE="-1"><i>COLOR</i></font><i></i></p>
<dd>エクスポートした <font SIZE="-1">PNG</font> の背景色になります。SVG がサポートする色指定文字列 (&#8220;#ff007f&#8221; や &#8220;rgb(255,0,128)&#8221; など) が使用できます。これを指定しない場合、Inkscape のドキュメントの設定で指定された色 (sodipodi:namedview の pagecolor= 属性) が使用されます。</p>
<dt><code>-d</code> <i></i><font SIZE="-1"><i>DPI</i></font><i></i>, <code>&#8211;export-dpi</code>=<i></i><font SIZE="-1"><i>DPI</i></font><i></i></p>
<dd><font SIZE="-1">PNG</font> エクスポートで使用される解像度になります。PS、EPS、あるいは <font SIZE="-1">PDF</font> へのエクスポート時のフィルター処理されたオブジェクトにおけるフォールバックラスタライズでも使用されます (&#8211;export-ignore-filters でラスタライズを抑止している場合を除く)。</p>
<dt><code>-e</code> <i></i><font SIZE="-1"><i>FILENAME</i></font><i></i>, <code>&#8211;export-png</code>=<i></i><font SIZE="-1"><i>FILENAME</i></font><i></i></p>
<dd><font SIZE="-1">PNG</font> エクスポート時のファイル名を指定します。同名のファイルが存在する場合、問い合わせなしに上書きされます。</p>
<dt><code>-f</code> <i></i><font SIZE="-1"><i>FILENAME</i></font><i></i>, <code>&#8211;file</code>=<i></i><font SIZE="-1"><i>FILENAME</i></font><i></i></p>
<dd>指定されたドキュメントを開きます。オプション文字 (-f) は省略できます。すなわち、オプション文字が与えられていない場合は -f が指定され、パラメーターはすべてファイル名とみなされます。</p>
<dt><code>-g</code>, <code>&#8211;with-gui</code></p>
<dd><font SIZE="-1">GUI</font> の使用を試みます (Unix の場合、$DISPLAY が設定されていない場合でも X server を使用します)。</p>
<dt><code>-h</code> <i></i><font SIZE="-1"><i>HEIGHT</i></font><i></i>, <code>&#8211;export-height</code>=<i></i><font SIZE="-1"><i>HEIGHT</i></font><i></i></p>
<dd>生成するビットマップの高さ (ピクセル) になります。この値は &#8211;export-dpi 設定 (または &#8211;export-use-hints を指定した場合の <font SIZE="-1">DPI</font> ヒント) より優先されます。</p>
<dt><code>-i</code> <i></i><font SIZE="-1"><i>ID</i></font><i></i>, <code>&#8211;export-id</code>=<i></i><font SIZE="-1"><i>ID</i></font><i></i></p>
<dd>For <font SIZE="-1">PNG, PS, EPS, PDF</font> and plain <font SIZE="-1">SVG</font> export, the id attribute value of the object that you want to export from the document; all other objects are not exported. By default the exported area is the bounding box of the object; you can override this using &#8211;export-area (<font SIZE="-1">PNG</font> only) or &#8211;export-area-page.</p>
<dt><code>-j</code>, <code>&#8211;export-id-only</code></p>
<dd>For <font SIZE="-1">PNG</font> and plain <font SIZE="-1">SVG,</font> only export the object whose id is given in &#8211;export-id. All other objects are hidden and won&#8217;t show in export even if they overlay the exported object. Without &#8211;export-id, this option is ignored. For <font SIZE="-1">PDF</font> export, this is the default, so this option has no effect.</p>
<dt><code>-l</code>, <code>&#8211;export-plain-svg</code>=<i></i><font SIZE="-1"><i>FILENAME</i></font><i></i></p>
<dd>ドキュメントをプレーン <font SIZE="-1">SVG</font> 形式にエクスポートします。sodipodi: あるいは inkscape: 名前空間や <font SIZE="-1">RDF</font> メタデータは破棄されます。</p>
<dt><code>-x</code>, <code>&#8211;extension-directory</code></p>
<dd>Inkscape が使用するよう設定されている現在のエクステンションディレクトリの一覧を表示して終了します。これは外部のエクステンションがオリジナルの Inkscape インストール場所を取得するために使用されます。</p>
<dt><code>&#8211;verb-list</code></p>
<dd>Inkscape で利用できる全 <font SIZE="-1">VERB </font>(内部コマンド) の一覧を <font SIZE="-1">ID</font> 順で表示します。この <font SIZE="-1">ID</font> はキーマップやメニューの定義で使用することができる他、&#8211;verb コマンドラインオプションでも使用できます。</p>
<dt><code>&#8211;verb</code>=<i>VERB-ID</i>, <code>&#8211;select</code>=<i>OBJECT-ID</i></p>
<dd>これら 2 つのオプションは同時に使用し、コマンドラインから Inkscape を操作できる基本的なスクリプト機能を提供します。これらはコマンドライン上で、必要であれば何度でも使用でき、指定された各ドキュメント上で順番に実行されます。 </p>
<p> &#8211;verb コマンドは指定された <font SIZE="-1">VERB</font> をメニューやボタンから呼び出した場合と同様に実行します。VERB にダイアログがある場合はそれが表示されます。使用できる <font SIZE="-1">VERB ID</font> の一覧は &#8211;verb-list コマンドで確認できます。 </p>
<p> &#8211;select コマンドは指定された <font SIZE="-1">ID</font> のオブジェクトを選択状態にします。様々な <font SIZE="-1">VERB</font> はここで指定されたオブジェクトに対して実行されます。すべての選択を解除するには &#8211;verb=EditDeselect を使用します。使用できるオブジェクト <font SIZE="-1">ID</font> は読み込まれるドキュメントに依存します。</p>
<dt><code>-p</code> <i></i><font SIZE="-1"><i>PRINTER</i></font><i></i>, <code>&#8211;print</code>=<i></i><font SIZE="-1"><i>PRINTER</i></font><i></i></p>
<dd>ドキュメントを `lpr -P <font SIZE="-1">PRINTER</font>&#8216; で指定されたプリンターで印刷します。他に、`| <font SIZE="-1">COMMAND</font>&#8216; でさまざまなコマンドへリダイレクトし、`&gt; <font SIZE="-1">FILENAME</font>&#8216; で PostScript 出力でファイルに書き出します。使用するシェルに応じた引用符で括ることを忘れないでください。 </p>
<p> 例: inkscape &#8211;print=&#8217;| ps2pdf &#8211; mydoc.pdf&#8217; mydoc.svg</p>
<dt><code>-t</code>, <code>&#8211;export-use-hints</code></p>
<dd>エクスポートしたオブジェクトに保存されているファイル名および <font SIZE="-1">DPI</font> ヒントを使用します (&#8211;export-id 使用時のみ)。これらヒントは Inkscape 内から選択範囲をエクスポートするときに自動的に設定されます。すなわち、例えば Inkscape を使用してドキュメント document.svg からオブジェクト <font SIZE="-1">ID </font>&#8220;path231&#8221; を /home/me/shape.png に解像度 300dpi でエクスポートし、ドキュメントを保存すれば、そのシェイプを同じファイル名で同じ解像度で再度エクスポートする場合は、以下の指定だけで行えます。 </p>
<p> inkscape -i path231 -t document.svg </p>
<p> &#8211;export-dpi、&#8211;export-width、あるいは &#8211;export-height をこのオプションと共に指定した場合は、DPI ヒントは無視され、コマンドラインで指定された値が使用されます。&#8211;export-png をこのオプションと共に使用した場合は、ファイル名ヒントは無視され、コマンドラインで指定されたファイル名が使用されます。</p>
<dt><code>-w</code> <i></i><font SIZE="-1"><i>WIDTH</i></font><i></i>, <code>&#8211;export-width</code>=<i></i><font SIZE="-1"><i>WIDTH</i></font><i></i></p>
<dd>生成されるビットマップの幅のピクセル数になります。この値は &#8211;export-dpi 指定 (&#8211;export-use-hints を使用した場合は <font SIZE="-1">DPI</font> ヒント) より優先されます。</p>
<dt><code>-y</code> <i></i><font SIZE="-1"><i>VALUE</i></font><i></i>, <code>&#8211;export-background-opacity</code>=<i></i><font SIZE="-1"><i>VALUE</i></font><i></i></p>
<dd>エクスポートした <font SIZE="-1">PNG</font> の背景の透明度になります。指定できる値の範囲は 0.0 から 1.0 (0.0 が完全な透明、1.0 が完全な不透明)、あるいは 1 から 255 (255 が完全な不透明) のどちらかです。このオプションを指定せず -b オプションも指定されなかった場合、 Inkscape 内のドキュメントの設定で指定された値 (sodipodi:namedview の inkscape:pageopacity= 属性)が使用されます。このオプションを指定せずに -b オプションが指定された場合、255 (完全な不透明) とみなされます。</p>
<dt><code>-P</code> <i></i><font SIZE="-1"><i>FILENAME</i></font><i></i>, <code>&#8211;export-ps</code>=<i></i><font SIZE="-1"><i>FILENAME</i></font><i></i></p>
<dd>ドキュメントを PostScript (<font SIZE="-1">PS</font>) 形式にエクスポートします。PostScript は透明度をサポートしていない点に留意してください。オリジナルの <font SIZE="-1">SVG</font> にあるいかなる透明なオブジェクトも自動的にラスタライズされます。使用しているフォントはサブセット化されて埋め込まれます。デフォルトのエクスポート領域はページになり、&#8211;export-area-drawing で描画全体に指定できます。&#8211;export-id でエクスポートするオブジェクトを 1 つ指定でき (その他はすべてエクスポートされません)、その場合はエクスポート領域はそのオブジェクトの境界枠になりますが、&#8211;export-area-page でそのページに指定できます。</p>
<dt><code>-E</code> <i></i><font SIZE="-1"><i>FILENAME</i></font><i></i>, <code>&#8211;export-eps</code>=<i></i><font SIZE="-1"><i>FILENAME</i></font><i></i></p>
<dd>ドキュメントを Encapsulated PostScript (<font SIZE="-1">EPS</font>) 形式にエクスポートします。PostScript は透明度をサポートしていない点に留意してください。オリジナルの <font SIZE="-1">SVG</font> にあるいかなる透明オブジェクトも自動的にラスタライズされます。使用しているフォントはサブセット化されて埋め込まれます。デフォルトのエクスポート領域は描画全体になり、ページに指定することも出来ますが、その場合の制限事項については &#8211;export-area-page を参照してください。&#8211;export-id でエクスポートするオブジェクトを 1 つ指定できます (その他はすべてエクスポートされません)。</p>
<dt><code>-A</code> <i></i><font SIZE="-1"><i>FILENAME</i></font><i></i>, <code>&#8211;export-pdf</code>=<i></i><font SIZE="-1"><i>FILENAME</i></font><i></i></p>
<dd>ドキュメントを <font SIZE="-1">PDF</font> 形式にエクスポートします。この形式ではオリジナル <font SIZE="-1">SVG</font> の透明度は保持されます。使用しているフォントはサブセット化され埋め込まれます。デフォルトのエクスポート領域はページになり、&#8211;export-area-drawing で描画全体に指定できます。&#8211;export-id でエクスポートするオブジェクトを 1 つ指定でき (その他はすべてエクスポートされません)、その場合はエクスポート領域はそのオブジェクトの境界枠になりますが、&#8211;export-area-page でそのページに指定できます。&quot;</p>
<dt><code>&#8211;export-pdf-version</code>=<i>PDF-VERSION</i></p>
<dd>Select the <font SIZE="-1">PDF</font> version of the exported <font SIZE="-1">PDF</font> file. This option basically exposes the <font SIZE="-1">PDF</font> version selector found in the PDF-export dialog of the <font SIZE="-1">GUI.</font> You must provide one of the versions from that combo-box, e.g. &#8220;1.4&#8221;. The default pdf export version is &#8220;1.4&#8221;.</p>
<dt><code>&#8211;export-latex</code></p>
<dd>(PS、EPS、および <font SIZE="-1">PDF</font> エクスポート用) LaTeX ドキュメント用のイメージを作成し、イメージ内のテキストは LaTeX によるタイプセットになります。PDF/PS/EPS 形式へのエクスポート時、このオプションはオリジナルの <font SIZE="-1">SVG</font> を <font SIZE="-1">PDF/PS/EPS</font> ファイル (形式は &#8211;export-pdf などで指定) と LaTeX ファイルに分割します。テキストは <font SIZE="-1">PDF/PS/EPS</font> ファイルには出力されず、LaTeX ファイルに出力されます。この LaTeX ファイルには <font SIZE="-1">PDF/PS/EPS</font> も含まれます。LaTex でこの LaTeX ファイルを入力 (\input{image.tex}) すると、イメージと共に LaTeX によってタイプセットされたテキストが表示されます。より詳しい情報は出力された実際の LaTeX ファイルを参照してください。また、GNUPlot の `epslatex&#8217; 出力ターミナルも参照してください。</p>
<dt><code>-T</code>, <code>&#8211;export-text-to-path</code></p>
<dd>該当する場合は、テキストオブジェクトをパスに変換します (PS、EPS、PDF、および <font SIZE="-1">SVG</font> エクスポート用)。</p>
<dt><code>&#8211;export-ignore-filters</code></p>
<dd>ぼかしなどのフィルターが適用されたベクターオブジェクトをエクスポートするとき、フィルターを無視します (PS、EPS、および <font SIZE="-1">PDF</font> 用)。デフォルトでは、フィルターが適用されているオブジェクトは &#8211;export-dpi で指定された解像度 (デフォルトは 90 dpi) でラスタライズされ、その外見を維持します。</p>
<dt><code>-I</code>, <code>&#8211;query-id</code></p>
<dd>サイズや座標を問い合わせたいオブジェクトの <font SIZE="-1">ID</font> を指定します。指定がない場合、ページや viewBox ではなく、描画全体 (ドキュメント内のすべてのオブジェクト) の情報を返します。</p>
<dt><code>-X</code>, <code>&#8211;query-x</code></p>
<dd>描画全体、あるいは &#8211;query-id が指定されている場合はそのオブジェクトの X 座標を問い合せます。返される値の単位は px (<font SIZE="-1">SVG</font> ユーザー単位) です。</p>
<dt><code>-Y</code>, <code>&#8211;query-y</code></p>
<dd>描画全体、あるいは &#8211;query-id が指定されている場合はそのオブジェクトの Y 座標を問い合せます。返される値の単位は px (<font SIZE="-1">SVG</font> ユーザー単位) です。</p>
<dt><code>-W</code>, <code>&#8211;query-width</code></p>
<dd>描画全体、あるいは &#8211;query-id が指定されている場合はそのオブジェクトの幅を問い合せます。返される値の単位は px (<font SIZE="-1">SVG</font> ユーザー単位) です。</p>
<dt><code>-H</code>, <code>&#8211;query-height</code></p>
<dd>描画全体、あるいは &#8211;query-id が指定されている場合はそのオブジェクトの高さを問い合せます。返される値の単位は px (<font SIZE="-1">SVG</font> ユーザー単位) です。</p>
<dt><code>-S</code>, <code>&#8211;query-all</code></p>
<dd><font SIZE="-1">SVG</font> ドキュメント内のすべてのオブジェクトの定義されている ID、X 座標、Y 座標、幅、および高さをコンマで区切った一覧を出力します。</p>
<dt><code>&#8211;shell</code></p>
<dd>このオプションを指定すると、Inkscape は対話式のコマンドラインシェルモードで起動します。このモードでは、プロンプトでコマンドを入力すると Inkscape はそれらを実行し、コマンドごとに新しく Inkscape を起動する必要がありません。このモードは主にスクリプト作成やサーバー用途で役立ちます。ここでなにか新しい機能が追加されるわけではありませんが、くり返し Inkscape を呼び出すコマンドラインでの作業 (エクスポートや変換など) は直ちに実行されることでその結果が素早く得られ、メモリ消費も抑えられます。シェルモードでも各コマンドは正しく記述されなければなりませんが、プログラム名の Inkscape の入力の必要ありません (例: &#8220;file.svg &#8211;export-pdf=file.pdf&#8221;)。</p>
<dt><code>&#8211;vacuum-defs</code></p>
<dd><font SIZE="-1">SVG</font> ファイル内の &lt;lt&gt;defs&lt;gt&gt; セクションから未使用のアイテムをすべて除去します。このオプションが &#8211;export-plain-svg とともに指定された場合、エクスポートされるファイルに対してのみ作用します。このオプションだけ指定された場合は、指定されたファイルが修正されます。</p>
<dt><code>-z</code>, <code>&#8211;without-gui</code></p>
<dd><font SIZE="-1">GUI</font> を使用せず (Unix では X server を使用しません)、コンソールからのみファイルを処理します。これは -p、-e、-l、および &#8211;vacuum-defs オプションでの使用を想定しています。</p>
<dt><code>&#8211;g-fatal-warnings</code></p>
<dd>この標準 <font SIZE="-1">GTK</font> オプションは、通常問題のないあらゆる警告でも Inkscape を中断します (デバッグ用)。</p>
<dt><code>&#8211;usage</code></p>
<dd>簡単なオプションの一覧を表示します。</dl>
<h2>設定</h2>
<p>主たる構成設定ファイルは ~/.config/inkscape/preferences.xml にあります。この中には Inkscape をカスタマイズする様々な設定情報 (そのほとんどは Inkscape の設定ダイアログにあります) があり、そのサブディレクトリには以下のようなカスタム情報を格納できます: </p>
<p> $HOME/.config/inkscape/extensions/ &#8211; エクステンション エフェクト </p>
<p> $HOME/.config/inkscape/icons/ &#8211; アイコン </p>
<p> $HOME/.config/inkscape/keys/ &#8211; キーボードマップ </p>
<p> $HOME/.config/inkscape/templates/ &#8211; 新規ファイルのテンプレート</p>
<h2>返り値</h2>
<p>このプログラムは正常に終了するとゼロを返し、異常終了すると非ゼロを返します。 </p>
<p> 様々なエラーあるいは警告メッセージが <font SIZE="-1">STDERR</font> または <font SIZE="-1">STDOUT</font> に出力されます。このプログラムが特定の <font SIZE="-1">SVG</font> において不規則な挙動を示す場合は、この出力を参照することで問題解決に役立ちます。</p>
<h2>例</h2>
<p><code>Inkscape</code> は <font SIZE="-1">GUI</font> アプリケーションとして開発されていますが、コマンドラインで <font SIZE="-1">SVG</font> を処理するためにも使用できます。 </p>
<p> <font SIZE="-1">GUI</font> で <font SIZE="-1">SVG</font> ファイルを開く: </p>
<pre> inkscape filename.svg</pre>
<p><font SIZE="-1">SVG</font> ファイルをコマンドラインから印刷する: </p>
<pre> inkscape filename.svg -p '| lpr'</pre>
<p><font SIZE="-1">SVG</font> ファイルをデフォルトの解像度である 90dpi で <font SIZE="-1">PNG</font> にエクスポートする (1 <font SIZE="-1">SVG</font> ユーザー単位は 1 ビットマップピクセルに変換されます): </p>
<pre> inkscape filename.svg --export-png=filename.png</pre>
<p>同様の処理で出力サイズを 600&#215;400 ピクセルにする: </p>
<pre> inkscape filename.svg --export-png=filename.png -w600 -h400</pre>
<p>同様の処理で、ページではなく描画全体 (すべてのオブジェクトの境界枠) をエクスポートする: </p>
<pre> inkscape filename.svg --export-png=filename.png --export-area-drawing</pre>
<p>オブジェクト &#8220;text1555&#8221; を <font SIZE="-1">PNG</font> にエクスポートする。出力ファイル名および解像度は、そのオブジェクトが最後に <font SIZE="-1">GUI</font> からエクスポートされた時の指定を利用する: </p>
<pre> inkscape filename.svg --export-id=text1555 --export-use-hints</pre>
<p>同様の処理を、解像度はデフォルトの 90dpi、ファイル名を指定、およびエクスポート領域を拡大方向に最も近い <font SIZE="-1">SVG</font> ユーザー単位 (px) 値にスナップして行う: </p>
<pre> inkscape filename.svg --export-id=text1555 --export-png=text.png --export-area-snap</pre>
<p>Inkscape <font SIZE="-1">SVG</font> ドキュメントをプレーン <font SIZE="-1">SVG</font> へ変換する: </p>
<pre> inkscape filename1.svg --export-plain-svg=filename2.svg</pre>
<p><font SIZE="-1">SVG</font> ドキュメントを <font SIZE="-1">EPS</font> へ変換する。すべてのテキストはパスへ変換する: </p>
<pre> inkscape filename.svg --export-eps=filename.eps --export-text-to-path</pre>
<p>オブジェクトID &#8220;text1555&#8221; の幅を問い合わせる: </p>
<pre> inkscape filename.svg --query-width --query-id text1555</pre>
<p>オブジェクト <font SIZE="-1">ID </font>&#8220;text1555&#8221; の複製を作成し、その複製を 90°回転し、SVG に保存して終了する: </p>
<pre> inkscape filename.svg --select=path1555 --verb=EditDuplicate --verb=ObjectRotate90 --verb=FileSave --verb=FileClose</pre>
<h2>環境変数</h2>
<p><font SIZE="-1"><code>DISPLAY</code></font> デフォルトのホストおよびディスプレイ番号を指定します。 </p>
<p> <font SIZE="-1"><code>TMPDIR</code></font> 一時ファイル用ディレクトリのデフォルトパスを指定します。ディレクトリは存在していなければなりません。 </p>
<p> <font SIZE="-1"><code>INKSCAPE_PROFILE_DIR</code></font> to set the path of the directory to use for the user profile.</p>
<h2>テーマ</h2>
<p>読み込むアイコンセットは $HOME/.config/inkscape/icons/ 配下から参照され、存在しない場合はシステムデフォルトの $PREFIX/share/inkscape/icons/icons.svg が読み込まれます。アイコンはその名前で読み込まれ (例: <i>fill_none.svg</i>)、見つからないときに <i>icons.svg</i> から使用されます。どのアイコンもどちらの場所からも見つからない場合は、システムデフォルトの場所にフォールバックします。 </p>
<p> 必要なアイコンは <font SIZE="-1">SVG</font> ファイルから <font SIZE="-1">SVG ID</font> がアイコン名とマッチするものが読み込まれます (例えば &#8220;fill_none&#8221; アイコンをファイルから読み込むときは、<i>fill_none.svg</i> か、それがなければ <i>icons.svg</i> から <font SIZE="-1">SVG ID </font>&#8220;fill_none&#8221; の境界枠がアイコンとして描画されます)。</p>
<h2>その他</h2>
<p><code>Inkscape</code> に関する公式の情報は <a rel="nofollow" href="http://www.inkscape.org/">http://www.inkscape.org/</a> にあります。このウェブサイトには、ニュース、ドキュメント、チュートリアル、作例、メーリングリスト書庫、最新バージョンのプログラム、バグおよび機能要望のデータベース、フォーラムなどがあります。</p>
<h2>関連項目</h2>
<p>potrace, cairo, <i><a href="/docs/linux/man/1-rsvg/">rsvg</a></i>(1), batik, ghostscript, pstoedit. </p>
<p> <font SIZE="-1">SVG</font> 準拠テストスイート: <a rel="nofollow" href="http://www.w3.org/Graphics/SVG/Test/">http://www.w3.org/Graphics/SVG/Test/</a> </p>
<p> <font SIZE="-1">SVG</font> 検証: <a rel="nofollow" href="http://jiggles.w3.org/svgvalidator/">http://jiggles.w3.org/svgvalidator/</a> </p>
<p> <i>Scalable Vector Graphics (</i><font SIZE="-1"><i>SVG</i></font><i>) 1.1 Specification</i> <i>W3C Recommendation 14 January 2003</i> &lt;<a rel="nofollow" href="http://www.w3.org/TR/SVG11/">http://www.w3.org/TR/SVG11/</a>&gt; </p>
<p> <i>Scalable Vector Graphics (</i><font SIZE="-1"><i>SVG</i></font><i>) 1.2 Specification</i> <i>W3C Working Draft 13 November 2003</i> &lt;<a rel="nofollow" href="http://www.w3.org/TR/SVG12/">http://www.w3.org/TR/SVG12/</a>&gt; </p>
<p> <i></i><font SIZE="-1"><i>SVG 1.1/1.2/2.0</i></font><i> Requirements</i> <i>W3C Working Draft 22 April 2002</i> &lt;<a rel="nofollow" href="http://www.w3.org/TR/SVG2Reqs/">http://www.w3.org/TR/SVG2Reqs/</a>&gt; </p>
<p> <i>Document Object Model (</i><font SIZE="-1"><i>DOM</i></font><i>): Level 2 Core</i> <i>Arnaud Le Hors et al editors, W3C</i> &lt;<a rel="nofollow" href="http://www.w3.org/TR/DOM-Level-2-Core/">http://www.w3.org/TR/DOM-Level-2-Core/</a>&gt;</p>
<h2>Gui 情報</h2>
<p>Inkscape の <font SIZE="-1">GUI</font> 操作について学ぶには、「ヘルプ」&gt;「チュートリアル」配下にあるチュートリアルを参照してください。 </p>
<p> Inkscape は <font SIZE="-1">SVG</font> 以外にも、ほとんどのビットマップ形式 (PNG、BMP、JPG、XPM、GIF など)、プレーンテキスト (Perl が必要)、PS および <font SIZE="-1">EPS </font>(Ghostscript が必要)、PDF および <font SIZE="-1">AI</font> 形式 (<font SIZE="-1">AI</font> バージョン 9.0 以降) をインポートできます (「ファイル」&gt;「インポート」)。 </p>
<p> Inkscape exports 32-bit <font SIZE="-1">PNG</font> images (File &gt; Export <font SIZE="-1">PNG</font> Image) as well as <font SIZE="-1">AI, PS, EPS, PDF, DXF,</font> and several other formats via File &gt; Save as. </p>
<p> Inkscape はグラフィックタブレットの筆圧および傾き検出に対応しており、カリグラフィツールなどでペンの幅、角度、および動きに利用できます。 </p>
<p> Inkscape はビットマップトレースエンジン Potrace (<a rel="nofollow" href="http://potrace.sf.net)">http://potrace.sf.net)</a> の <font SIZE="-1">GUI</font> フロントエンドを具備しています。 </p>
<p> Inkscape は外部スクリプト (標準入力から標準出力へのフィルター) を使用でき、それらは「エクステンション」メニューに表示されます。スクリプトはパラメーター設定のための <font SIZE="-1">GUI</font> ダイアログを持つことができ、コマンドラインを通して作用する選択オブジェクトの <font SIZE="-1">ID</font> を取得することができます。Inkscape は Python で書かれたエフェクトを各種取り揃えています。</p>
<h2>キーバインド</h2>
<p>キーボードとマウスショートカットの完全なリストは、doc/keys.html か「ヘルプ」メニューの「キーとマウスのリファレンス」から参照できます。</p>
<h2>バグ</h2>
<p>多くのバグが報告されています。ウェブサイト (inkscape.org) から報告されたものを参照し、新しく発見した問題を報告してください。お使いのバージョンのリリースノート内の Known Issues (既知の問題) セクションも参照してください。</p>
<h2>著者</h2>
<p>このコードベースは、様々な形の貢献によって成り立っています。以下のリストが完全でないことは確かなのですが、このアプリケーションが多くの方々に協力していただいていることを知るのに役立ちます。 </p>
<p> Maximilian Albert, Joshua A. Andler, Tavmjong Bah, Pierre Barbry-Blot, Jean-François Barraud, Campbell Barton, Bill Baxter, John Beard, John Bintz, Arpad Biro, Nicholas Bishop, Joshua L. Blocher, Hanno Böck, Tomasz Boczkowski, Henrik Bohre, Boldewyn, Daniel Borgmann, Bastien Bouclet, Hans Breuer, Gustav Broberg, Christopher Brown, Marcus Brubaker, Luca Bruno, Nicu Buculei, Bulia Byak, Pierre Caclin, Ian Caldwell, Gail Carmichael, Ed Catmur, Chema Celorio, Jabiertxo Arraiza Cenoz, Johan Ceuppens, Zbigniew Chyla, Alexander Clausen, John Cliff, Kees Cook, Ben Cromwell, Robert Crosbie, Jon Cruz, Aurélie De-Cooman, Kris De Gussem, Milosz Derezynski, Daniel Díaz, Bruno Dilly, Larry Doolittle, Nicolas Dufour, Tim Dwyer, Maxim V. Dziumanenko, Johan Engelen, Miklos Erdelyi, Ulf Erikson, Noé Falzon, Frank Felfe, Andrew Fitzsimon, Edward Flick, Marcin Floryan, Fred, Ben Fowler, Cedric Gemy, Steren Giannini, Olivier Gondouin, Ted Gould, Toine de Greef, Michael Grosberg, Bryce Harrington, Dale Harvey, Aurélio Adnauer Heckert, Carl Hetherington, Jos Hirth, Hannes Hochreiner, Thomas Holder, Joel Holdsworth, Christoffer Holmstedt, Alan Horkan, Karl Ove Hufthammer, Richard Hughes, Nathan Hurst, inductiveload, Thomas Ingham, Jean-Olivier Irisson, Bob Jamison, Ted Janeczko, jEsuSdA, Lauris Kaplinski, Lynn Kerby, Niko Kiirala, James Kilfiger, Nikita Kitaev, Jason Kivlighn, Adrian Knoth, Krzysztof Kosiński, Petr Kovar, Benoît Lavorata, Alex Leone, Julien Leray, Raph Levien, Diederik van Lierop, Nicklas Lindgren, Vitaly Lipatov, Ivan Louette, Fernando Lucchesi Bastos Jurema, Pierre-Antoine Marc, Aurel-Aimé Marmion, Colin Marquardt, Craig Marshall, Ivan Masár, Dmitry G. Mastrukov, David Mathog, Matiphas, Michael Meeks, Federico Mena, MenTaLguY, Aubanel Monnier, Vincent Montagne, Tim Mooney, Derek P. Moore, Chris Morgan, Peter Moulder, Jörg Müller, Yukihiro Nakai, Victor Navez, Christian Neumair, Nick, Andreas Nilsson, Mitsuru Oka, Vinícius dos Santos Oliveira, Martin Owens, Alvin Penner, Matthew Petroff, Jon Phillips, Zdenko Podobny, Alexandre Prokoudine, Jean-René Reinhard, Alexey Remizov, Frederic Rodrigo, Hugo Rodrigues, Juarez Rudsatz, Xavier Conde Rueda, Felipe Corrêa da Silva Sanches, Christian Schaller, Marco Scholten, Tom von Schwerdtner, Danilo Šegan, Abhishek Sharma, Shivaken, Michael Sloan, John Smith, Boštjan Špetič, Aaron Spike, Kaushik Sridharan, Ralf Stephan, Dariusz Stojek, Martin Sucha, ~suv, Pat Suwalski, Adib Taraben, Hugh Tebby, Jonas Termeau, David Turner, Andre Twupack, Aleksandar Urošević, Alex Valavanis, Joakim Verona, Lucas Vieites, Daniel Wagenaar, Liam P. White, Sebastian Wüst, Michael Wybrow, Gellule Xg, Daniel Yacob, David Yip, Masatake Yamato </p>
<p> This man page was put together by Bryce Harrington &lt;brycehar [at] bryceharrington.org&gt;.</p>
<h2>沿革</h2>
<p>後に Inkscape となるコードベースは 1999 年、GNOME イラストレーターアプリケーション Gill として Raph Leiven によって製作が開始されました。Gill の当初の目標は最終的に <font SIZE="-1">SVG</font> のすべてをサポートすることでした。Raph は、ストロークとフィル、線のキャップ方式、線の連結方式、テキストなどを含む PostScript ベジエイメージングモデルを実装しました。Raph の Gill のウェブページは <a rel="nofollow" href="http://www.levien.com/svg/">http://www.levien.com/svg/</a> です。Gill の開発は 2000 年には停滞したか、あるいは停止したようです。 </p>
<p> 次にこのコードベースは Lauris Kaplinski が中心となって非常に人気のあるプログラム Sodipodi に引き継がれました。コードベースは数年の作業を経ていくつかの新機能の追加、多言語サポート、Windows その他の <font SIZE="-1">OS</font> への移植、および依存関係の整理が行われ、強力なイラストレーションプログラムになりました。 </p>
<p> 2003 年、アクティブな Sodopodi 開発者であった Bryce Harrington、MenTaLguY、Nathan Hurst、および Ted Gould の 4 人は、コードベースにおける <font SIZE="-1">SVG</font> 準拠やインターフェイスのルックアンドフィールに関しての異なる方向、および参加者に開かれた開発体制をとることを目的として Inkscape を立ち上げました。 </p>
<p> プロジェクトの初期には、コードの安定化と国際化に焦点がおかれ多くの作業が行われました。Sodipodi から受け継がれたオリジナルのレンダラーには、数学的にまれですが所定の操作から外れたときに想定外のクラッシュを引き起こす数多くのケースが存在していました。このレンダラーは完全ではありませんが格段に安定性に優れた Livarot に置き換えられました。プロジェクトはまた、コードを頻繁にコミットし、ユーザーに開発中のプログラムのスナップショットを利用することを奨励する方針を採用しました。これはバグを速やかに発見し、修正の確認をユーザーが簡単に行えることに繋がりました。結果、Inkscape リリースは一般に堅牢で信頼性があるという評価を得ました。 </p>
<p> 同様に、インターフェイスの国際化とローカライズに対する取り組みも行われ、世界中からの貢献を得ることに役立ちました。 </p>
<p> Inkscape はアイコン、スプラッシュスクリーン、ウェブサイトアートなどを作成や共有するツールを提供することによってオープンソース全体の視覚的な魅力に有益な影響を及ぼしました。ある意味「ただのドローイングプログラム」であるにもかかわらず、Inkscape は、より多くの人々にオープンソースについての視覚的刺激を与える重要な役割を担っています。</p>
<h2>著作権およびライセンス</h2>
<p><code>Copyright (C)</code> 1999-2010 by Authors. </p>
<p> <code>Inkscape</code> はフリーソフトウェアです。あなたは <font SIZE="-1">GPL</font> の示す条件下においてこのプログラムを配布および/または変更できます。</p>
