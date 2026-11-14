---
title: "libopenjp2(3)"
name: "libopenjp2"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libopenjp2/"
description: "libopenjp2 – a library for reading and writing JPEG2000 image files."
---

<h2 class="name">NAME</h2>
<p> libopenjp2 &#8211; a library for reading and writing JPEG2000 image files.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;openjpeg.h&gt;</code> </p>
<h3>CONVERSION FORMATS</h3>
<p> <code>PGX: imagetopgx() </code>/<code> pgxtoimage()</code> </p>
<p> <code>PXM: imagetopnm() </code>/<code> pnmtoimage()</code> </p>
<p> <code>BMP: imagetobmp() </code>/<code> bmptoimage()</code> </p>
<p> <code>TIF: imagetotif() </code>/<code> tiftoimage()</code> </p>
<p> <code>RAW: imagetoraw() </code>/<code> rawtoimage()</code> </p>
<p> <code>TGA: imagetotga() </code>/<code> tgatoimage()</code> </p>
<p> <code>PNG: imagetopng() </code>/<code> pngtoimage()</code> </p>
<p> <code>YUV: imagetoyuv() </code>/<code> yuvtoimage() </code>(MJ2) </p>
<h3>READ</h3>
<p> <code>opj_set_default_decoder_parameters(opj_dparameters_t *</code><i>params</i><code>);</code> </p>
<p> <code>opj_dinfo_t *opj_create_decompress(OPJ_CODEC_FORMAT </code><i>format</i><code>);</code> </p>
<p> <code>opj_event_mgr_t *opj_set_event_mgr(opj_common_ptr </code><i>info</i><code>, opj_event_mgr_t *</code><i>event_mgr</i><code>, void *</code><i>context</i><code>);</code> </p>
<p> <code>void opj_setup_decoder(opj_dinfo_t *</code><i>dinfo</i><code>, opj_dparameters_t * </code><i>params</i><code>);</code> </p>
<p> <code>opj_cio_t *opj_cio_open(opj_common_ptr </code><i>info</i><code>, unsigned char *</code><i>buf</i><code>, int </code><i>buf_len</i><code>);</code> </p>
<p> <code>opj_image_t *opj_decode(opj_dinfo_t *</code><i>dinfo</i><code>, opj_cio_t *</code><i>cio</i><code>);</code> </p>
<p> <code>void opj_cio_close(opj_cio_t *</code><i>cio</i><code>);</code> </p>
<p> <code>void opj_destroy_decompress(opj_dinfo_t *</code><i>dinfo</i><code>);</code> </p>
<p> <code>void opj_image_destroy(opj_image_t *</code><i>image</i><code>);</code> </p>
<h3>WRITE</h3>
<p> <code>void opj_set_default_encoder_parameters(opj_cparameters_t *</code><i>params</i><code>);</code> </p>
<p> /* <code>opj_image_t *FORMATtoimage(const char *</code><i>fname</i><code>, opj_cparameters_t *</code><i>params</i><code>);</code> </p>
<p> */<br />
 <code>opj_cinfo_t* opj_create_compress(OPJ_CODEC_FORMAT </code><i>format</i><code>);</code> </p>
<p> <code>opj_event_mgr_t *opj_set_event_mgr(opj_common_ptr </code><i>info</i><code>, opj_event_mgr_t *</code><i>event_mgr</i><code>, void *</code><i>context</i><code>);</code> </p>
<p> <code>void opj_setup_encoder(opj_cinfo_t *</code><i>cinfo</i><code>, opj_cparameters_t *</code><i>params</i><code>, opj_image_t *</code><i>image</i><code>);</code> </p>
<p> <code>opj_cio_t *opj_cio_open(opj_common_ptr </code><i>cinfo</i><code>, </code><i>NULL</i><code>, </code><i>0</i><code>);</code> </p>
<p> <code>bool opj_encode(opj_cinfo_t *</code><i>cinfo</i><code>, opj_cio_t *</code><i>cio</i><code>, opj_image_t *</code><i>image</i><code>, char *</code><i>index</i><code>);</code> </p>
<p> <code>void opj_cio_close(opj_cio_t *</code><i>cio</i><code>);</code> </p>
<p> <code>void opj_destroy_compress(opj_cinfo_t *</code><i>cinfo</i><code>);</code> </p>
<p> <code>void opj_image_destroy(opj_image_t *</code><i>image</i><code>);</code> </p>
<h3>GENERAL</h3>
<p> <code>void opj_image_create(int </code><i>numcmpts</i><code>, opj_image_cmptparm_t *</code><i>cmptparms</i><code>, OPJ_COLOR_SPACE </code><i>clrspc</i><code>);</code> </p>
<p> <code>int cio_tell(opj_cio_t *</code><i>cio</i><code>);</code> </p>
<p> <code>void cio_seek(opj_cio_t *</code><i>cio</i><code>, int </code><i>pos</i><code>);</code> </p>
<p> <code>opj_image_t *opj_decode_with_info(opj_dinfo_t *</code><i>dinfo</i><code>, opj_cio_t *</code><i>cio</i><code>, opj_codestream_info_t *</code><i>cstr_info</i><code>);</code> </p>
<p> <code>bool opj_encode_with_info(opj_cinfo_t *</code><i>cinfo</i><code>, opj_cio_t *</code><i>cio</i><code>, opj_image_t *</code><i>image</i><code>, opj_codestream_info_t *</code><i>cstr_info</i><code>);</code> </p>
<p> <code>void opj_destroy_cstr_info(opj_codestream_info_t *</code><i>cstr_info</i><code>);</code> </p>
<p> <code>const char *opj_version(</code><i>void</i><code>);</code> </p>
<h2>OPJ_CODEC_FORMAT</h2>
<p> <code>CODEC_J2K</code> or <code>CODEC_JPT</code> or <code>CODEC_JP2</code> </p>
<h2>OPJ_COLOR_SPACE</h2>
<p> <code>CLRSPC_UNKNOWN</code> or <code>CLRSPC_UNSPECIFIED</code> or <code>CLRSPC_SRGB</code> or <code>CLRSPC_GRAY</code> or <code>CLRSPC_SYCC</code> </p>
<h2>DECOMPRESSION PARAMETERS</h2>
<p> typedef struct opj_dparameters<br />
 {<br />
&nbsp;<wbr>/*<br />
&nbsp;<wbr>Set the number of highest resolution levels to be discarded.<br />
&nbsp;<wbr>The image resolution is effectively divided by 2 to the power&nbsp;<wbr><br />
&nbsp;<wbr>of the number of discarded levels.<br />
&nbsp;<wbr>The reduce factor is limited by the smallest total number of&nbsp;<wbr><br />
&nbsp;<wbr>decomposition levels among tiles.<br />
&nbsp;<wbr>if&nbsp;<wbr>!=&nbsp;<wbr>0, then original dimension divided by 2^(reduce);<br />
&nbsp;<wbr>if&nbsp;<wbr>==&nbsp;<wbr>0 or not used, image is decoded to the full resolution<br />
&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>cp_reduce;<br />
&nbsp;<wbr>/*<br />
&nbsp;<wbr>Set the maximum number of quality layers to decode.<br />
&nbsp;<wbr>If there are less quality layers than the specified number,&nbsp;<wbr><br />
&nbsp;<wbr>all the quality layers are decoded.<br />
&nbsp;<wbr>if&nbsp;<wbr>!=&nbsp;<wbr>0, then only the first&nbsp;<wbr>&quot;layer&quot;&nbsp;<wbr>layers are decoded;<br />
&nbsp;<wbr>if&nbsp;<wbr>==&nbsp;<wbr>0 or not used, all the quality layers are decoded<br />
&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>cp_layer; </p>
<p>&nbsp;<wbr>/*command line encoder parameters&nbsp;<wbr>(not used inside the library)&nbsp;<wbr>*/<br />
&nbsp;<wbr>/*&nbsp;<wbr>input file name&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>char</code>&nbsp;<wbr>infile[OPJ_PATH_LEN];<br />
&nbsp;<wbr>/*&nbsp;<wbr>output file name&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>char</code>&nbsp;<wbr>outfile[OPJ_PATH_LEN];<br />
&nbsp;<wbr>/*&nbsp;<wbr>input file format: see OPJ_CODEC_FORMAT&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>decod_format;<br />
&nbsp;<wbr>/*&nbsp;<wbr>output file format&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>cod_format; </p>
<p>&nbsp;<wbr>/*JPWL decoding parameters&nbsp;<wbr>*/<br />
&nbsp;<wbr>/*&nbsp;<wbr>activates the JPWL correction capabilities&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>bool</code>&nbsp;<wbr>jpwl_correct;<br />
&nbsp;<wbr>/*&nbsp;<wbr>expected number of components&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>jpwl_exp_comps;<br />
&nbsp;<wbr>/*&nbsp;<wbr>maximum number of tiles&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>jpwl_max_tiles; </p>
<p>&nbsp;<wbr>/*<br />
&nbsp;<wbr>Specify whether the decoding should be done on the entire&nbsp;<wbr><br />
&nbsp;<wbr>codestream, or be limited to the main header<br />
&nbsp;<wbr>Limiting the decoding to the main header makes it possible&nbsp;<wbr><br />
&nbsp;<wbr>to extract the characteristics of the codestream<br />
&nbsp;<wbr>if&nbsp;<wbr>==&nbsp;<wbr>NO_LIMITATION, the entire codestream is decoded;<br />
&nbsp;<wbr>if&nbsp;<wbr>==&nbsp;<wbr>LIMIT_TO_MAIN_HEADER, only the main header is decoded;<br />
&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>OPJ_LIMIT_DECODING</code>&nbsp;<wbr>cp_limit_decoding;<br />
 } opj_dparameters_t; </p>
<h2>COMPRESSION PARAMETERS</h2>
<p> typedef struct opj_cparameters<br />
 {<br />
&nbsp;<wbr>/*&nbsp;<wbr>size of tile: tile_size_on&nbsp;<wbr>=&nbsp;<wbr>false&nbsp;<wbr>(not in argument)&nbsp;<wbr><br />
&nbsp;<wbr>or tile_size_on&nbsp;<wbr>=&nbsp;<wbr>true&nbsp;<wbr>(in argument)&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>bool</code>&nbsp;<wbr>tile_size_on;<br />
&nbsp;<wbr>/*&nbsp;<wbr>XTOsiz&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>cp_tx0;<br />
&nbsp;<wbr>/*&nbsp;<wbr>YTOsiz&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>cp_ty0;<br />
&nbsp;<wbr>/*&nbsp;<wbr>XTsiz&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>cp_tdx;<br />
&nbsp;<wbr>/*&nbsp;<wbr>YTsiz&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>cp_tdy;<br />
&nbsp;<wbr>/*&nbsp;<wbr>allocation by rate/distortion&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>cp_disto_alloc;<br />
&nbsp;<wbr>/*&nbsp;<wbr>allocation by fixed layer&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>cp_fixed_alloc;<br />
&nbsp;<wbr>/*&nbsp;<wbr>add fixed_quality&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>cp_fixed_quality;<br />
&nbsp;<wbr>/*&nbsp;<wbr>fixed layer&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int&nbsp;<wbr>*</code>cp_matrice;<br />
&nbsp;<wbr>/*&nbsp;<wbr>comment for coding&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>char&nbsp;<wbr>*</code>cp_comment;<br />
&nbsp;<wbr>/*&nbsp;<wbr>coding style&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>csty;<br />
&nbsp;<wbr>/*&nbsp;<wbr>progression order:<br />
&nbsp;<wbr>PROG_UNKNOWN, LRCP(default), RLCP, RPCL, PCRL, CPRL&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>OPJ_PROG_ORDER</code>&nbsp;<wbr>prog_order;<br />
&nbsp;<wbr>/*&nbsp;<wbr>progression order changes&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>opj_poc_t</code>&nbsp;<wbr>POC[32];<br />
&nbsp;<wbr>/*&nbsp;<wbr>number of progression order changes&nbsp;<wbr>(POC), default: 0&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>numpocs;<br />
&nbsp;<wbr>/*&nbsp;<wbr>number of layers&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>tcp_numlayers;<br />
&nbsp;<wbr>/*&nbsp;<wbr>rates of layers&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>float</code>&nbsp;<wbr>tcp_rates[100];<br />
&nbsp;<wbr>/*&nbsp;<wbr>different psnr for successive layers&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>float</code>&nbsp;<wbr>tcp_distoratio[100];<br />
&nbsp;<wbr>/*&nbsp;<wbr>number of resolutions&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>numresolution;<br />
&nbsp;<wbr>/*&nbsp;<wbr>initial code block width, default: 64&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>cblockw_init;<br />
&nbsp;<wbr>/*&nbsp;<wbr>initial code block height, default: 64&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>cblockh_init;<br />
&nbsp;<wbr>/*&nbsp;<wbr>mode switch&nbsp;<wbr>(cblk_style)&nbsp;<wbr>*/<br />
&nbsp;<wbr>/*&nbsp;<wbr>1 : use the irreversible DWT 9-7,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>0 : use lossless compression&nbsp;<wbr>(default)&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>irreversible;<br />
&nbsp;<wbr>/*&nbsp;<wbr>region of interest: affected component in&nbsp;<wbr>[0..3],&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>-1 means no ROI&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>roi_compno;<br />
&nbsp;<wbr>/*&nbsp;<wbr>region of interest: upshift value&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>roi_shift;<br />
&nbsp;<wbr>/*&nbsp;<wbr>number of precinct size specifications&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>res_spec;<br />
&nbsp;<wbr>/*&nbsp;<wbr>initial precinct width&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>prcw_init[J2K_MAXRLVLS];<br />
&nbsp;<wbr>/*&nbsp;<wbr>initial precinct height&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>prch_init[J2K_MAXRLVLS]; </p>
<p>&nbsp;<wbr>/*command line encoder parameters&nbsp;<wbr>(not used inside the library)&nbsp;<wbr>*/<br />
&nbsp;<wbr>/*&nbsp;<wbr>input file name&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>char</code>&nbsp;<wbr>infile[OPJ_PATH_LEN];<br />
&nbsp;<wbr>/*&nbsp;<wbr>output file name&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>char</code>&nbsp;<wbr>outfile[OPJ_PATH_LEN];<br />
&nbsp;<wbr>/*&nbsp;<wbr>DEPRECATED. Index generation is now handeld with the&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>opj_encode_with_info()&nbsp;<wbr>function. Set to NULL&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>index_on;<br />
&nbsp;<wbr>/*&nbsp;<wbr>DEPRECATED. Index generation is now handeld with the&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>opj_encode_with_info()&nbsp;<wbr>function. Set to NULL&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>char</code>&nbsp;<wbr>index[OPJ_PATH_LEN];<br />
&nbsp;<wbr>/*&nbsp;<wbr>subimage encoding: origin image offset in x direction&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>image_offset_x0;<br />
&nbsp;<wbr>/*&nbsp;<wbr>subimage encoding: origin image offset in y direction&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>image_offset_y0;<br />
&nbsp;<wbr>/*&nbsp;<wbr>subsampling value for dx&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>subsampling_dx;<br />
&nbsp;<wbr>/*&nbsp;<wbr>subsampling value for dy&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>subsampling_dy;<br />
&nbsp;<wbr>/*&nbsp;<wbr>input file format&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>decod_format;<br />
&nbsp;<wbr>/*&nbsp;<wbr>output file format: see OPJ_CODEC_FORMAT&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>cod_format; </p>
<p>&nbsp;<wbr>/*JPWL encoding parameters&nbsp;<wbr>*/<br />
&nbsp;<wbr>/*&nbsp;<wbr>enables writing of EPC in MH, thus activating JPWL&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>bool</code>&nbsp;<wbr>jpwl_epc_on;<br />
&nbsp;<wbr>/*&nbsp;<wbr>error protection method for MH&nbsp;<wbr>(0,1,16,32,37-128)&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>jpwl_hprot_MH;<br />
&nbsp;<wbr>/*&nbsp;<wbr>tile number of header protection specification&nbsp;<wbr>(&gt;=0)&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>jpwl_hprot_TPH_tileno[JPWL_MAX_NO_TILESPECS];<br />
&nbsp;<wbr>/*&nbsp;<wbr>error protection methods for TPHs&nbsp;<wbr>(0,1,16,32,37-128)&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>jpwl_hprot_TPH[JPWL_MAX_NO_TILESPECS];<br />
&nbsp;<wbr>/*&nbsp;<wbr>tile number of packet protection specification&nbsp;<wbr>(&gt;=0)&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>jpwl_pprot_tileno[JPWL_MAX_NO_PACKSPECS];<br />
&nbsp;<wbr>/*&nbsp;<wbr>packet number of packet protection specification&nbsp;<wbr>(&gt;=0)&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>jpwl_pprot_packno[JPWL_MAX_NO_PACKSPECS];<br />
&nbsp;<wbr>/*&nbsp;<wbr>error protection methods for packets&nbsp;<wbr>(0,1,16,32,37-128)&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>jpwl_pprot[JPWL_MAX_NO_PACKSPECS];<br />
&nbsp;<wbr>/*&nbsp;<wbr>enables writing of ESD,&nbsp;<wbr>(0=no/1/2 bytes)&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>jpwl_sens_size;<br />
&nbsp;<wbr>/*&nbsp;<wbr>sensitivity addressing size&nbsp;<wbr>(0=auto/2/4 bytes)&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>jpwl_sens_addr;<br />
&nbsp;<wbr>/*&nbsp;<wbr>sensitivity range&nbsp;<wbr>(0-3)&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>jpwl_sens_range;<br />
&nbsp;<wbr>/*&nbsp;<wbr>sensitivity method for MH&nbsp;<wbr>(-1=no,0-7)&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>jpwl_sens_MH;<br />
&nbsp;<wbr>/*&nbsp;<wbr>tile number of sensitivity specification&nbsp;<wbr>(&gt;=0)&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>jpwl_sens_TPH_tileno[JPWL_MAX_NO_TILESPECS];<br />
&nbsp;<wbr>/*&nbsp;<wbr>sensitivity methods for TPHs&nbsp;<wbr>(-1=no,0-7)&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>jpwl_sens_TPH[JPWL_MAX_NO_TILESPECS]; </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>Digital Cinema compliance: OFF-not compliant,&nbsp;<wbr><br />
&nbsp;<wbr>CINEMA2K_24, CINEMA2K_48, CINEMA4K_24&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>OPJ_CINEMA_MODE</code>&nbsp;<wbr>cp_cinema;<br />
&nbsp;<wbr>/*&nbsp;<wbr>Maximum rate for each component.&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>If&nbsp;<wbr>==&nbsp;<wbr>0, component size limitation is not considered&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>int</code>&nbsp;<wbr>max_comp_size;<br />
&nbsp;<wbr>/*&nbsp;<wbr>Profile name*/<br />
&nbsp;<wbr><code>OPJ_RSIZ_CAPABILITIES</code>&nbsp;<wbr>cp_rsiz;<br />
&nbsp;<wbr>/*&nbsp;<wbr>Tile part generation*/<br />
&nbsp;<wbr><code>char</code>&nbsp;<wbr>tp_on;<br />
&nbsp;<wbr>/*&nbsp;<wbr>Flag for Tile part generation*/<br />
&nbsp;<wbr><code>char</code>&nbsp;<wbr>tp_flag;<br />
&nbsp;<wbr>/*&nbsp;<wbr>MCT&nbsp;<wbr>(multiple component transform)&nbsp;<wbr>*/<br />
&nbsp;<wbr><code>char</code>&nbsp;<wbr>tcp_mct;<br />
 } opj_cparameters_t; </p>
<h2>AUTHORS</h2>
<p> Copyright (c) 2002-2014, Universite catholique de Louvain (UCL), Belgium </p>
<p> Copyright (c) 2002-2014, Professor Benoit Macq </p>
<p> Copyright (c) 2001-2003, David Janssens </p>
<p> Copyright (c) 2002-2003, Yannick Verschueren </p>
<p> Copyright (c) 2003-2007, Francois-Olivier Devaux and Antonin Descampe </p>
<p> Copyright (c) 2005, Herve Drolon, FreeImage Team </p>
<p> Copyright (c) 2006-2007, Parvatha Elangovan </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-image_to_j2k/">image_to_j2k</a></code>(1) <code><a href="/docs/linux/man/1-j2k_to_image/">j2k_to_image</a></code>(1) <code><a href="/docs/linux/man/1-j2k_dump/">j2k_dump</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-jpwl_image_to_j2k/">JPWL_image_to_j2k</a></code>(1) <code><a href="/docs/linux/man/1-jpwl_j2k_to_image/">JPWL_j2k_to_image</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-extract_j2k_from_mj2/">extract_j2k_from_mj2</a></code>(1) <code><a href="/docs/linux/man/1-wrap_j2k_in_mj2/">wrap_j2k_in_mj2</a></code>(1) <code><a href="/docs/linux/man/1-frames_to_mj2/">frames_to_mj2</a></code>(1) <code><a href="/docs/linux/man/1-mj2_to_frames/">mj2_to_frames</a></code>(1) </p>
<h2>Index</h2>
