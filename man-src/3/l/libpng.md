---
title: "libpng(3)"
name: "libpng"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libpng/"
description: "libpng – Portable Network Graphics (PNG) Reference Library 1.5.13"
---

<h2>NAME</h2>
<p> libpng &#8211; Portable Network Graphics (PNG) Reference Library 1.5.13</p>
<h2>SYNOPSIS</h2>
<p> <i></i><code> </p>
<p> #include &lt;png.h&gt;</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_access_version_number </code><i>(void</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_benign_error (png_structp </code><i>png_ptr</i><code>, png_const_charp </code><i>error</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_build_grayscale_palette (int </code><i>bit_depth</i><code>, png_colorp </code><i>palette</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_voidp png_calloc (png_structp </code><i>png_ptr</i><code>, png_alloc_size_t </code><i>size</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_chunk_benign_error (png_structp </code><i>png_ptr</i><code>, png_const_charp </code><i>error</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_chunk_error (png_structp </code><i>png_ptr</i><code>, png_const_charp </code><i>error</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_chunk_warning (png_structp </code><i>png_ptr</i><code>, png_const_charp </code><i>message</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_convert_from_struct_tm (png_timep </code><i>ptime</i><code>, struct tm FAR * </code><i>ttime</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_convert_from_time_t (png_timep </code><i>ptime</i><code>, time_t </code><i>ttime</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_charp png_convert_to_rfc1123 (png_structp </code><i>png_ptr</i><code>, png_timep </code><i>ptime</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_infop png_create_info_struct (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_structp png_create_read_struct (png_const_charp </code><i>user_png_ver</i><code>, png_voidp </code><i>error_ptr</i><code>, png_error_ptr </code><i>error_fn</i><code>, png_error_ptr </code><i>warn_fn</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_structp png_create_read_struct_2 (png_const_charp </code><i>user_png_ver</i><code>, png_voidp </code><i>error_ptr</i><code>, png_error_ptr </code><i>error_fn</i><code>, png_error_ptr </code><i>warn_fn</i><code>, png_voidp </code><i>mem_ptr</i><code>, png_malloc_ptr </code><i>malloc_fn</i><code>, png_free_ptr </code><i>free_fn</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_structp png_create_write_struct (png_const_charp </code><i>user_png_ver</i><code>, png_voidp </code><i>error_ptr</i><code>, png_error_ptr </code><i>error_fn</i><code>, png_error_ptr </code><i>warn_fn</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_structp png_create_write_struct_2 (png_const_charp </code><i>user_png_ver</i><code>, png_voidp </code><i>error_ptr</i><code>, png_error_ptr </code><i>error_fn</i><code>, png_error_ptr </code><i>warn_fn</i><code>, png_voidp </code><i>mem_ptr</i><code>, png_malloc_ptr </code><i>malloc_fn</i><code>, png_free_ptr </code><i>free_fn</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_data_freer (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, int </code><i>freer</i><code>, png_uint_32 </code><i>mask)</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_destroy_info_struct (png_structp </code><i>png_ptr</i><code>, png_infopp </code><i>info_ptr_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_destroy_read_struct (png_structpp </code><i>png_ptr_ptr</i><code>, png_infopp </code><i>info_ptr_ptr</i><code>, png_infopp </code><i>end_info_ptr_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_destroy_write_struct (png_structpp </code><i>png_ptr_ptr</i><code>, png_infopp </code><i>info_ptr_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_err (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_error (png_structp </code><i>png_ptr</i><code>, png_const_charp </code><i>error</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_free (png_structp </code><i>png_ptr</i><code>, png_voidp </code><i>ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_free_chunk_list (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_free_default (png_structp </code><i>png_ptr</i><code>, png_voidp </code><i>ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_free_data (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, int </code><i>num</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_byte png_get_bit_depth (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_bKGD (png_const_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_color_16p </code><i>*background</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_byte png_get_channels (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_cHRM (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>, double </code><i>*white_x</i><code>, double </code><i>*white_y</i><code>, double </code><i>*red_x</i><code>, double </code><i>*red_y</i><code>, double </code><i>*green_x</i><code>, double </code><i>*green_y</i><code>, double </code><i>*blue_x</i><code>, double </code><i>*blue_y</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_cHRM_fixed (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>, png_uint_32 </code><i>*white_x</i><code>, png_uint_32 </code><i>*white_y</i><code>, png_uint_32 </code><i>*red_x</i><code>, png_uint_32 </code><i>*red_y</i><code>, png_uint_32 </code><i>*green_x</i><code>, png_uint_32 </code><i>*green_y</i><code>, png_uint_32 </code><i>*blue_x</i><code>, png_uint_32 </code><i>*blue_y</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_cHRM_XYZ (png_structp </code><i>png_ptr, </p>
<p> </i><code>png_const_infop </code><i>info_ptr</i><code>, double </code><i>*red_X</i><code>, double </code><i>*red_Y</i><code>, double </code><i>*red_Z, </p>
<p> </i><code>double </code><i>*green_X</i><code>, double </code><i>*green_Y</i><code>, double </code><i>*green_Z</i><code>, double </code><i>*blue_X, </p>
<p> </i><code>double </code><i>*blue_Y</i><code>, double </code><i>*blue_Z</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_cHRM_XYZ_fixed (png_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>, png_fixed_point </code><i>*int_red_X</i><code>, png_fixed_point </code><i>*int_red_Y</i><code>, png_fixed_point </code><i>*int_red_Z</i><code>, png_fixed_point </code><i>*int_green_X</i><code>, png_fixed_point </code><i>*int_green_Y</i><code>, png_fixed_point </code><i>*int_green_Z</i><code>, png_fixed_point </code><i>*int_blue_X</i><code>, png_fixed_point </code><i>*int_blue_Y</i><code>, png_fixed_point </code><i>*int_blue_Z</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_chunk_cache_max (png_const_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_alloc_size_t png_get_chunk_malloc_max (png_const_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_byte png_get_color_type (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_compression_buffer_size (png_const_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_byte png_get_compression_type (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_byte png_get_copyright (png_const_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_current_row_number </code><i>(png_const_structp</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_byte png_get_current_pass_number </code><i>(png_const_structp</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_voidp png_get_error_ptr (png_const_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_byte png_get_filter_type (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_gAMA (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>, double </code><i>*file_gamma</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_gAMA_fixed (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>, png_uint_32 </code><i>*int_file_gamma</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_byte png_get_header_ver (png_const_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_byte png_get_header_version (png_const_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_hIST (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>, png_uint_16p </code><i>*hist</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_iCCP (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>, png_charpp </code><i>name</i><code>, int </code><i>*compression_type</i><code>, png_bytepp </code><i>profile</i><code>, png_uint_32 </code><i>*proflen</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_IHDR (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_uint_32 </code><i>*width</i><code>, png_uint_32 </code><i>*height</i><code>, int </code><i>*bit_depth</i><code>, int </code><i>*color_type</i><code>, int </code><i>*interlace_type</i><code>, int </code><i>*compression_type</i><code>, int </code><i>*filter_type</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_image_height (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_image_width (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_int_32 png_get_int_32 (png_bytep </code><i>buf</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_byte png_get_interlace_type (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_const_bytep png_get_io_chunk_name (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_io_chunk_type (png_const_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_voidp png_get_io_ptr (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_io_state (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_byte png_get_libpng_ver (png_const_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_voidp png_get_mem_ptr (png_const_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_oFFs (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>, png_uint_32 </code><i>*offset_x</i><code>, png_uint_32 </code><i>*offset_y</i><code>, int </code><i>*unit_type</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_pCAL (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>, png_charp </code><i>*purpose</i><code>, png_int_32 </code><i>*X0</i><code>, png_int_32 </code><i>*X1</i><code>, int </code><i>*type</i><code>, int </code><i>*nparams</i><code>, png_charp </code><i>*units</i><code>, png_charpp </code><i>*params</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_pHYs (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>, png_uint_32 </code><i>*res_x</i><code>, png_uint_32 </code><i>*res_y</i><code>, int </code><i>*unit_type</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> float png_get_pixel_aspect_ratio (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_pHYs_dpi (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>, png_uint_32 </code><i>*res_x</i><code>, png_uint_32 </code><i>*res_y</i><code>, int </code><i>*unit_type</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_fixed_point png_get_pixel_aspect_ratio_fixed (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_pixels_per_inch (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_pixels_per_meter (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_voidp png_get_progressive_ptr (png_const_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_PLTE (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>, png_colorp </code><i>*palette</i><code>, int </code><i>*num_palette</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_byte png_get_rgb_to_gray_status (png_const_structp </code><i>png_ptr) </p>
<p> </i><code>png_uint_32 png_get_rowbytes (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_bytepp png_get_rows (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_sBIT (png_const_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_color_8p </code><i>*sig_bit</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_get_sCAL (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>, int* </code><i>unit</i><code>, double* </code><i>width</i><code>, double* </code><i>height</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_get_sCAL_fixed (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>, int* </code><i>unit</i><code>, png_fixed_pointp </code><i>width</i><code>, png_fixed_pointp </code><i>height</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_get_sCAL_s (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>, int* </code><i>unit</i><code>, png_charpp </code><i>width</i><code>, png_charpp </code><i>height</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_bytep png_get_signature (png_const_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_sPLT (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>, png_spalette_p </code><i>*splt_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_sRGB (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>, int </code><i>*file_srgb_intent</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_text (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>, png_textp </code><i>*text_ptr</i><code>, int </code><i>*num_text</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_tIME (png_const_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_timep </code><i>*mod_time</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_tRNS (png_const_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_bytep </code><i>*trans_alpha</i><code>, int </code><i>*num_trans</i><code>, png_color_16p </code><i>*trans_color</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> /* This function is really an inline macro. </code><i>*/ </p>
<p> </i><code>png_uint_16 png_get_uint_16 (png_bytep </code><i>buf</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_uint_31 (png_structp </code><i>png_ptr</i><code>, png_bytep </code><i>buf</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> /* This function is really an inline macro. </code><i>*/ </p>
<p> </i><code>png_uint_32 png_get_uint_32 (png_bytep </code><i>buf</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_unknown_chunks (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>, png_unknown_chunkpp </code><i>unknowns</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_voidp png_get_user_chunk_ptr (png_const_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_user_height_max (png_const_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_voidp png_get_user_transform_ptr (png_const_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_user_width_max (png_const_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_valid (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>, png_uint_32 </code><i>flag</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> float png_get_x_offset_inches (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_fixed_point png_get_x_offset_inches_fixed (png_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_int_32 png_get_x_offset_microns (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_int_32 png_get_x_offset_pixels (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_x_pixels_per_inch (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_x_pixels_per_meter (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> float png_get_y_offset_inches (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_fixed_point png_get_y_offset_inches_fixed (png_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_int_32 png_get_y_offset_microns (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_int_32 png_get_y_offset_pixels (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_y_pixels_per_inch (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_get_y_pixels_per_meter (png_const_structp </code><i>png_ptr</i><code>, png_const_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> int png_handle_as_unknown (png_structp </code><i>png_ptr</i><code>, png_bytep </code><i>chunk_name</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_info_init_3 (png_infopp </code><i>info_ptr</i><code>, png_size_t </code><i>png_info_struct_size</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_init_io (png_structp </code><i>png_ptr</i><code>, FILE </code><i>*fp</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_longjmp (png_structp </code><i>png_ptr</i><code>, int </code><i>val</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_voidp png_malloc (png_structp </code><i>png_ptr</i><code>, png_alloc_size_t </code><i>size</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_voidp png_malloc_default (png_structp </code><i>png_ptr</i><code>, png_alloc_size_t </code><i>size</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_voidp png_malloc_warn (png_structp </code><i>png_ptr</i><code>, png_alloc_size_t </code><i>size</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_permit_mng_features (png_structp </code><i>png_ptr</i><code>, png_uint_32 </code><i>mng_features_permitted</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_process_data (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_bytep </code><i>buffer</i><code>, png_size_t </code><i>buffer_size</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_size_t png_process_data_pause </code><i>(png_structp</i><code>, int </code><i>save</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_process_data_skip </code><i>(png_structp</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_progressive_combine_row (png_structp </code><i>png_ptr</i><code>, png_bytep </code><i>old_row</i><code>, png_bytep </code><i>new_row</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_read_end (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_read_image (png_structp </code><i>png_ptr</i><code>, png_bytepp </code><i>image</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_read_info (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_read_png (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, int </code><i>transforms</i><code>, png_voidp </code><i>params</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_read_row (png_structp </code><i>png_ptr</i><code>, png_bytep </code><i>row</i><code>, png_bytep </code><i>display_row</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_read_rows (png_structp </code><i>png_ptr</i><code>, png_bytepp </code><i>row</i><code>, png_bytepp </code><i>display_row</i><code>, png_uint_32 </code><i>num_rows</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_read_update_info (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> int png_reset_zstream (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_save_int_32 (png_bytep </code><i>buf</i><code>, png_int_32 </code><i>i</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_save_uint_16 (png_bytep </code><i>buf</i><code>, unsigned int </code><i>i</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_save_uint_32 (png_bytep </code><i>buf</i><code>, png_uint_32 </code><i>i</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_add_alpha (png_structp </code><i>png_ptr</i><code>, png_uint_32 </code><i>filler</i><code>, int </code><i>flags</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_alpha_mode (png_structp </code><i>png_ptr</i><code>, int </code><i>mode</i><code>, double </code><i>output_gamma</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_alpha_mode_fixed (png_structp </code><i>png_ptr</i><code>, int </code><i>mode</i><code>, png_fixed_point </code><i>output_gamma</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_background (png_structp </code><i>png_ptr</i><code>, png_color_16p </code><i>background_color</i><code>, int </code><i>background_gamma_code</i><code>, int </code><i>need_expand</i><code>, double </code><i>background_gamma</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_background_fixed (png_structp </code><i>png_ptr</i><code>, png_color_16p </code><i>background_color</i><code>, int </code><i>background_gamma_code</i><code>, int </code><i>need_expand</i><code>, png_uint_32 </code><i>background_gamma</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_benign_errors (png_structp </code><i>png_ptr</i><code>, int </code><i>allowed</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_bgr (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_bKGD (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_color_16p </code><i>background</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_check_for_invalid_index(png_structrp </code><i>png_ptr</i><code>, int </code><i>allowed</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_cHRM (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, double </code><i>white_x</i><code>, double </code><i>white_y</i><code>, double </code><i>red_x</i><code>, double </code><i>red_y</i><code>, double </code><i>green_x</i><code>, double </code><i>green_y</i><code>, double </code><i>blue_x</i><code>, double </code><i>blue_y</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_cHRM_fixed (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_uint_32 </code><i>white_x</i><code>, png_uint_32 </code><i>white_y</i><code>, png_uint_32 </code><i>red_x</i><code>, png_uint_32 </code><i>red_y</i><code>, png_uint_32 </code><i>green_x</i><code>, png_uint_32 </code><i>green_y</i><code>, png_uint_32 </code><i>blue_x</i><code>, png_uint_32 </code><i>blue_y</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_cHRM_XYZ (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, double </code><i>red_X</i><code>, double </code><i>red_Y</i><code>, double </code><i>red_Z</i><code>, double </code><i>green_X</i><code>, double </code><i>green_Y, </p>
<p> </i><code>double </code><i>green_Z</i><code>, double </code><i>blue_X</i><code>, double </code><i>blue_Y</i><code>, double </code><i>blue_Z</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_cHRM_XYZ_fixed (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_fixed_point </code><i>int_red_X</i><code>, png_fixed_point </code><i>int_red_Y</i><code>, png_fixed_point </code><i>int_red_Z</i><code>, png_fixed_point </code><i>int_green_X</i><code>, png_fixed_point </code><i>int_green_Y</i><code>, png_fixed_point </code><i>int_green_Z</i><code>, png_fixed_point </code><i>int_blue_X</i><code>, png_fixed_point </code><i>int_blue_Y</i><code>, png_fixed_point </code><i>int_blue_Z</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_chunk_cache_max (png_structp </code><i>png_ptr</i><code>, png_uint_32 </code><i>user_chunk_cache_max</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_compression_level (png_structp </code><i>png_ptr</i><code>, int </code><i>level</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_compression_mem_level (png_structp </code><i>png_ptr</i><code>, int </code><i>mem_level</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_compression_method (png_structp </code><i>png_ptr</i><code>, int </code><i>method</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_compression_strategy (png_structp </code><i>png_ptr</i><code>, int </code><i>strategy</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_compression_window_bits (png_structp </code><i>png_ptr</i><code>, int </code><i>window_bits</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_crc_action (png_structp </code><i>png_ptr</i><code>, int </code><i>crit_action</i><code>, int </code><i>ancil_action</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_error_fn (png_structp </code><i>png_ptr</i><code>, png_voidp </code><i>error_ptr</i><code>, png_error_ptr </code><i>error_fn</i><code>, png_error_ptr </code><i>warning_fn</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_expand (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_expand_16 (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_expand_gray_1_2_4_to_8 (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_filler (png_structp </code><i>png_ptr</i><code>, png_uint_32 </code><i>filler</i><code>, int </code><i>flags</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_filter (png_structp </code><i>png_ptr</i><code>, int </code><i>method</i><code>, int </code><i>filters</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_filter_heuristics (png_structp </code><i>png_ptr</i><code>, int </code><i>heuristic_method</i><code>, int </code><i>num_weights</i><code>, png_doublep </code><i>filter_weights</i><code>, png_doublep </code><i>filter_costs</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_filter_heuristics_fixed (png_structp </code><i>png_ptr</i><code>, int </code><i>heuristic_method</i><code>, int </code><i>num_weights</i><code>, png_fixed_point_p </code><i>filter_weights</i><code>, png_fixed_point_p </code><i>filter_costs</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_flush (png_structp </code><i>png_ptr</i><code>, int </code><i>nrows</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_gamma (png_structp </code><i>png_ptr</i><code>, double </code><i>screen_gamma</i><code>, double </code><i>default_file_gamma</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_gamma_fixed (png_structp </code><i>png_ptr</i><code>, png_uint_32 </code><i>screen_gamma</i><code>, png_uint_32 </code><i>default_file_gamma</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_gAMA (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, double </code><i>file_gamma</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_gAMA_fixed (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_uint_32 </code><i>file_gamma</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_gray_1_2_4_to_8 (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_gray_to_rgb (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_hIST (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_uint_16p </code><i>hist</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_iCCP (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_const_charp </code><i>name</i><code>, int </code><i>compression_type</i><code>, png_const_bytep </code><i>profile</i><code>, png_uint_32 </code><i>proflen</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> int png_set_interlace_handling (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_invalid (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, int </code><i>mask</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_invert_alpha (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_invert_mono (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_IHDR (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_uint_32 </code><i>width</i><code>, png_uint_32 </code><i>height</i><code>, int </code><i>bit_depth</i><code>, int </code><i>color_type</i><code>, int </code><i>interlace_type</i><code>, int </code><i>compression_type</i><code>, int </code><i>filter_type</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_keep_unknown_chunks (png_structp </code><i>png_ptr</i><code>, int </code><i>keep</i><code>, png_bytep </code><i>chunk_list</i><code>, int </code><i>num_chunks</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> jmp_buf* png_set_longjmp_fn (png_structp </code><i>png_ptr</i><code>, png_longjmp_ptr </code><i>longjmp_fn</i><code>, size_t </code><i>jmp_buf_size</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_chunk_malloc_max (png_structp </code><i>png_ptr</i><code>, png_alloc_size_t </code><i>user_chunk_cache_max</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_compression_buffer_size (png_structp </code><i>png_ptr</i><code>, png_uint_32 </code><i>size</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_mem_fn (png_structp </code><i>png_ptr</i><code>, png_voidp </code><i>mem_ptr</i><code>, png_malloc_ptr </code><i>malloc_fn</i><code>, png_free_ptr </code><i>free_fn</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_oFFs (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_uint_32 </code><i>offset_x</i><code>, png_uint_32 </code><i>offset_y</i><code>, int </code><i>unit_type</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_packing (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_packswap (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_palette_to_rgb (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_pCAL (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_charp </code><i>purpose</i><code>, png_int_32 </code><i>X0</i><code>, png_int_32 </code><i>X1</i><code>, int </code><i>type</i><code>, int </code><i>nparams</i><code>, png_charp </code><i>units</i><code>, png_charpp </code><i>params</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_pHYs (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_uint_32 </code><i>res_x</i><code>, png_uint_32 </code><i>res_y</i><code>, int </code><i>unit_type</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_progressive_read_fn (png_structp </code><i>png_ptr</i><code>, png_voidp </code><i>progressive_ptr</i><code>, png_progressive_info_ptr </code><i>info_fn</i><code>, png_progressive_row_ptr </code><i>row_fn</i><code>, png_progressive_end_ptr </code><i>end_fn</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_PLTE (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_colorp </code><i>palette</i><code>, int </code><i>num_palette</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_quantize (png_structp </code><i>png_ptr</i><code>, png_colorp </code><i>palette</i><code>, int </code><i>num_palette</i><code>, int </code><i>maximum_colors</i><code>, png_uint_16p </code><i>histogram</i><code>, int </code><i>full_quantize</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_read_fn (png_structp </code><i>png_ptr</i><code>, png_voidp </code><i>io_ptr</i><code>, png_rw_ptr </code><i>read_data_fn</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_read_status_fn (png_structp </code><i>png_ptr</i><code>, png_read_status_ptr </code><i>read_row_fn</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_read_user_chunk_fn (png_structp </code><i>png_ptr</i><code>, png_voidp </code><i>user_chunk_ptr</i><code>, png_user_chunk_ptr </code><i>read_user_chunk_fn</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_read_user_transform_fn (png_structp </code><i>png_ptr</i><code>, png_user_transform_ptr </code><i>read_user_transform_fn</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_rgb_to_gray (png_structp </code><i>png_ptr</i><code>, int </code><i>error_action</i><code>, double </code><i>red</i><code>, double </code><i>green</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_rgb_to_gray_fixed (png_structp </code><i>png_ptr</i><code>, int error_action png_uint_32 </code><i>red</i><code>, png_uint_32 </code><i>green</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_rows (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_bytepp </code><i>row_pointers</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_sBIT (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_color_8p </code><i>sig_bit</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_sCAL (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, int </code><i>unit</i><code>, double </code><i>width</i><code>, double </code><i>height</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_sCAL_fixed (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, int </code><i>unit</i><code>, png_fixed_point </code><i>width</i><code>, png_fixed_point </code><i>height</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_sCAL_s (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, int </code><i>unit</i><code>, png_charp </code><i>width</i><code>, png_charp </code><i>height</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_scale_16 (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_shift (png_structp </code><i>png_ptr</i><code>, png_color_8p </code><i>true_bits</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_sig_bytes (png_structp </code><i>png_ptr</i><code>, int </code><i>num_bytes</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_sPLT (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_spalette_p </code><i>splt_ptr</i><code>, int </code><i>num_spalettes</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_sRGB (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, int </code><i>srgb_intent</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_sRGB_gAMA_and_cHRM (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, int </code><i>srgb_intent</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_strip_16 (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_strip_alpha (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_strip_error_numbers (png_structp </code><i>png_ptr</i><code>, png_uint_32 </code><i>strip_mode</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_swap (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_swap_alpha (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_text (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_textp </code><i>text_ptr</i><code>, int </code><i>num_text</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_text_compression_level (png_structp </code><i>png_ptr</i><code>, int </code><i>level</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_text_compression_mem_level (png_structp </code><i>png_ptr</i><code>, int </code><i>mem_level</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_text_compression_strategy (png_structp </code><i>png_ptr</i><code>, int </code><i>strategy</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_text_compression_window_bits (png_structp </code><i>png_ptr</i><code>, int </code><i>window_bits</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void </code><i>png_set_text_compression_method</i><code>, (png_structp </code><i>png_ptr</i><code>, int </code><i>method)</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_tIME (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_timep </code><i>mod_time</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_tRNS (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_bytep </code><i>trans_alpha</i><code>, int </code><i>num_trans</i><code>, png_color_16p </code><i>trans_color</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_tRNS_to_alpha (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> png_uint_32 png_set_unknown_chunks (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, png_unknown_chunkp </code><i>unknowns</i><code>, int </code><i>num</i><code>, int </code><i>location</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_unknown_chunk_location (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, int </code><i>chunk</i><code>, int </code><i>location</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_user_limits (png_structp </code><i>png_ptr</i><code>, png_uint_32 </code><i>user_width_max</i><code>, png_uint_32 </code><i>user_height_max</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_user_transform_info (png_structp </code><i>png_ptr</i><code>, png_voidp </code><i>user_transform_ptr</i><code>, int </code><i>user_transform_depth</i><code>, int </code><i>user_transform_channels</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_write_fn (png_structp </code><i>png_ptr</i><code>, png_voidp </code><i>io_ptr</i><code>, png_rw_ptr </code><i>write_data_fn</i><code>, png_flush_ptr </code><i>output_flush_fn</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_write_status_fn (png_structp </code><i>png_ptr</i><code>, png_write_status_ptr </code><i>write_row_fn</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_set_write_user_transform_fn (png_structp </code><i>png_ptr</i><code>, png_user_transform_ptr </code><i>write_user_transform_fn</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> int png_sig_cmp (png_bytep </code><i>sig</i><code>, png_size_t </code><i>start</i><code>, png_size_t </code><i>num_to_check</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_start_read_image (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_warning (png_structp </code><i>png_ptr</i><code>, png_const_charp </code><i>message</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_write_chunk (png_structp </code><i>png_ptr</i><code>, png_bytep </code><i>chunk_name</i><code>, png_bytep </code><i>data</i><code>, png_size_t </code><i>length</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_write_chunk_data (png_structp </code><i>png_ptr</i><code>, png_bytep </code><i>data</i><code>, png_size_t </code><i>length</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_write_chunk_end (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_write_chunk_start (png_structp </code><i>png_ptr</i><code>, png_bytep </code><i>chunk_name</i><code>, png_uint_32 </code><i>length</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_write_end (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_write_flush (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_write_image (png_structp </code><i>png_ptr</i><code>, png_bytepp </code><i>image</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_write_info (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_write_info_before_PLTE (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_write_png (png_structp </code><i>png_ptr</i><code>, png_infop </code><i>info_ptr</i><code>, int </code><i>transforms</i><code>, png_voidp </code><i>params</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_write_row (png_structp </code><i>png_ptr</i><code>, png_bytep </code><i>row</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_write_rows (png_structp </code><i>png_ptr</i><code>, png_bytepp </code><i>row</i><code>, png_uint_32 </code><i>num_rows</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> void png_write_sig (png_structp </code><i>png_ptr</i><code>);</code> </p>
<p> <i></i><code> </p>
<p> </code></p>
<h2>DESCRIPTION</h2>
<p> The <i>libpng</i> library supports encoding, decoding, and various manipulations of the Portable Network Graphics (PNG) format image files. It uses the <i><a href="/docs/linux/man/3-zlib/">zlib</a>(3)</i> compression library. Following is a copy of the libpng-manual.txt file that accompanies libpng.</p>
<h2>LIBPNG.TXT</h2>
<p> Libpng-manual.txt &#8211; A description on how to use and modify libpng </p>
<p>&nbsp;<wbr>libpng version 1.5.13 &#8211; September 27, 2012<br />
&nbsp;<wbr>Updated and distributed by Glenn Randers-Pehrson<br />
&nbsp;<wbr>&lt;glennrp at users.sourceforge.net&gt;<br />
&nbsp;<wbr>Copyright&nbsp;<wbr>(c)&nbsp;<wbr>1998-2012 Glenn Randers-Pehrson </p>
<p>&nbsp;<wbr>This document is released under the libpng license.<br />
&nbsp;<wbr>For conditions of distribution and use, see the disclaimer<br />
&nbsp;<wbr>and license in png.h </p>
<p>&nbsp;<wbr>Based on: </p>
<p>&nbsp;<wbr>libpng versions 0.97, January 1998, through 1.5.13 &#8211; September 27, 2012<br />
&nbsp;<wbr>Updated and distributed by Glenn Randers-Pehrson<br />
&nbsp;<wbr>Copyright&nbsp;<wbr>(c)&nbsp;<wbr>1998-2012 Glenn Randers-Pehrson </p>
<p>&nbsp;<wbr>libpng 1.0 beta 6&nbsp;<wbr>&nbsp;<wbr>version 0.96 May 28, 1997<br />
&nbsp;<wbr>Updated and distributed by Andreas Dilger<br />
&nbsp;<wbr>Copyright&nbsp;<wbr>(c)&nbsp;<wbr>1996, 1997 Andreas Dilger </p>
<p>&nbsp;<wbr>libpng 1.0 beta 2 &#8211; version 0.88&nbsp;<wbr>&nbsp;<wbr>January 26, 1996<br />
&nbsp;<wbr>For conditions of distribution and use, see copyright<br />
&nbsp;<wbr>notice in png.h. Copyright&nbsp;<wbr>(c)&nbsp;<wbr>1995, 1996 Guy Eric<br />
&nbsp;<wbr>Schalnat, Group 42, Inc. </p>
<p>&nbsp;<wbr>Updated/rewritten per request in the libpng FAQ<br />
&nbsp;<wbr>Copyright&nbsp;<wbr>(c)&nbsp;<wbr>1995, 1996 Frank J. T. Wojcik<br />
&nbsp;<wbr>December 18, 1995&nbsp;<wbr>&amp;&nbsp;<wbr>January 20, 1996 </p>
<h2>I. Introduction</h2>
<p> This file describes how to use and modify the PNG reference library (known as libpng) for your own use. There are five sections to this file: introduction, structures, reading, writing, and modification and configuration notes for various special platforms. In addition to this file, example.c is a good starting point for using the library, as it is heavily commented and should include everything most people will need. We assume that libpng is already installed; see the INSTALL file for instructions on how to install libpng. </p>
<p> For examples of libpng usage, see the files &quot;example.c&quot;, &quot;pngtest.c&quot;, and the files in the &quot;contrib&quot; directory, all of which are included in the libpng distribution. </p>
<p> Libpng was written as a companion to the PNG specification, as a way of reducing the amount of time and effort it takes to support the PNG file format in application programs. </p>
<p> The PNG specification (second edition), November 2003, is available as a W3C Recommendation and as an ISO Standard (ISO/IEC 15948:2003 (E)) at &lt;<a rel="nofollow" href="http://www.w3.org/TR/2003/REC-PNG-20031110/">http://www.w3.org/TR/2003/REC-PNG-20031110/</a> The W3C and ISO documents have identical technical content. </p>
<p> The PNG-1.2 specification is available at &lt;<a rel="nofollow" href="http://www.libpng.org/pub/png/documents/">http://www.libpng.org/pub/png/documents/</a>&gt;. It is technically equivalent to the PNG specification (second edition) but has some additional material. </p>
<p> The PNG-1.0 specification is available as RFC 2083 &lt;<a rel="nofollow" href="http://www.libpng.org/pub/png/documents/">http://www.libpng.org/pub/png/documents/</a>&gt; and as a W3C Recommendation &lt;<a rel="nofollow" href="http://www.w3.org/TR/REC.png.html">http://www.w3.org/TR/REC.png.html</a>&gt;. </p>
<p> Some additional chunks are described in the special-purpose public chunks documents at &lt;<a rel="nofollow" href="http://www.libpng.org/pub/png/documents/">http://www.libpng.org/pub/png/documents/</a>&gt;. </p>
<p> Other information about PNG, and the latest version of libpng, can be found at the PNG home page, &lt;<a rel="nofollow" href="http://www.libpng.org/pub/png/">http://www.libpng.org/pub/png/</a>&gt;. </p>
<p> Most users will not have to modify the library significantly; advanced users may want to modify it more. All attempts were made to make it as complete as possible, while keeping the code easy to understand. Currently, this library only supports C. Support for other languages is being considered. </p>
<p> Libpng has been designed to handle multiple sessions at one time, to be easily modifiable, to be portable to the vast majority of machines (ANSI, K&amp;R, 16-, 32-, and 64-bit) available, and to be easy to use. The ultimate goal of libpng is to promote the acceptance of the PNG file format in whatever way possible. While there is still work to be done (see the TODO file), libpng should cover the majority of the needs of its users. </p>
<p> Libpng uses zlib for its compression and decompression of PNG files. Further information about zlib, and the latest version of zlib, can be found at the zlib home page, &lt;<a rel="nofollow" href="http://www.info-zip.org/pub/infozip/zlib/">http://www.info-zip.org/pub/infozip/zlib/</a>&gt;. The zlib compression utility is a general purpose utility that is useful for more than PNG files, and can be used without libpng. See the documentation delivered with zlib for more details. You can usually find the source files for the zlib utility wherever you find the libpng source files. </p>
<p> Libpng is thread safe, provided the threads are using different instances of the structures. Each thread should have its own png_struct and png_info instances, and thus its own image. Libpng does not protect itself against two threads using the same instance of a structure. </p>
<h2>II. Structures</h2>
<p> There are two main structures that are important to libpng, png_struct and png_info. Both are internal structures that are no longer exposed in the libpng interface (as of libpng 1.5.0). </p>
<p> The png_info structure is designed to provide information about the PNG file. At one time, the fields of png_info were intended to be directly accessible to the user. However, this tended to cause problems with applications using dynamically loaded libraries, and as a result a set of interface functions for png_info (the png_get_*() and png_set_*() functions) was developed, and direct access to the png_info fields was deprecated.. </p>
<p> The png_struct structure is the object used by the library to decode a single image. As of 1.5.0 this structure is also not exposed. </p>
<p> Almost all libpng APIs require a pointer to a png_struct as the first argument. Many (in particular the png_set and png_get APIs) also require a pointer to png_info as the second argument. Some application visible macros defined in png.h designed for basic data access (reading and writing integers in the PNG format) don&#8217;t take a png_info pointer, but it&#8217;s almost always safe to assume that a (png_struct*) has to be passed to call an API function. </p>
<p> You can have more than one png_info structure associated with an image, as illustrated in pngtest.c, one for information valid prior to the IDAT chunks and another (called &quot;end_info&quot; below) for things after them. </p>
<p> The png.h header file is an invaluable reference for programming with libpng. And while I&#8217;m on the topic, make sure you include the libpng header file: </p>
<p> #include &lt;png.h&gt; </p>
<p> and also (as of libpng-1.5.0) the zlib header file, if you need it: </p>
<p> #include &lt;zlib.h&gt; </p>
<h3>Types</h3>
<p> The png.h header file defines a number of integral types used by the APIs. Most of these are fairly obvious; for example types corresponding to integers of particular sizes and types for passing color values. </p>
<p> One exception is how non-integral numbers are handled. For application convenience most APIs that take such numbers have C (double) arguments; however, internally PNG, and libpng, use 32 bit signed integers and encode the value by multiplying by 100,000. As of libpng 1.5.0 a convenience macro PNG_FP_1 is defined in png.h along with a type (png_fixed_point) which is simply (png_int_32). </p>
<p> All APIs that take (double) arguments also have a matching API that takes the corresponding fixed point integer arguments. The fixed point API has the same name as the floating point one with &quot;_fixed&quot; appended. The actual range of values permitted in the APIs is frequently less than the full range of (png_fixed_point) (-21474 to +21474). When APIs require a non-negative argument the type is recorded as png_uint_32 above. Consult the header file and the text below for more information. </p>
<p> Special care must be take with sCAL chunk handling because the chunk itself uses non-integral values encoded as strings containing decimal floating point numbers. See the comments in the header file. </p>
<h3>Configuration</h3>
<p> The main header file function declarations are frequently protected by C preprocessing directives of the form: </p>
<p>&nbsp;<wbr>#ifdef PNG_feature_SUPPORTED<br />
&nbsp;<wbr>declare-function<br />
&nbsp;<wbr>#endif<br />
&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>#ifdef PNG_feature_SUPPORTED<br />
&nbsp;<wbr>use-function<br />
&nbsp;<wbr>#endif </p>
<p> The library can be built without support for these APIs, although a standard build will have all implemented APIs. Application programs should check the feature macros before using an API for maximum portability. From libpng 1.5.0 the feature macros set during the build of libpng are recorded in the header file &quot;pnglibconf.h&quot; and this file is always included by png.h. </p>
<p> If you don&#8217;t need to change the library configuration from the default, skip to the next section (&quot;Reading&quot;). </p>
<p> Notice that some of the makefiles in the &#8216;scripts&#8217; directory and (in 1.5.0) all of the build project files in the &#8216;projects&#8217; directory simply copy scripts/pnglibconf.h.prebuilt to pnglibconf.h. This means that these build systems do not permit easy auto-configuration of the library &#8211; they only support the default configuration. </p>
<p> The easiest way to make minor changes to the libpng configuration when auto-configuration is supported is to add definitions to the command line using (typically) CPPFLAGS. For example: </p>
<p> CPPFLAGS=-DPNG_NO_FLOATING_ARITHMETIC </p>
<p> will change the internal libpng math implementation for gamma correction and other arithmetic calculations to fixed point, avoiding the need for fast floating point support. The result can be seen in the generated pnglibconf.h &#8211; make sure it contains the changed feature macro setting. </p>
<p> If you need to make more extensive configuration changes &#8211; more than one or two feature macro settings &#8211; you can either add -DPNG_USER_CONFIG to the build command line and put a list of feature macro settings in pngusr.h or you can set DFA_XTRA (a makefile variable) to a file containing the same information in the form of &#8216;option&#8217; settings. </p>
<p> A. Changing pnglibconf.h </p>
<p> A variety of methods exist to build libpng. Not all of these support reconfiguration of pnglibconf.h. To reconfigure pnglibconf.h it must either be rebuilt from scripts/pnglibconf.dfa using awk or it must be edited by hand. </p>
<p> Hand editing is achieved by copying scripts/pnglibconf.h.prebuilt to pnglibconf.h and changing the lines defining the supported features, paying very close attention to the &#8216;option&#8217; information in scripts/pnglibconf.dfa that describes those features and their requirements. This is easy to get wrong. </p>
<p> B. Configuration using DFA_XTRA </p>
<p> Rebuilding from pnglibconf.dfa is easy if a functioning &#8216;awk&#8217;, or a later variant such as &#8216;nawk&#8217; or &#8216;gawk&#8217;, is available. The configure build will automatically find an appropriate awk and build pnglibconf.h. The scripts/pnglibconf.mak file contains a set of make rules for doing the same thing if configure is not used, and many of the makefiles in the scripts directory use this approach. </p>
<p> When rebuilding simply write a new file containing changed options and set DFA_XTRA to the name of this file. This causes the build to append the new file to the end of scripts/pnglibconf.dfa. The pngusr.dfa file should contain lines of the following forms: </p>
<p> everything = off </p>
<p> This turns all optional features off. Include it at the start of pngusr.dfa to make it easier to build a minimal configuration. You will need to turn at least some features on afterward to enable either reading or writing code, or both. </p>
<p> option feature on option feature off </p>
<p> Enable or disable a single feature. This will automatically enable other features required by a feature that is turned on or disable other features that require a feature which is turned off. Conflicting settings will cause an error message to be emitted by awk. </p>
<p> setting feature default value </p>
<p> Changes the default value of setting &#8216;feature&#8217; to &#8216;value&#8217;. There are a small number of settings listed at the top of pnglibconf.h, they are documented in the source code. Most of these values have performance implications for the library but most of them have no visible effect on the API. Some can also be overridden from the API. </p>
<p> This method of building a customized pnglibconf.h is illustrated in contrib/pngminim/*. See the &quot;$(PNGCONF):&quot; target in the makefile and pngusr.dfa in these directories. </p>
<p> C. Configuration using PNG_USR_CONFIG </p>
<p> If -DPNG_USR_CONFIG is added to the CFLAGS when pnglibconf.h is built the file pngusr.h will automatically be included before the options in scripts/pnglibconf.dfa are processed. Your pngusr.h file should contain only macro definitions turning features on or off or setting settings. </p>
<p> Apart from the global setting &quot;everything = off&quot; all the options listed above can be set using macros in pngusr.h: </p>
<p> #define PNG_feature_SUPPORTED </p>
<p> is equivalent to: </p>
<p> option feature on </p>
<p> #define PNG_NO_feature </p>
<p> is equivalent to: </p>
<p> option feature off </p>
<p> #define PNG_feature value </p>
<p> is equivalent to: </p>
<p> setting feature default value </p>
<p> Notice that in both cases, pngusr.dfa and pngusr.h, the contents of the pngusr file you supply override the contents of scripts/pnglibconf.dfa </p>
<p> If confusing or incomprehensible behavior results it is possible to examine the intermediate file pnglibconf.dfn to find the full set of dependency information for each setting and option. Simply locate the feature in the file and read the C comments that precede it. </p>
<p> This method is also illustrated in the contrib/pngminim/* makefiles and pngusr.h. </p>
<h2>III. Reading</h2>
<p> We&#8217;ll now walk you through the possible functions to call when reading in a PNG file sequentially, briefly explaining the syntax and purpose of each one. See example.c and png.h for more detail. While progressive reading is covered in the next section, you will still need some of the functions discussed in this section to read a PNG file. </p>
<h3>Setup</h3>
<p> You will want to do the I/O initialization(*) before you get into libpng, so if it doesn&#8217;t work, you don&#8217;t have much to undo. Of course, you will also want to insure that you are, in fact, dealing with a PNG file. Libpng provides a simple check to see if a file is a PNG file. To use it, pass in the first 1 to 8 bytes of the file to the function png_sig_cmp(), and it will return 0 (false) if the bytes match the corresponding bytes of the PNG signature, or nonzero (true) otherwise. Of course, the more bytes you pass in, the greater the accuracy of the prediction. </p>
<p> If you are intending to keep the file pointer open for use in libpng, you must ensure you don&#8217;t read more than 8 bytes from the beginning of the file, and you also have to make a call to png_set_sig_bytes_read() with the number of bytes you read from the beginning. Libpng will then only check the bytes (if any) that your program didn&#8217;t read. </p>
<p> (*): If you are not using the standard I/O functions, you will need to replace them with custom functions. See the discussion under Customizing libpng. </p>
<p>&nbsp;<wbr>FILE&nbsp;<wbr>*fp&nbsp;<wbr>=&nbsp;<wbr>fopen(file_name,&nbsp;<wbr>&quot;rb&quot;);<br />
&nbsp;<wbr>if&nbsp;<wbr>(!fp)<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>return&nbsp;<wbr>(ERROR);<br />
&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>fread(header, 1, number, fp);<br />
&nbsp;<wbr>is_png&nbsp;<wbr>=&nbsp;<wbr>!png_sig_cmp(header, 0, number); </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(!is_png)<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>return&nbsp;<wbr>(NOT_PNG);<br />
&nbsp;<wbr>} </p>
<p> Next, png_struct and png_info need to be allocated and initialized. In order to ensure that the size of these structures is correct even with a dynamically linked libpng, there are functions to initialize and allocate the structures. We also pass the library version, optional pointers to error handling functions, and a pointer to a data struct for use by the error functions, if necessary (the pointer and functions can be NULL if the default error handlers are to be used). See the section on Changes to Libpng below regarding the old initialization functions. The structure allocation functions quietly return NULL if they fail to create the structure, so your application should check for that. </p>
<p>&nbsp;<wbr>png_structp png_ptr&nbsp;<wbr>=&nbsp;<wbr>png_create_read_struct<br />
&nbsp;<wbr>&nbsp;<wbr>(PNG_LIBPNG_VER_STRING,&nbsp;<wbr>(png_voidp)user_error_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>user_error_fn, user_warning_fn); </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(!png_ptr)<br />
&nbsp;<wbr>return&nbsp;<wbr>(ERROR); </p>
<p>&nbsp;<wbr>png_infop info_ptr&nbsp;<wbr>=&nbsp;<wbr>png_create_info_struct(png_ptr); </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(!info_ptr)<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>png_destroy_read_struct(&amp;png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(png_infopp)NULL,&nbsp;<wbr>(png_infopp)NULL);<br />
&nbsp;<wbr>return&nbsp;<wbr>(ERROR);<br />
&nbsp;<wbr>} </p>
<p> If you want to use your own memory allocation routines, use a libpng that was built with PNG_USER_MEM_SUPPORTED defined, and use png_create_read_struct_2() instead of png_create_read_struct(): </p>
<p>&nbsp;<wbr>png_structp png_ptr&nbsp;<wbr>=&nbsp;<wbr>png_create_read_struct_2<br />
&nbsp;<wbr>&nbsp;<wbr>(PNG_LIBPNG_VER_STRING,&nbsp;<wbr>(png_voidp)user_error_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>user_error_fn, user_warning_fn,&nbsp;<wbr>(png_voidp)<br />
&nbsp;<wbr>&nbsp;<wbr>user_mem_ptr, user_malloc_fn, user_free_fn); </p>
<p> The error handling routines passed to png_create_read_struct() and the memory alloc/free routines passed to png_create_struct_2() are only necessary if you are not using the libpng supplied error handling and memory alloc/free functions. </p>
<p> When libpng encounters an error, it expects to longjmp back to your routine. Therefore, you will need to call setjmp and pass your png_jmpbuf(png_ptr). If you read the file from different routines, you will need to update the longjmp buffer every time you enter a new routine that will call a png_*() function. </p>
<p> See your documentation of setjmp/longjmp for your compiler for more information on setjmp/longjmp. See the discussion on libpng error handling in the Customizing Libpng section below for more information on the libpng error handling. If an error occurs, and libpng longjmp&#8217;s back to your setjmp, you will want to call png_destroy_read_struct() to free any memory. </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(setjmp(png_jmpbuf(png_ptr)))<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>png_destroy_read_struct(&amp;png_ptr,&nbsp;<wbr>&amp;info_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&amp;end_info);<br />
&nbsp;<wbr>fclose(fp);<br />
&nbsp;<wbr>return&nbsp;<wbr>(ERROR);<br />
&nbsp;<wbr>} </p>
<p> Pass (png_infopp)NULL instead of &amp;end_info if you didn&#8217;t create an end_info structure. </p>
<p> If you would rather avoid the complexity of setjmp/longjmp issues, you can compile libpng with PNG_NO_SETJMP, in which case errors will result in a call to PNG_ABORT() which defaults to abort(). </p>
<p> You can #define PNG_ABORT() to a function that does something more useful than abort(), as long as your function does not return. </p>
<p> Now you need to set up the input code. The default for libpng is to use the C function fread(). If you use this, you will need to pass a valid FILE * in the function png_init_io(). Be sure that the file is opened in binary mode. If you wish to handle reading data in another way, you need not call the png_init_io() function, but you must then implement the libpng I/O methods discussed in the Customizing Libpng section below. </p>
<p>&nbsp;<wbr>png_init_io(png_ptr, fp); </p>
<p> If you had previously opened the file and read any of the signature from the beginning in order to see if this was a PNG file, you need to let libpng know that there are some bytes missing from the start of the file. </p>
<p>&nbsp;<wbr>png_set_sig_bytes(png_ptr, number); </p>
<p> You can change the zlib compression buffer size to be used while reading compressed data with </p>
<p>&nbsp;<wbr>png_set_compression_buffer_size(png_ptr, buffer_size); </p>
<p> where the default size is 8192 bytes. Note that the buffer size is changed immediately and the buffer is reallocated immediately, instead of setting a flag to be acted upon later. </p>
<p> If you want CRC errors to be handled in a different manner than the default, use </p>
<p>&nbsp;<wbr>png_set_crc_action(png_ptr, crit_action, ancil_action); </p>
<p> The values for png_set_crc_action() say how libpng is to handle CRC errors in ancillary and critical chunks, and whether to use the data contained therein. Note that it is impossible to &quot;discard&quot; data in a critical chunk. </p>
<p> Choices for (int) crit_action are<br />
PNG_CRC_DEFAULT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>error/quit<br />
PNG_CRC_ERROR_QUIT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>error/quit<br />
PNG_CRC_WARN_USE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>warn/use data<br />
PNG_CRC_QUIET_USE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4&nbsp;<wbr>&nbsp;<wbr>quiet/use data<br />
PNG_CRC_NO_CHANGE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>5&nbsp;<wbr>&nbsp;<wbr>use the current value </p>
<p> Choices for (int) ancil_action are<br />
PNG_CRC_DEFAULT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>error/quit<br />
PNG_CRC_ERROR_QUIT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>error/quit<br />
PNG_CRC_WARN_DISCARD 2&nbsp;<wbr>&nbsp;<wbr>warn/discard data<br />
PNG_CRC_WARN_USE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>warn/use data<br />
PNG_CRC_QUIET_USE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4&nbsp;<wbr>&nbsp;<wbr>quiet/use data<br />
PNG_CRC_NO_CHANGE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>5&nbsp;<wbr>&nbsp;<wbr>use the current value </p>
<h3>Setting up callback code</h3>
<p> You can set up a callback function to handle any unknown chunks in the input stream. You must supply the function </p>
<p>&nbsp;<wbr>read_chunk_callback(png_structp png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>png_unknown_chunkp chunk);<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>/*&nbsp;<wbr>The unknown chunk structure contains your<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>chunk data, along with similar data for any other<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unknown chunks:&nbsp;<wbr>*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>png_byte name[5];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>png_byte&nbsp;<wbr>*data;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>png_size_t size; </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>Note that libpng has already taken care of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the CRC handling&nbsp;<wbr>*/ </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>put your code here.&nbsp;<wbr>&nbsp;<wbr>Search for your chunk in the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unknown chunk structure, process it, and return one<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>of the following:&nbsp;<wbr>*/ </p>
<p>&nbsp;<wbr>return&nbsp;<wbr>(-n);&nbsp;<wbr>/*&nbsp;<wbr>chunk had an error&nbsp;<wbr>*/<br />
&nbsp;<wbr>return&nbsp;<wbr>(0);&nbsp;<wbr>/*&nbsp;<wbr>did not recognize&nbsp;<wbr>*/<br />
&nbsp;<wbr>return&nbsp;<wbr>(n);&nbsp;<wbr>/*&nbsp;<wbr>success&nbsp;<wbr>*/<br />
&nbsp;<wbr>} </p>
<p> (You can give your function another name that you like instead of &quot;read_chunk_callback&quot;) </p>
<p> To inform libpng about your function, use </p>
<p>&nbsp;<wbr>png_set_read_user_chunk_fn(png_ptr, user_chunk_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>read_chunk_callback); </p>
<p> This names not only the callback function, but also a user pointer that you can retrieve with </p>
<p>&nbsp;<wbr>png_get_user_chunk_ptr(png_ptr); </p>
<p> If you call the png_set_read_user_chunk_fn() function, then all unknown chunks will be saved when read, in case your callback function will need one or more of them. This behavior can be changed with the png_set_keep_unknown_chunks() function, described below. </p>
<p> At this point, you can set up a callback function that will be called after each row has been read, which you can use to control a progress meter or the like. It&#8217;s demonstrated in pngtest.c. You must supply a function </p>
<p>&nbsp;<wbr>void read_row_callback(png_structp png_ptr,<br />
&nbsp;<wbr>png_uint_32 row, int pass);<br />
&nbsp;<wbr>{<br />
/*&nbsp;<wbr>put your code here&nbsp;<wbr>*/<br />
&nbsp;<wbr>} </p>
<p> (You can give it another name that you like instead of &quot;read_row_callback&quot;) </p>
<p> To inform libpng about your function, use </p>
<p>&nbsp;<wbr>png_set_read_status_fn(png_ptr, read_row_callback); </p>
<p> When this function is called the row has already been completely processed and the &#8216;row&#8217; and &#8216;pass&#8217; refer to the next row to be handled. For the non-interlaced case the row that was just handled is simply one less than the passed in row number, and pass will always be 0. For the interlaced case the same applies unless the row value is 0, in which case the row just handled was the last one from one of the preceding passes. Because interlacing may skip a pass you cannot be sure that the preceding pass is just &#8216;pass-1&#8217;, if you really need to know what the last pass is record (row,pass) from the callback and use the last recorded value each time. </p>
<p> As with the user transform you can find the output row using the PNG_ROW_FROM_PASS_ROW macro. </p>
<h3>Unknown-chunk handling</h3>
<p> Now you get to set the way the library processes unknown chunks in the input PNG stream. Both known and unknown chunks will be read. Normal behavior is that known chunks will be parsed into information in various info_ptr members while unknown chunks will be discarded. This behavior can be wasteful if your application will never use some known chunk types. To change this, you can call: </p>
<p>&nbsp;<wbr>png_set_keep_unknown_chunks(png_ptr, keep,<br />
&nbsp;<wbr>&nbsp;<wbr>chunk_list, num_chunks);<br />
&nbsp;<wbr>keep&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; 0: default unknown chunk handling<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1: ignore;&nbsp;<wbr>do not keep<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2: keep only if safe-to-copy<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3: keep even if unsafe-to-copy </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>You can use these definitions:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_HANDLE_CHUNK_AS_DEFAULT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_HANDLE_CHUNK_NEVER&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_HANDLE_CHUNK_IF_SAFE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_HANDLE_CHUNK_ALWAYS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3 </p>
<p>&nbsp;<wbr>chunk_list &#8211; list of chunks affected&nbsp;<wbr>(a byte string,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>five bytes per chunk, NULL or&nbsp;<wbr>&#8216;&nbsp;<wbr>&#8216;&nbsp;<wbr>if<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>num_chunks is 0) </p>
<p>&nbsp;<wbr>num_chunks &#8211; number of chunks affected;&nbsp;<wbr>if 0, all<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unknown chunks are affected.&nbsp;<wbr>&nbsp;<wbr>If nonzero,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>only the chunks in the list are affected </p>
<p> Unknown chunks declared in this way will be saved as raw data onto a list of png_unknown_chunk structures. If a chunk that is normally known to libpng is named in the list, it will be handled as unknown, according to the &quot;keep&quot; directive. If a chunk is named in successive instances of png_set_keep_unknown_chunks(), the final instance will take precedence. The IHDR and IEND chunks should not be named in chunk_list; if they are, libpng will process them normally anyway. If you know that your application will never make use of some particular chunks, use PNG_HANDLE_CHUNK_NEVER (or 1) as demonstrated below. </p>
<p> Here is an example of the usage of png_set_keep_unknown_chunks(), where the private &quot;vpAg&quot; chunk will later be processed by a user chunk callback function: </p>
<p>&nbsp;<wbr>png_byte vpAg[5]={118, 112,&nbsp;<wbr>&nbsp;<wbr>65, 103,&nbsp;<wbr>(png_byte)&nbsp;<wbr>&#8216;&nbsp;<wbr>&#8216;}; </p>
<p>&nbsp;<wbr>#if defined(PNG_UNKNOWN_CHUNKS_SUPPORTED)<br />
png_byte unused_chunks[]=<br />
{<br />
&nbsp;<wbr>&nbsp;<wbr>104,&nbsp;<wbr>&nbsp;<wbr>73,&nbsp;<wbr>&nbsp;<wbr>83,&nbsp;<wbr>&nbsp;<wbr>84,&nbsp;<wbr>(png_byte)&nbsp;<wbr>&#8216;&nbsp;<wbr>&#8216;,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>hIST&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>105,&nbsp;<wbr>&nbsp;<wbr>84,&nbsp;<wbr>&nbsp;<wbr>88, 116,&nbsp;<wbr>(png_byte)&nbsp;<wbr>&#8216;&nbsp;<wbr>&#8216;,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>iTXt&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>112,&nbsp;<wbr>&nbsp;<wbr>67,&nbsp;<wbr>&nbsp;<wbr>65,&nbsp;<wbr>&nbsp;<wbr>76,&nbsp;<wbr>(png_byte)&nbsp;<wbr>&#8216;&nbsp;<wbr>&#8216;,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>pCAL&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>115,&nbsp;<wbr>&nbsp;<wbr>67,&nbsp;<wbr>&nbsp;<wbr>65,&nbsp;<wbr>&nbsp;<wbr>76,&nbsp;<wbr>(png_byte)&nbsp;<wbr>&#8216;&nbsp;<wbr>&#8216;,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>sCAL&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>115,&nbsp;<wbr>&nbsp;<wbr>80,&nbsp;<wbr>&nbsp;<wbr>76,&nbsp;<wbr>&nbsp;<wbr>84,&nbsp;<wbr>(png_byte)&nbsp;<wbr>&#8216;&nbsp;<wbr>&#8216;,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>sPLT&nbsp;<wbr>*/<br />
&nbsp;<wbr>&nbsp;<wbr>116,&nbsp;<wbr>&nbsp;<wbr>73,&nbsp;<wbr>&nbsp;<wbr>77,&nbsp;<wbr>&nbsp;<wbr>69,&nbsp;<wbr>(png_byte)&nbsp;<wbr>&#8216;&nbsp;<wbr>&#8216;,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>tIME&nbsp;<wbr>*/<br />
};<br />
&nbsp;<wbr>#endif </p>
<p>&nbsp;<wbr>&#8230; </p>
<p>&nbsp;<wbr>#if defined(PNG_UNKNOWN_CHUNKS_SUPPORTED)<br />
/*&nbsp;<wbr>ignore all unknown chunks:&nbsp;<wbr>*/<br />
png_set_keep_unknown_chunks(read_ptr, 1, NULL, 0); </p>
<p>/*&nbsp;<wbr>except for vpAg:&nbsp;<wbr>*/<br />
png_set_keep_unknown_chunks(read_ptr, 2, vpAg, 1); </p>
<p>/*&nbsp;<wbr>also ignore unused known chunks:&nbsp;<wbr>*/<br />
png_set_keep_unknown_chunks(read_ptr, 1, unused_chunks,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(int)sizeof(unused_chunks)/5);<br />
&nbsp;<wbr>#endif </p>
<h3>User limits</h3>
<p> The PNG specification allows the width and height of an image to be as large as 2^31-1 (0x7fffffff), or about 2.147 billion rows and columns. Since very few applications really need to process such large images, we have imposed an arbitrary 1-million limit on rows and columns. Larger images will be rejected immediately with a png_error() call. If you wish to change this limit, you can use </p>
<p>png_set_user_limits(png_ptr, width_max, height_max); </p>
<p> to set your own limits, or use width_max = height_max = 0x7fffffffL to allow all valid dimensions (libpng may reject some very large images anyway because of potential buffer overflow conditions). </p>
<p> You should put this statement after you create the PNG structure and before calling png_read_info(), png_read_png(), or png_process_data(). </p>
<p> When writing a PNG datastream, put this statement before calling png_write_info() or png_write_png(). </p>
<p> If you need to retrieve the limits that are being applied, use </p>
<p>width_max&nbsp;<wbr>=&nbsp;<wbr>png_get_user_width_max(png_ptr);<br />
height_max&nbsp;<wbr>=&nbsp;<wbr>png_get_user_height_max(png_ptr); </p>
<p> The PNG specification sets no limit on the number of ancillary chunks allowed in a PNG datastream. You can impose a limit on the total number of sPLT, tEXt, iTXt, zTXt, and unknown chunks that will be stored, with </p>
<p>png_set_chunk_cache_max(png_ptr, user_chunk_cache_max); </p>
<p> where 0x7fffffffL means unlimited. You can retrieve this limit with </p>
<p>chunk_cache_max&nbsp;<wbr>=&nbsp;<wbr>png_get_chunk_cache_max(png_ptr); </p>
<p> This limit also applies to the number of buffers that can be allocated by png_decompress_chunk() while decompressing iTXt, zTXt, and iCCP chunks. </p>
<p> You can also set a limit on the amount of memory that a compressed chunk other than IDAT can occupy, with </p>
<p>png_set_chunk_malloc_max(png_ptr, user_chunk_malloc_max); </p>
<p> and you can retrieve the limit with </p>
<p>chunk_malloc_max&nbsp;<wbr>=&nbsp;<wbr>png_get_chunk_malloc_max(png_ptr); </p>
<p> Any chunks that would cause either of these limits to be exceeded will be ignored. </p>
<h3>Information about your system</h3>
<p> If you intend to display the PNG or to incorporate it in other image data you need to tell libpng information about your display or drawing surface so that libpng can convert the values in the image to match the display. </p>
<p> From libpng-1.5.4 this information can be set before reading the PNG file header. In earlier versions png_set_gamma() existed but behaved incorrectly if called before the PNG file header had been read and png_set_alpha_mode() did not exist. </p>
<p> If you need to support versions prior to libpng-1.5.4 test the version number as illustrated below using &quot;PNG_LIBPNG_VER &gt;= 10504&quot; and follow the procedures described in the appropriate manual page. </p>
<p> You give libpng the encoding expected by your system expressed as a &#8216;gamma&#8217; value. You can also specify a default encoding for the PNG file in case the required information is missing from the file. By default libpng assumes that the PNG data matches your system, to keep this default call: </p>
<p>png_set_gamma(png_ptr, screen_gamma, 1/screen_gamma/*file gamma*/); </p>
<p> or you can use the fixed point equivalent: </p>
<p>png_set_gamma_fixed(png_ptr, PNG_FP_1*screen_gamma, PNG_FP_1/screen_gamma); </p>
<p> If you don&#8217;t know the gamma for your system it is probably 2.2 &#8211; a good approximation to the IEC standard for display systems (sRGB). If images are too contrasty or washed out you got the value wrong &#8211; check your system documentation! </p>
<p> Many systems permit the system gamma to be changed via a lookup table in the display driver, a few systems, including older Macs, change the response by default. As of 1.5.4 three special values are available to handle common situations: </p>
<p>PNG_DEFAULT_sRGB: Indicates that the system conforms to the IEC 61966-2-1<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>standard.&nbsp;<wbr>&nbsp;<wbr>This matches almost all systems.<br />
PNG_GAMMA_MAC_18: Indicates that the system is an older&nbsp;<wbr>(pre Mac OS 10.6)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Apple Macintosh system with the default settings.<br />
PNG_GAMMA_LINEAR: Just the fixed point value for 1.0 &#8211; indicates that the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>system expects data with no gamma encoding. </p>
<p> You would use the linear (unencoded) value if you need to process the pixel values further because this avoids the need to decode and reencode each component value whenever arithmetic is performed. A lot of graphics software uses linear values for this reason, often with higher precision component values to preserve overall accuracy. </p>
<p> The second thing you may need to tell libpng about is how your system handles alpha channel information. Some, but not all, PNG files contain an alpha channel. To display these files correctly you need to compose the data onto a suitable background, as described in the PNG specification. </p>
<p> Libpng only supports composing onto a single color (using png_set_background; see below). Otherwise you must do the composition yourself and, in this case, you may need to call png_set_alpha_mode: </p>
<p>&nbsp;<wbr>#if PNG_LIBPNG_VER&nbsp;<wbr>&gt;=&nbsp;<wbr>10504<br />
&nbsp;<wbr>png_set_alpha_mode(png_ptr, mode, screen_gamma);<br />
&nbsp;<wbr>#else<br />
&nbsp;<wbr>png_set_gamma(png_ptr, screen_gamma, 1.0/screen_gamma);<br />
&nbsp;<wbr>#endif </p>
<p> The screen_gamma value is the same as the argument to png_set_gamma; however, how it affects the output depends on the mode. png_set_alpha_mode() sets the file gamma default to 1/screen_gamma, so normally you don&#8217;t need to call png_set_gamma. If you need different defaults call png_set_gamma() before png_set_alpha_mode() &#8211; if you call it after it will override the settings made by png_set_alpha_mode(). </p>
<p> The mode is as follows: </p>
<p>&nbsp;<wbr>PNG_ALPHA_PNG: The data is encoded according to the PNG specification.&nbsp;<wbr>&nbsp;<wbr>Red, green and blue, or gray, components are gamma encoded color values and are not premultiplied by the alpha value. The alpha value is a linear measure of the contribution of the pixel to the corresponding final output pixel. </p>
<p> You should normally use this format if you intend to perform color correction on the color values; most, maybe all, color correction software has no handling for the alpha channel and, anyway, the math to handle pre-multiplied component values is unnecessarily complex. </p>
<p> Before you do any arithmetic on the component values you need to remove the gamma encoding and multiply out the alpha channel. See the PNG specification for more detail. It is important to note that when an image with an alpha channel is scaled, linear encoded, pre-multiplied component values must be used! </p>
<p> The remaining modes assume you don&#8217;t need to do any further color correction or that if you do, your color correction software knows all about alpha (it probably doesn&#8217;t!) </p>
<p>&nbsp;<wbr>PNG_ALPHA_STANDARD:&nbsp;<wbr>&nbsp;<wbr>The data libpng produces is encoded in the standard way assumed by most correctly written graphics software. The gamma encoding will be removed by libpng and the linear component values will be pre-multiplied by the alpha channel. </p>
<p> With this format the final image must be re-encoded to match the display gamma before the image is displayed. If your system doesn&#8217;t do that, yet still seems to perform arithmetic on the pixels without decoding them, it is broken &#8211; check out the modes below. </p>
<p> With PNG_ALPHA_STANDARD libpng always produces linear component values, whatever screen_gamma you supply. The screen_gamma value is, however, used as a default for the file gamma if the PNG file has no gamma information. </p>
<p> If you call png_set_gamma() after png_set_alpha_mode() you will override the linear encoding. Instead the pre-multiplied pixel values will be gamma encoded but the alpha channel will still be linear. This may actually match the requirements of some broken software, but it is unlikely. </p>
<p> While linear 8-bit data is often used it has insufficient precision for any image with a reasonable dynamic range. To avoid problems, and if your software supports it, use png_set_expand_16() to force all components to 16 bits. </p>
<p>&nbsp;<wbr>PNG_ALPHA_OPTIMIZED: This mode is the same as PNG_ALPHA_STANDARD except that completely opaque pixels are gamma encoded according to the screen_gamma value. Pixels with alpha less than 1.0 will still have linear components. </p>
<p> Use this format if you have control over your compositing software and so don&#8217;t do other arithmetic (such as scaling) on the data you get from libpng. Your compositing software can simply copy opaque pixels to the output but still has linear values for the non-opaque pixels. </p>
<p> In normal compositing, where the alpha channel encodes partial pixel coverage (as opposed to broad area translucency), the inaccuracies of the 8-bit representation of non-opaque pixels are irrelevant. </p>
<p> You can also try this format if your software is broken; it might look better. </p>
<p>&nbsp;<wbr>PNG_ALPHA_BROKEN: This is PNG_ALPHA_STANDARD; however, all component values, including the alpha channel are gamma encoded. This is an appropriate format to try if your software, or more likely hardware, is totally broken, i.e., if it performs linear arithmetic directly on gamma encoded values. </p>
<p> In most cases of broken software or hardware the bug in the final display manifests as a subtle halo around composited parts of the image. You may not even perceive this as a halo; the composited part of the image may simply appear separate from the background, as though it had been cut out of paper and pasted on afterward. </p>
<p> If you don&#8217;t have to deal with bugs in software or hardware, or if you can fix them, there are three recommended ways of using png_set_alpha_mode(): </p>
<p>png_set_alpha_mode(png_ptr, PNG_ALPHA_PNG,<br />
&nbsp;<wbr>screen_gamma); </p>
<p> You can do color correction on the result (libpng does not currently support color correction internally). When you handle the alpha channel you need to undo the gamma encoding and multiply out the alpha. </p>
<p>png_set_alpha_mode(png_ptr, PNG_ALPHA_STANDARD,<br />
&nbsp;<wbr>screen_gamma);<br />
png_set_expand_16(png_ptr); </p>
<p> If you are using the high level interface, don&#8217;t call png_set_expand_16(); instead pass PNG_TRANSFORM_EXPAND_16 to the interface. </p>
<p> With this mode you can&#8217;t do color correction, but you can do arithmetic, including composition and scaling, on the data without further processing. </p>
<p>png_set_alpha_mode(png_ptr, PNG_ALPHA_OPTIMIZED,<br />
&nbsp;<wbr>screen_gamma); </p>
<p> You can avoid the expansion to 16-bit components with this mode, but you lose the ability to scale the image or perform other linear arithmetic. All you can do is compose the result onto a matching output. Since this mode is libpng-specific you also need to write your own composition software. </p>
<p> If you don&#8217;t need, or can&#8217;t handle, the alpha channel you can call png_set_background() to remove it by compositing against a fixed color. Don&#8217;t call png_set_strip_alpha() to do this &#8211; it will leave spurious pixel values in transparent parts of this image. </p>
<p>png_set_background(png_ptr,&nbsp;<wbr>&amp;background_color,<br />
&nbsp;<wbr>PNG_BACKGROUND_GAMMA_SCREEN, 0, 1); </p>
<p> The background_color is an RGB or grayscale value according to the data format libpng will produce for you. Because you don&#8217;t yet know the format of the PNG file, if you call png_set_background at this point you must arrange for the format produced by libpng to always have 8-bit or 16-bit components and then store the color as an 8-bit or 16-bit color as appropriate. The color contains separate gray and RGB component values, so you can let libpng produce gray or RGB output according to the input format, but low bit depth grayscale images must always be converted to at least 8-bit format. (Even though low bit depth grayscale images can&#8217;t have an alpha channel they can have a transparent color!) </p>
<p> You set the transforms you need later, either as flags to the high level interface or libpng API calls for the low level interface. For reference the settings and API calls required are: </p>
<p> 8-bit values:<br />
PNG_TRANSFORM_SCALE_16 | PNG_EXPAND<br />
png_set_expand(png_ptr);&nbsp;<wbr>png_set_scale_16(png_ptr); </p>
<p>If you must get exactly the same inaccurate results<br />
produced by default in versions prior to libpng-1.5.4,<br />
use PNG_TRANSFORM_STRIP_16 and png_set_strip_16(png_ptr)<br />
instead. </p>
<p> 16-bit values:<br />
PNG_TRANSFORM_EXPAND_16<br />
png_set_expand_16(png_ptr); </p>
<p> In either case palette image data will be expanded to RGB. If you just want color data you can add PNG_TRANSFORM_GRAY_TO_RGB or png_set_gray_to_rgb(png_ptr) to the list. </p>
<p> Calling png_set_background before the PNG file header is read will not work prior to libpng-1.5.4. Because the failure may result in unexpected warnings or errors it is therefore much safer to call png_set_background after the head has been read. Unfortunately this means that prior to libpng-1.5.4 it cannot be used with the high level interface. </p>
<h3>The high-level read interface</h3>
<p> At this point there are two ways to proceed; through the high-level read interface, or through a sequence of low-level read operations. You can use the high-level interface if (a) you are willing to read the entire image into memory, and (b) the input transformations you want to do are limited to the following set: </p>
<p>&nbsp;<wbr>PNG_TRANSFORM_IDENTITY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>No transformation<br />
&nbsp;<wbr>PNG_TRANSFORM_SCALE_16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Strip 16-bit samples to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>8-bit accurately<br />
&nbsp;<wbr>PNG_TRANSFORM_STRIP_16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Chop 16-bit samples to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>8-bit less accurately<br />
&nbsp;<wbr>PNG_TRANSFORM_STRIP_ALPHA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Discard the alpha channel<br />
&nbsp;<wbr>PNG_TRANSFORM_PACKING&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Expand 1, 2 and 4-bit<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>samples to bytes<br />
&nbsp;<wbr>PNG_TRANSFORM_PACKSWAP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Change order of packed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pixels to LSB first<br />
&nbsp;<wbr>PNG_TRANSFORM_EXPAND&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Perform set_expand()<br />
&nbsp;<wbr>PNG_TRANSFORM_INVERT_MONO&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Invert monochrome images<br />
&nbsp;<wbr>PNG_TRANSFORM_SHIFT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Normalize pixels to the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>sBIT depth<br />
&nbsp;<wbr>PNG_TRANSFORM_BGR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Flip RGB to BGR, RGBA<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>to BGRA<br />
&nbsp;<wbr>PNG_TRANSFORM_SWAP_ALPHA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Flip RGBA to ARGB or GA<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>to AG<br />
&nbsp;<wbr>PNG_TRANSFORM_INVERT_ALPHA&nbsp;<wbr>&nbsp;<wbr>Change alpha from opacity<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>to transparency<br />
&nbsp;<wbr>PNG_TRANSFORM_SWAP_ENDIAN&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Byte-swap 16-bit samples<br />
&nbsp;<wbr>PNG_TRANSFORM_GRAY_TO_RGB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Expand grayscale samples<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>to RGB&nbsp;<wbr>(or GA to RGBA)<br />
&nbsp;<wbr>PNG_TRANSFORM_EXPAND_16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Expand samples to 16 bits </p>
<p> (This excludes setting a background color, doing gamma transformation, quantizing, and setting filler.) If this is the case, simply do this: </p>
<p>&nbsp;<wbr>png_read_png(png_ptr, info_ptr, png_transforms, NULL) </p>
<p> where png_transforms is an integer containing the bitwise OR of some set of transformation flags. This call is equivalent to png_read_info(), followed the set of transformations indicated by the transform mask, then png_read_image(), and finally png_read_end(). </p>
<p> (The final parameter of this call is not yet used. Someday it might point to transformation parameters required by some future input transform.) </p>
<p> You must use png_transforms and not call any png_set_transform() functions when you use png_read_png(). </p>
<p> After you have called png_read_png(), you can retrieve the image data with </p>
<p>row_pointers&nbsp;<wbr>=&nbsp;<wbr>png_get_rows(png_ptr, info_ptr); </p>
<p> where row_pointers is an array of pointers to the pixel data for each row: </p>
<p>png_bytep row_pointers[height]; </p>
<p> If you know your image size and pixel size ahead of time, you can allocate row_pointers prior to calling png_read_png() with </p>
<p>if&nbsp;<wbr>(height&nbsp;<wbr>&gt;&nbsp;<wbr>PNG_UINT_32_MAX/png_sizeof(png_byte))<br />
png_error&nbsp;<wbr>(png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;Image is too tall to process in memory&quot;); </p>
<p>if&nbsp;<wbr>(width&nbsp;<wbr>&gt;&nbsp;<wbr>PNG_UINT_32_MAX/pixel_size)<br />
png_error&nbsp;<wbr>(png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;Image is too wide to process in memory&quot;); </p>
<p>row_pointers&nbsp;<wbr>=&nbsp;<wbr>png_malloc(png_ptr,<br />
&nbsp;<wbr>height*png_sizeof(png_bytep)); </p>
<p>for&nbsp;<wbr>(int i=0;&nbsp;<wbr>i&lt;height, i++)<br />
row_pointers[i]=NULL;&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>security precaution&nbsp;<wbr>*/ </p>
<p>for&nbsp;<wbr>(int i=0;&nbsp;<wbr>i&lt;height, i++)<br />
row_pointers[i]=png_malloc(png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>width*pixel_size); </p>
<p>png_set_rows(png_ptr, info_ptr,&nbsp;<wbr>&amp;row_pointers); </p>
<p> Alternatively you could allocate your image in one big block and define row_pointers[i] to point into the proper places in your block. </p>
<p> If you use png_set_rows(), the application is responsible for freeing row_pointers (and row_pointers[i], if they were separately allocated). </p>
<p> If you don&#8217;t allocate row_pointers ahead of time, png_read_png() will do it, and it&#8217;ll be free&#8217;ed by libpng when you call png_destroy_*(). </p>
<h3>The low-level read interface</h3>
<p> If you are going the low-level route, you are now ready to read all the file information up to the actual image data. You do this with a call to png_read_info(). </p>
<p>&nbsp;<wbr>png_read_info(png_ptr, info_ptr); </p>
<p> This will process all chunks up to but not including the image data. </p>
<p> This also copies some of the data from the PNG file into the decode structure for use in later transformations. Important information copied in is: </p>
<p> 1) The PNG file gamma from the gAMA chunk. This overwrites the default value provided by an earlier call to png_set_gamma or png_set_alpha_mode. </p>
<p> 2) Prior to libpng-1.5.4 the background color from a bKGd chunk. This damages the information provided by an earlier call to png_set_background resulting in unexpected behavior. Libpng-1.5.4 no longer does this. </p>
<p> 3) The number of significant bits in each component value. Libpng uses this to optimize gamma handling by reducing the internal lookup table sizes. </p>
<p> 4) The transparent color information from a tRNS chunk. This can be modified by a later call to png_set_tRNS. </p>
<h3>Querying the info structure</h3>
<p> Functions are used to get the information from the info_ptr once it has been read. Note that these fields may not be completely filled in until png_read_end() has read the chunk data following the image. </p>
<p>&nbsp;<wbr>png_get_IHDR(png_ptr, info_ptr,&nbsp;<wbr>&amp;width,&nbsp;<wbr>&amp;height,<br />
&nbsp;<wbr>&amp;bit_depth,&nbsp;<wbr>&amp;color_type,&nbsp;<wbr>&amp;interlace_type,<br />
&nbsp;<wbr>&amp;compression_type,&nbsp;<wbr>&amp;filter_method); </p>
<p>&nbsp;<wbr>width&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; holds the width of the image<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>in pixels&nbsp;<wbr>(up to 2^31). </p>
<p>&nbsp;<wbr>height&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; holds the height of the image<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>in pixels&nbsp;<wbr>(up to 2^31). </p>
<p>&nbsp;<wbr>bit_depth&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; holds the bit depth of one of the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>image channels.&nbsp;<wbr>&nbsp;<wbr>(valid values are<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1, 2, 4, 8, 16 and depend also on<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the color_type.&nbsp;<wbr>&nbsp;<wbr>See also<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>significant bits&nbsp;<wbr>(sBIT)&nbsp;<wbr>below). </p>
<p>&nbsp;<wbr>color_type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; describes which color/alpha channels<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>are present.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_COLOR_TYPE_GRAY<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(bit depths 1, 2, 4, 8, 16)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_COLOR_TYPE_GRAY_ALPHA<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(bit depths 8, 16)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_COLOR_TYPE_PALETTE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(bit depths 1, 2, 4, 8)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_COLOR_TYPE_RGB<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(bit_depths 8, 16)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_COLOR_TYPE_RGB_ALPHA<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(bit_depths 8, 16) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_COLOR_MASK_PALETTE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_COLOR_MASK_COLOR<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_COLOR_MASK_ALPHA </p>
<p>&nbsp;<wbr>interlace_type &#8211;&nbsp;<wbr>(PNG_INTERLACE_NONE or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_INTERLACE_ADAM7) </p>
<p>&nbsp;<wbr>compression_type &#8211;&nbsp;<wbr>(must be PNG_COMPRESSION_TYPE_BASE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>for PNG 1.0) </p>
<p>&nbsp;<wbr>filter_method&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>(must be PNG_FILTER_TYPE_BASE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>for PNG 1.0, and can also be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_INTRAPIXEL_DIFFERENCING if<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the PNG datastream is embedded in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>a MNG-1.0 datastream) </p>
<p>&nbsp;<wbr>Any or all of interlace_type, compression_type, or<br />
&nbsp;<wbr>filter_method can be NULL if you are<br />
&nbsp;<wbr>not interested in their values. </p>
<p>&nbsp;<wbr>Note that png_get_IHDR()&nbsp;<wbr>returns 32-bit data into<br />
&nbsp;<wbr>the application&#8217;s width and height variables.<br />
&nbsp;<wbr>This is an unsafe situation if these are 16-bit<br />
&nbsp;<wbr>variables.&nbsp;<wbr>&nbsp;<wbr>In such situations, the<br />
&nbsp;<wbr>png_get_image_width()&nbsp;<wbr>and png_get_image_height()<br />
&nbsp;<wbr>functions described below are safer. </p>
<p>&nbsp;<wbr>width&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>png_get_image_width(png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>info_ptr); </p>
<p>&nbsp;<wbr>height&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>png_get_image_height(png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>info_ptr); </p>
<p>&nbsp;<wbr>bit_depth&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>png_get_bit_depth(png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>info_ptr); </p>
<p>&nbsp;<wbr>color_type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>png_get_color_type(png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>info_ptr); </p>
<p>&nbsp;<wbr>interlace_type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>png_get_interlace_type(png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>info_ptr); </p>
<p>&nbsp;<wbr>compression_type&nbsp;<wbr>=&nbsp;<wbr>png_get_compression_type(png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>info_ptr); </p>
<p>&nbsp;<wbr>filter_method&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>png_get_filter_type(png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>info_ptr); </p>
<p>&nbsp;<wbr>channels&nbsp;<wbr>=&nbsp;<wbr>png_get_channels(png_ptr, info_ptr); </p>
<p>&nbsp;<wbr>channels&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; number of channels of info for the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>color type&nbsp;<wbr>(valid values are 1&nbsp;<wbr>(GRAY,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PALETTE), 2&nbsp;<wbr>(GRAY_ALPHA), 3&nbsp;<wbr>(RGB),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4&nbsp;<wbr>(RGB_ALPHA or RGB&nbsp;<wbr>+&nbsp;<wbr>filler byte)) </p>
<p>&nbsp;<wbr>rowbytes&nbsp;<wbr>=&nbsp;<wbr>png_get_rowbytes(png_ptr, info_ptr); </p>
<p>&nbsp;<wbr>rowbytes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; number of bytes needed to hold a row </p>
<p>&nbsp;<wbr>signature&nbsp;<wbr>=&nbsp;<wbr>png_get_signature(png_ptr, info_ptr); </p>
<p>&nbsp;<wbr>signature&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; holds the signature read from the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>file&nbsp;<wbr>(if any).&nbsp;<wbr>&nbsp;<wbr>The data is kept in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the same offset it would be if the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>whole signature were read&nbsp;<wbr>(i.e. if an<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>application had already read in 4<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bytes of signature before starting<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>libpng, the remaining 4 bytes would<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>be in signature[4]&nbsp;<wbr>through signature[7]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(see png_set_sig_bytes())). </p>
<p> These are also important, but their validity depends on whether the chunk has been read. The png_get_valid(png_ptr, info_ptr, PNG_INFO_&lt;chunk&gt;) and png_get_&lt;chunk&gt;(png_ptr, info_ptr, &#8230;) functions return non-zero if the data has been read, or zero if it is missing. The parameters to the png_get_&lt;chunk&gt; are set directly if they are simple data types, or a pointer into the info_ptr is returned for any complex types. </p>
<p> The colorspace data from gAMA, cHRM, sRGB, iCCP, and sBIT chunks is simply returned to give the application information about how the image was encoded. Libpng itself only does transformations using the file gamma when combining semitransparent pixels with the background color. </p>
<p>&nbsp;<wbr>png_get_PLTE(png_ptr, info_ptr,&nbsp;<wbr>&amp;palette,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&amp;num_palette); </p>
<p>&nbsp;<wbr>palette&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; the palette for the file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(array of png_color) </p>
<p>&nbsp;<wbr>num_palette&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; number of entries in the palette </p>
<p>&nbsp;<wbr>png_get_gAMA(png_ptr, info_ptr,&nbsp;<wbr>&amp;file_gamma);<br />
&nbsp;<wbr>png_get_gAMA_fixed(png_ptr, info_ptr,&nbsp;<wbr>&amp;int_file_gamma); </p>
<p>&nbsp;<wbr>file_gamma&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; the gamma at which the file was<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>written&nbsp;<wbr>(PNG_INFO_gAMA) </p>
<p>&nbsp;<wbr>int_file_gamma &#8211; 100,000 times the gamma at which the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>file is written </p>
<p>&nbsp;<wbr>png_get_cHRM(png_ptr, info_ptr,&nbsp;<wbr>&nbsp;<wbr>&amp;white_x,&nbsp;<wbr>&amp;white_y,&nbsp;<wbr>&amp;red_x,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&amp;red_y,&nbsp;<wbr>&amp;green_x,&nbsp;<wbr>&amp;green_y,&nbsp;<wbr>&amp;blue_x,&nbsp;<wbr>&amp;blue_y)<br />
&nbsp;<wbr>png_get_cHRM_XYZ(png_ptr, info_ptr,&nbsp;<wbr>&amp;red_X,&nbsp;<wbr>&amp;red_Y,&nbsp;<wbr>&amp;red_Z,&nbsp;<wbr>&amp;green_X,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&amp;green_Y,&nbsp;<wbr>&amp;green_Z,&nbsp;<wbr>&amp;blue_X,&nbsp;<wbr>&amp;blue_Y,&nbsp;<wbr>&amp;blue_Z)<br />
&nbsp;<wbr>png_get_cHRM_fixed(png_ptr, info_ptr,&nbsp;<wbr>&amp;int_white_x,&nbsp;<wbr>&amp;int_white_y,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&amp;int_red_x,&nbsp;<wbr>&amp;int_red_y,&nbsp;<wbr>&amp;int_green_x,&nbsp;<wbr>&amp;int_green_y,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&amp;int_blue_x,&nbsp;<wbr>&amp;int_blue_y)<br />
&nbsp;<wbr>png_get_cHRM_XYZ_fixed(png_ptr, info_ptr,&nbsp;<wbr>&amp;int_red_X,&nbsp;<wbr>&amp;int_red_Y,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&amp;int_red_Z,&nbsp;<wbr>&amp;int_green_X,&nbsp;<wbr>&amp;int_green_Y,&nbsp;<wbr>&amp;int_green_Z,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&amp;int_blue_X,&nbsp;<wbr>&amp;int_blue_Y,&nbsp;<wbr>&amp;int_blue_Z) </p>
<p>&nbsp;<wbr>{white,red,green,blue}_{x,y}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A color space encoding specified using the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>chromaticities of the end points and the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>white point.&nbsp;<wbr>(PNG_INFO_cHRM) </p>
<p>&nbsp;<wbr>{red,green,blue}_{X,Y,Z}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A color space encoding specified using the encoding end<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>points &#8211; the CIE tristimulus specification of the intended<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>color of the red, green and blue channels in the PNG RGB<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>data.&nbsp;<wbr>&nbsp;<wbr>The white point is simply the sum of the three end<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>points.&nbsp;<wbr>(PNG_INFO_cHRM) </p>
<p>&nbsp;<wbr>png_get_sRGB(png_ptr, info_ptr,&nbsp;<wbr>&amp;srgb_intent); </p>
<p>&nbsp;<wbr>file_srgb_intent &#8211; the rendering intent&nbsp;<wbr>(PNG_INFO_sRGB)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The presence of the sRGB chunk<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>means that the pixel data is in the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>sRGB color space.&nbsp;<wbr>&nbsp;<wbr>This chunk also<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>implies specific values of gAMA and<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cHRM. </p>
<p>&nbsp;<wbr>png_get_iCCP(png_ptr, info_ptr,&nbsp;<wbr>&amp;name,<br />
&nbsp;<wbr>&amp;compression_type,&nbsp;<wbr>&amp;profile,&nbsp;<wbr>&amp;proflen); </p>
<p>&nbsp;<wbr>name&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; The profile name. </p>
<p>&nbsp;<wbr>compression_type &#8211; The compression type;&nbsp;<wbr>always<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_COMPRESSION_TYPE_BASE for PNG 1.0.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>You may give NULL to this argument to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ignore it. </p>
<p>&nbsp;<wbr>profile&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; International Color Consortium color<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>profile data. May contain NULs. </p>
<p>&nbsp;<wbr>proflen&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; length of profile data in bytes. </p>
<p>&nbsp;<wbr>png_get_sBIT(png_ptr, info_ptr,&nbsp;<wbr>&amp;sig_bit); </p>
<p>&nbsp;<wbr>sig_bit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; the number of significant bits for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(PNG_INFO_sBIT)&nbsp;<wbr>each of the gray,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>red, green, and blue channels,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>whichever are appropriate for the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>given color type&nbsp;<wbr>(png_color_16) </p>
<p>&nbsp;<wbr>png_get_tRNS(png_ptr, info_ptr,&nbsp;<wbr>&amp;trans_alpha,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&amp;num_trans,&nbsp;<wbr>&amp;trans_color); </p>
<p>&nbsp;<wbr>trans_alpha&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; array of alpha&nbsp;<wbr>(transparency)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>entries for palette&nbsp;<wbr>(PNG_INFO_tRNS) </p>
<p>&nbsp;<wbr>num_trans&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; number of transparent entries<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(PNG_INFO_tRNS) </p>
<p>&nbsp;<wbr>trans_color&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; graylevel or color sample values of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the single transparent color for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>non-paletted images&nbsp;<wbr>(PNG_INFO_tRNS) </p>
<p>&nbsp;<wbr>png_get_hIST(png_ptr, info_ptr,&nbsp;<wbr>&amp;hist);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(PNG_INFO_hIST) </p>
<p>&nbsp;<wbr>hist&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; histogram of palette&nbsp;<wbr>(array of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>png_uint_16) </p>
<p>&nbsp;<wbr>png_get_tIME(png_ptr, info_ptr,&nbsp;<wbr>&amp;mod_time); </p>
<p>&nbsp;<wbr>mod_time&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; time image was last modified<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(PNG_VALID_tIME) </p>
<p>&nbsp;<wbr>png_get_bKGD(png_ptr, info_ptr,&nbsp;<wbr>&amp;background); </p>
<p>&nbsp;<wbr>background&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; background color&nbsp;<wbr>(of type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>png_color_16p)&nbsp;<wbr>(PNG_VALID_bKGD)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>valid 16-bit red, green and blue<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>values, regardless of color_type </p>
<p>&nbsp;<wbr>num_comments&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>png_get_text(png_ptr, info_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&amp;text_ptr,&nbsp;<wbr>&amp;num_text); </p>
<p>&nbsp;<wbr>num_comments&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; number of comments </p>
<p>&nbsp;<wbr>text_ptr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; array of png_text holding image<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>comments </p>
<p>&nbsp;<wbr>text_ptr[i].compression &#8211; type of compression used<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>on&nbsp;<wbr>&quot;text&quot;&nbsp;<wbr>PNG_TEXT_COMPRESSION_NONE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_TEXT_COMPRESSION_zTXt<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_ITXT_COMPRESSION_NONE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_ITXT_COMPRESSION_zTXt </p>
<p>&nbsp;<wbr>text_ptr[i].key&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; keyword for comment.&nbsp;<wbr>&nbsp;<wbr>Must contain<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1-79 characters. </p>
<p>&nbsp;<wbr>text_ptr[i].text&nbsp;<wbr>&nbsp;<wbr>&#8211; text comments for current<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>keyword.&nbsp;<wbr>&nbsp;<wbr>Can be empty. </p>
<p>&nbsp;<wbr>text_ptr[i].text_length &#8211; length of text string,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>after decompression, 0 for iTXt </p>
<p>&nbsp;<wbr>text_ptr[i].itxt_length &#8211; length of itxt string,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>after decompression, 0 for tEXt/zTXt </p>
<p>&nbsp;<wbr>text_ptr[i].lang&nbsp;<wbr>&nbsp;<wbr>&#8211; language of comment&nbsp;<wbr>(empty<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>string for unknown). </p>
<p>&nbsp;<wbr>text_ptr[i].lang_key&nbsp;<wbr>&nbsp;<wbr>&#8211; keyword in UTF-8<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(empty string for unknown). </p>
<p>&nbsp;<wbr>Note that the itxt_length, lang, and lang_key<br />
&nbsp;<wbr>members of the text_ptr structure only exist when the<br />
&nbsp;<wbr>library is built with iTXt chunk support.&nbsp;<wbr>&nbsp;<wbr>Prior to<br />
&nbsp;<wbr>libpng-1.4.0 the library was built by default without<br />
&nbsp;<wbr>iTXt support. Also note that when iTXt is supported,<br />
&nbsp;<wbr>they contain NULL pointers when the&nbsp;<wbr>&quot;compression&quot;<br />
&nbsp;<wbr>field contains PNG_TEXT_COMPRESSION_NONE or<br />
&nbsp;<wbr>PNG_TEXT_COMPRESSION_zTXt. </p>
<p>&nbsp;<wbr>num_text&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; number of comments&nbsp;<wbr>(same as<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>num_comments;&nbsp;<wbr>you can put NULL here<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>to avoid the duplication) </p>
<p>&nbsp;<wbr>Note while png_set_text()&nbsp;<wbr>will accept text, language,<br />
&nbsp;<wbr>and translated keywords that can be NULL pointers, the<br />
&nbsp;<wbr>structure returned by png_get_text will always contain<br />
&nbsp;<wbr>regular zero-terminated C strings.&nbsp;<wbr>&nbsp;<wbr>They might be<br />
&nbsp;<wbr>empty strings but they will never be NULL pointers. </p>
<p>&nbsp;<wbr>num_spalettes&nbsp;<wbr>=&nbsp;<wbr>png_get_sPLT(png_ptr, info_ptr,<br />
&nbsp;<wbr>&amp;palette_ptr); </p>
<p>&nbsp;<wbr>num_spalettes&nbsp;<wbr>&nbsp;<wbr>&#8211; number of sPLT chunks read. </p>
<p>&nbsp;<wbr>palette_ptr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; array of palette structures holding<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>contents of one or more sPLT chunks<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>read. </p>
<p>&nbsp;<wbr>png_get_oFFs(png_ptr, info_ptr,&nbsp;<wbr>&amp;offset_x,&nbsp;<wbr>&amp;offset_y,<br />
&nbsp;<wbr>&amp;unit_type); </p>
<p>&nbsp;<wbr>offset_x&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; positive offset from the left edge<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>of the screen&nbsp;<wbr>(can be negative) </p>
<p>&nbsp;<wbr>offset_y&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; positive offset from the top edge<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>of the screen&nbsp;<wbr>(can be negative) </p>
<p>&nbsp;<wbr>unit_type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; PNG_OFFSET_PIXEL, PNG_OFFSET_MICROMETER </p>
<p>&nbsp;<wbr>png_get_pHYs(png_ptr, info_ptr,&nbsp;<wbr>&amp;res_x,&nbsp;<wbr>&amp;res_y,<br />
&nbsp;<wbr>&amp;unit_type); </p>
<p>&nbsp;<wbr>res_x&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; pixels/unit physical resolution in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>x direction </p>
<p>&nbsp;<wbr>res_y&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; pixels/unit physical resolution in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>x direction </p>
<p>&nbsp;<wbr>unit_type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; PNG_RESOLUTION_UNKNOWN,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_RESOLUTION_METER </p>
<p>&nbsp;<wbr>png_get_sCAL(png_ptr, info_ptr,&nbsp;<wbr>&amp;unit,&nbsp;<wbr>&amp;width,<br />
&nbsp;<wbr>&amp;height) </p>
<p>&nbsp;<wbr>unit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; physical scale units&nbsp;<wbr>(an integer) </p>
<p>&nbsp;<wbr>width&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; width of a pixel in physical scale units </p>
<p>&nbsp;<wbr>height&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; height of a pixel in physical scale units<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(width and height are doubles) </p>
<p>&nbsp;<wbr>png_get_sCAL_s(png_ptr, info_ptr,&nbsp;<wbr>&amp;unit,&nbsp;<wbr>&amp;width,<br />
&nbsp;<wbr>&amp;height) </p>
<p>&nbsp;<wbr>unit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; physical scale units&nbsp;<wbr>(an integer) </p>
<p>&nbsp;<wbr>width&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; width of a pixel in physical scale units<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(expressed as a string) </p>
<p>&nbsp;<wbr>height&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; height of a pixel in physical scale units<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(width and height are strings like&nbsp;<wbr>&quot;2.54&quot;) </p>
<p>&nbsp;<wbr>num_unknown_chunks&nbsp;<wbr>=&nbsp;<wbr>png_get_unknown_chunks(png_ptr,<br />
&nbsp;<wbr>info_ptr,&nbsp;<wbr>&amp;unknowns) </p>
<p>&nbsp;<wbr>unknowns&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; array of png_unknown_chunk<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>structures holding unknown chunks </p>
<p>&nbsp;<wbr>unknowns[i].name&nbsp;<wbr>&nbsp;<wbr>&#8211; name of unknown chunk </p>
<p>&nbsp;<wbr>unknowns[i].data&nbsp;<wbr>&nbsp;<wbr>&#8211; data of unknown chunk </p>
<p>&nbsp;<wbr>unknowns[i].size&nbsp;<wbr>&nbsp;<wbr>&#8211; size of unknown chunk&#8217;s data </p>
<p>&nbsp;<wbr>unknowns[i].location &#8211; position of chunk in file </p>
<p>&nbsp;<wbr>The value of&nbsp;<wbr>&quot;i&quot;&nbsp;<wbr>corresponds to the order in which the<br />
&nbsp;<wbr>chunks were read from the PNG file or inserted with the<br />
&nbsp;<wbr>png_set_unknown_chunks()&nbsp;<wbr>function. </p>
<p>&nbsp;<wbr>The value of&nbsp;<wbr>&quot;location&quot;&nbsp;<wbr>is a bitwise&nbsp;<wbr>&quot;or&quot;&nbsp;<wbr>of </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_HAVE_IHDR&nbsp;<wbr>&nbsp;<wbr>(0x01)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_HAVE_PLTE&nbsp;<wbr>&nbsp;<wbr>(0x02)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_AFTER_IDAT&nbsp;<wbr>(0x08) </p>
<p> The data from the pHYs chunk can be retrieved in several convenient forms: </p>
<p>&nbsp;<wbr>res_x&nbsp;<wbr>=&nbsp;<wbr>png_get_x_pixels_per_meter(png_ptr,<br />
&nbsp;<wbr>info_ptr) </p>
<p>&nbsp;<wbr>res_y&nbsp;<wbr>=&nbsp;<wbr>png_get_y_pixels_per_meter(png_ptr,<br />
&nbsp;<wbr>info_ptr) </p>
<p>&nbsp;<wbr>res_x_and_y&nbsp;<wbr>=&nbsp;<wbr>png_get_pixels_per_meter(png_ptr,<br />
&nbsp;<wbr>info_ptr) </p>
<p>&nbsp;<wbr>res_x&nbsp;<wbr>=&nbsp;<wbr>png_get_x_pixels_per_inch(png_ptr,<br />
&nbsp;<wbr>info_ptr) </p>
<p>&nbsp;<wbr>res_y&nbsp;<wbr>=&nbsp;<wbr>png_get_y_pixels_per_inch(png_ptr,<br />
&nbsp;<wbr>info_ptr) </p>
<p>&nbsp;<wbr>res_x_and_y&nbsp;<wbr>=&nbsp;<wbr>png_get_pixels_per_inch(png_ptr,<br />
&nbsp;<wbr>info_ptr) </p>
<p>&nbsp;<wbr>aspect_ratio&nbsp;<wbr>=&nbsp;<wbr>png_get_pixel_aspect_ratio(png_ptr,<br />
&nbsp;<wbr>info_ptr) </p>
<p>&nbsp;<wbr>Each of these returns 0&nbsp;<wbr>[signifying&nbsp;<wbr>&quot;unknown&quot;]&nbsp;<wbr>if<br />
&nbsp;<wbr>the data is not present or if res_x is 0;<br />
&nbsp;<wbr>res_x_and_y is 0 if res_x&nbsp;<wbr>!=&nbsp;<wbr>res_y </p>
<p>&nbsp;<wbr>Note that because of the way the resolutions are<br />
&nbsp;<wbr>stored internally, the inch conversions won&#8217;t<br />
&nbsp;<wbr>come out to exactly even number.&nbsp;<wbr>&nbsp;<wbr>For example,<br />
&nbsp;<wbr>72 dpi is stored as 0.28346 pixels/meter, and<br />
&nbsp;<wbr>when this is retrieved it is 71.9988 dpi, so<br />
&nbsp;<wbr>be sure to round the returned value appropriately<br />
&nbsp;<wbr>if you want to display a reasonable-looking result. </p>
<p> The data from the oFFs chunk can be retrieved in several convenient forms: </p>
<p>&nbsp;<wbr>x_offset&nbsp;<wbr>=&nbsp;<wbr>png_get_x_offset_microns(png_ptr, info_ptr); </p>
<p>&nbsp;<wbr>y_offset&nbsp;<wbr>=&nbsp;<wbr>png_get_y_offset_microns(png_ptr, info_ptr); </p>
<p>&nbsp;<wbr>x_offset&nbsp;<wbr>=&nbsp;<wbr>png_get_x_offset_inches(png_ptr, info_ptr); </p>
<p>&nbsp;<wbr>y_offset&nbsp;<wbr>=&nbsp;<wbr>png_get_y_offset_inches(png_ptr, info_ptr); </p>
<p>&nbsp;<wbr>Each of these returns 0&nbsp;<wbr>[signifying&nbsp;<wbr>&quot;unknown&quot;&nbsp;<wbr>if both<br />
&nbsp;<wbr>x and y are 0]&nbsp;<wbr>if the data is not present or if the<br />
&nbsp;<wbr>chunk is present but the unit is the pixel.&nbsp;<wbr>&nbsp;<wbr>The<br />
&nbsp;<wbr>remark about inexact inch conversions applies here<br />
&nbsp;<wbr>as well, because a value in inches can&#8217;t always be<br />
&nbsp;<wbr>converted to microns and back without some loss<br />
&nbsp;<wbr>of precision. </p>
<p> For more information, see the PNG specification for chunk contents. Be careful with trusting rowbytes, as some of the transformations could increase the space needed to hold a row (expand, filler, gray_to_rgb, etc.). See png_read_update_info(), below. </p>
<p> A quick word about text_ptr and num_text. PNG stores comments in keyword/text pairs, one pair per chunk, with no limit on the number of text chunks, and a 2^31 byte limit on their size. While there are suggested keywords, there is no requirement to restrict the use to these strings. It is strongly suggested that keywords and text be sensible to humans (that&#8217;s the point), so don&#8217;t use abbreviations. Non-printing symbols are not allowed. See the PNG specification for more details. There is also no requirement to have text after the keyword. </p>
<p> Keywords should be limited to 79 Latin-1 characters without leading or trailing spaces, but non-consecutive spaces are allowed within the keyword. It is possible to have the same keyword any number of times. The text_ptr is an array of png_text structures, each holding a pointer to a language string, a pointer to a keyword and a pointer to a text string. The text string, language code, and translated keyword may be empty or NULL pointers. The keyword/text pairs are put into the array in the order that they are received. However, some or all of the text chunks may be after the image, so, to make sure you have read all the text chunks, don&#8217;t mess with these until after you read the stuff after the image. This will be mentioned again below in the discussion that goes with png_read_end(). </p>
<h3>Input transformations</h3>
<p> After you&#8217;ve read the header information, you can set up the library to handle any special transformations of the image data. The various ways to transform the data will be described in the order that they should occur. This is important, as some of these change the color type and/or bit depth of the data, and some others only work on certain color types and bit depths. </p>
<p> Transformations you request are ignored if they don&#8217;t have any meaning for a particular input data format. However some transformations can have an effect as a result of a previous transformation. If you specify a contradictory set of transformations, for example both adding and removing the alpha channel, you cannot predict the final result. </p>
<p> The color used for the transparency values should be supplied in the same format/depth as the current image data. It is stored in the same format/depth as the image data in a tRNS chunk, so this is what libpng expects for this data. </p>
<p> The color used for the background value depends on the need_expand argument as described below. </p>
<p> Data will be decoded into the supplied row buffers packed into bytes unless the library has been told to transform it into another format. For example, 4 bit/pixel paletted or grayscale data will be returned 2 pixels/byte with the leftmost pixel in the high-order bits of the byte, unless png_set_packing() is called. 8-bit RGB data will be stored in RGB RGB RGB format unless png_set_filler() or png_set_add_alpha() is called to insert filler bytes, either before or after each RGB triplet. 16-bit RGB data will be returned RRGGBB RRGGBB, with the most significant byte of the color value first, unless png_set_scale_16() is called to transform it to regular RGB RGB triplets, or png_set_filler() or png_set_add alpha() is called to insert filler bytes, either before or after each RRGGBB triplet. Similarly, 8-bit or 16-bit grayscale data can be modified with png_set_filler(), png_set_add_alpha(), png_set_strip_16(), or png_set_scale_16(). </p>
<p> The following code transforms grayscale images of less than 8 to 8 bits, changes paletted images to RGB, and adds a full alpha channel if there is transparency information in a tRNS chunk. This is most useful on grayscale images with bit depths of 2 or 4 or if there is a multiple-image viewing application that wishes to treat all images in the same way. </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(color_type&nbsp;<wbr>==&nbsp;<wbr>PNG_COLOR_TYPE_PALETTE)<br />
&nbsp;<wbr>&nbsp;<wbr>png_set_palette_to_rgb(png_ptr); </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(png_get_valid(png_ptr, info_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>PNG_INFO_tRNS))&nbsp;<wbr>png_set_tRNS_to_alpha(png_ptr); </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(color_type&nbsp;<wbr>==&nbsp;<wbr>PNG_COLOR_TYPE_GRAY&nbsp;<wbr>&amp;&amp;<br />
&nbsp;<wbr>&nbsp;<wbr>bit_depth&nbsp;<wbr>&lt;&nbsp;<wbr>8)&nbsp;<wbr>png_set_expand_gray_1_2_4_to_8(png_ptr); </p>
<p> The first two functions are actually aliases for png_set_expand(), added in libpng version 1.0.4, with the function names expanded to improve code readability. In some future version they may actually do different things. </p>
<p> As of libpng version 1.2.9, png_set_expand_gray_1_2_4_to_8() was added. It expands the sample depth without changing tRNS to alpha. </p>
<p> As of libpng version 1.5.2, png_set_expand_16() was added. It behaves as png_set_expand(); however, the resultant channels have 16 bits rather than 8. Use this when the output color or gray channels are made linear to avoid fairly severe accuracy loss. </p>
<p>if&nbsp;<wbr>(bit_depth&nbsp;<wbr>&lt;&nbsp;<wbr>16)<br />
png_set_expand_16(png_ptr); </p>
<p> PNG can have files with 16 bits per channel. If you only can handle 8 bits per channel, this will strip the pixels down to 8-bit. </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(bit_depth&nbsp;<wbr>==&nbsp;<wbr>16) #if PNG_LIBPNG_VER &gt;= 10504<br />
&nbsp;<wbr>png_set_scale_16(png_ptr); #else<br />
&nbsp;<wbr>png_set_strip_16(png_ptr); #endif </p>
<p> (The more accurate &quot;png_set_scale_16()&quot; API became available in libpng version 1.5.4). </p>
<p> If you need to process the alpha channel on the image separately from the image data (for example if you convert it to a bitmap mask) it is possible to have libpng strip the channel leaving just RGB or gray data: </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(color_type&nbsp;<wbr>&amp;&nbsp;<wbr>PNG_COLOR_MASK_ALPHA)<br />
&nbsp;<wbr>png_set_strip_alpha(png_ptr); </p>
<p> If you strip the alpha channel you need to find some other way of dealing with the information. If, instead, you want to convert the image to an opaque version with no alpha channel use png_set_background; see below. </p>
<p> As of libpng version 1.5.2, almost all useful expansions are supported, the major ommissions are conversion of grayscale to indexed images (which can be done trivially in the application) and conversion of indexed to grayscale (which can be done by a trivial manipulation of the palette.) </p>
<p> In the following table, the 01 means grayscale with depth&lt;8, 31 means indexed with depth&lt;8, other numerals represent the color type, &quot;T&quot; means the tRNS chunk is present, A means an alpha channel is present, and O means tRNS or alpha is present but all pixels in the image are opaque. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>FROM&nbsp;<wbr>&nbsp;<wbr>01&nbsp;<wbr>&nbsp;<wbr>31&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>0T&nbsp;<wbr>&nbsp;<wbr>0O&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>2T&nbsp;<wbr>&nbsp;<wbr>2O&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>3T&nbsp;<wbr>&nbsp;<wbr>3O&nbsp;<wbr>&nbsp;<wbr>4A&nbsp;<wbr>&nbsp;<wbr>4O&nbsp;<wbr>&nbsp;<wbr>6A&nbsp;<wbr>&nbsp;<wbr>6O<br />
TO<br />
01&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>[G]&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;<br />
31&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[Q]&nbsp;<wbr>&nbsp;<wbr>Q&nbsp;<wbr>&nbsp;<wbr>[Q]&nbsp;<wbr>[Q]&nbsp;<wbr>[Q]&nbsp;<wbr>&nbsp;<wbr>Q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Q&nbsp;<wbr>&nbsp;<wbr>[Q]&nbsp;<wbr>[Q]&nbsp;<wbr>&nbsp;<wbr>Q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Q<br />
&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>G&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>G&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>G&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>G&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>G&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>G&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>G&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>B&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>B&nbsp;<wbr>&nbsp;<wbr>GB&nbsp;<wbr>&nbsp;<wbr>GB<br />
0T&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>lt&nbsp;<wbr>&nbsp;<wbr>Gt&nbsp;<wbr>&nbsp;<wbr>t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Gt&nbsp;<wbr>&nbsp;<wbr>G&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>G&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Gt&nbsp;<wbr>&nbsp;<wbr>G&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>G&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Bt&nbsp;<wbr>&nbsp;<wbr>Bt GBt GBt<br />
0O&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>lt&nbsp;<wbr>&nbsp;<wbr>Gt&nbsp;<wbr>&nbsp;<wbr>t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Gt&nbsp;<wbr>&nbsp;<wbr>Gt&nbsp;<wbr>&nbsp;<wbr>G&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Gt&nbsp;<wbr>&nbsp;<wbr>Gt&nbsp;<wbr>&nbsp;<wbr>G&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Bt&nbsp;<wbr>&nbsp;<wbr>Bt GBt GBt<br />
&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>P&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>CB&nbsp;<wbr>&nbsp;<wbr>CB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>B&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>B<br />
2T&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Ct&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Ct&nbsp;<wbr>&nbsp;<wbr>C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>CBt CBt&nbsp;<wbr>&nbsp;<wbr>Bt&nbsp;<wbr>&nbsp;<wbr>Bt<br />
2O&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Ct&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Ct&nbsp;<wbr>&nbsp;<wbr>C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>CBt CBt&nbsp;<wbr>&nbsp;<wbr>Bt&nbsp;<wbr>&nbsp;<wbr>Bt<br />
&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[Q]&nbsp;<wbr>&nbsp;<wbr>p&nbsp;<wbr>&nbsp;<wbr>[Q]&nbsp;<wbr>[Q]&nbsp;<wbr>[Q]&nbsp;<wbr>&nbsp;<wbr>Q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>.&nbsp;<wbr>&nbsp;<wbr>[Q]&nbsp;<wbr>[Q]&nbsp;<wbr>&nbsp;<wbr>Q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Q<br />
3T&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[Qt]&nbsp;<wbr>p&nbsp;<wbr>&nbsp;<wbr>[Qt][Q]&nbsp;<wbr>[Q]&nbsp;<wbr>&nbsp;<wbr>Qt&nbsp;<wbr>&nbsp;<wbr>Qt&nbsp;<wbr>&nbsp;<wbr>Qt&nbsp;<wbr>&nbsp;<wbr>t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>t&nbsp;<wbr>&nbsp;<wbr>[Qt][Qt]&nbsp;<wbr>Qt&nbsp;<wbr>&nbsp;<wbr>Qt<br />
3O&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[Qt]&nbsp;<wbr>p&nbsp;<wbr>&nbsp;<wbr>[Qt][Q]&nbsp;<wbr>[Q]&nbsp;<wbr>&nbsp;<wbr>Qt&nbsp;<wbr>&nbsp;<wbr>Qt&nbsp;<wbr>&nbsp;<wbr>Qt&nbsp;<wbr>&nbsp;<wbr>t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>&nbsp;<wbr>[Qt][Qt]&nbsp;<wbr>Qt&nbsp;<wbr>&nbsp;<wbr>Qt<br />
4A&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>lA&nbsp;<wbr>&nbsp;<wbr>G&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>T&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>T&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>GA&nbsp;<wbr>&nbsp;<wbr>GT&nbsp;<wbr>&nbsp;<wbr>GT&nbsp;<wbr>&nbsp;<wbr>GA&nbsp;<wbr>&nbsp;<wbr>GT&nbsp;<wbr>&nbsp;<wbr>GT&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>BA&nbsp;<wbr>&nbsp;<wbr>G&nbsp;<wbr>&nbsp;<wbr>GBA<br />
4O&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>lA GBA&nbsp;<wbr>&nbsp;<wbr>A&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>T&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>T&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>GA&nbsp;<wbr>&nbsp;<wbr>GT&nbsp;<wbr>&nbsp;<wbr>GT&nbsp;<wbr>&nbsp;<wbr>GA&nbsp;<wbr>&nbsp;<wbr>GT&nbsp;<wbr>&nbsp;<wbr>GT&nbsp;<wbr>&nbsp;<wbr>BA&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>&nbsp;<wbr>GBA&nbsp;<wbr>&nbsp;<wbr>G<br />
6A&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>CA&nbsp;<wbr>&nbsp;<wbr>PA&nbsp;<wbr>&nbsp;<wbr>CA&nbsp;<wbr>&nbsp;<wbr>C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>T&nbsp;<wbr>&nbsp;<wbr>tT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PA&nbsp;<wbr>&nbsp;<wbr>P&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>P&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>C&nbsp;<wbr>&nbsp;<wbr>CBA&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>BA<br />
6O&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>CA PBA&nbsp;<wbr>&nbsp;<wbr>CA&nbsp;<wbr>&nbsp;<wbr>C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A&nbsp;<wbr>&nbsp;<wbr>tT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>T&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PA&nbsp;<wbr>&nbsp;<wbr>P&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>P&nbsp;<wbr>&nbsp;<wbr>CBA&nbsp;<wbr>&nbsp;<wbr>C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>BA&nbsp;<wbr>&nbsp;<wbr>+ </p>
<p> Within the matrix,<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;+&quot;&nbsp;<wbr>identifies entries where&nbsp;<wbr>&#8216;from&#8217;&nbsp;<wbr>and&nbsp;<wbr>&#8216;to&#8217;&nbsp;<wbr>are the same.<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;-&quot;&nbsp;<wbr>means the transformation is not supported.<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;.&quot;&nbsp;<wbr>means nothing is necessary&nbsp;<wbr>(a tRNS chunk can just be ignored).<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;t&quot;&nbsp;<wbr>means the transformation is obtained by png_set_tRNS.<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;A&quot;&nbsp;<wbr>means the transformation is obtained by png_set_add_alpha().<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;X&quot;&nbsp;<wbr>means the transformation is obtained by png_set_expand().<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;1&quot;&nbsp;<wbr>means the transformation is obtained by<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>png_set_expand_gray_1_2_4_to_8()&nbsp;<wbr>(and by png_set_expand()<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>if there is no transparency in the original or the final<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>format).<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;C&quot;&nbsp;<wbr>means the transformation is obtained by png_set_gray_to_rgb().<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;G&quot;&nbsp;<wbr>means the transformation is obtained by png_set_rgb_to_gray().<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;P&quot;&nbsp;<wbr>means the transformation is obtained by<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>png_set_expand_palette_to_rgb().<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;p&quot;&nbsp;<wbr>means the transformation is obtained by png_set_packing().<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;Q&quot;&nbsp;<wbr>means the transformation is obtained by png_set_quantize().<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;T&quot;&nbsp;<wbr>means the transformation is obtained by<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>png_set_tRNS_to_alpha().<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;B&quot;&nbsp;<wbr>means the transformation is obtained by<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>png_set_background(), or png_strip_alpha(). </p>
<p> When an entry has multiple transforms listed all are required to cause the right overall transformation. When two transforms are separated by a comma either will do the job. When transforms are enclosed in [] the transform should do the job but this is currently unimplemented &#8211; a different format will result if the suggested transformations are used. </p>
<p> In PNG files, the alpha channel in an image is the level of opacity. If you need the alpha channel in an image to be the level of transparency instead of opacity, you can invert the alpha channel (or the tRNS chunk data) after it&#8217;s read, so that 0 is fully opaque and 255 (in 8-bit or paletted images) or 65535 (in 16-bit images) is fully transparent, with </p>
<p>&nbsp;<wbr>png_set_invert_alpha(png_ptr); </p>
<p> PNG files pack pixels of bit depths 1, 2, and 4 into bytes as small as they can, resulting in, for example, 8 pixels per byte for 1 bit files. This code expands to 1 pixel per byte without changing the values of the pixels: </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(bit_depth&nbsp;<wbr>&lt;&nbsp;<wbr>8)<br />
&nbsp;<wbr>png_set_packing(png_ptr); </p>
<p> PNG files have possible bit depths of 1, 2, 4, 8, and 16. All pixels stored in a PNG image have been &quot;scaled&quot; or &quot;shifted&quot; up to the next higher possible bit depth (e.g. from 5 bits/sample in the range [0,31] to 8 bits/sample in the range [0, 255]). However, it is also possible to convert the PNG pixel data back to the original bit depth of the image. This call reduces the pixels back down to the original bit depth: </p>
<p>&nbsp;<wbr>png_color_8p sig_bit; </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(png_get_sBIT(png_ptr, info_ptr,&nbsp;<wbr>&amp;sig_bit))<br />
&nbsp;<wbr>png_set_shift(png_ptr, sig_bit); </p>
<p> PNG files store 3-color pixels in red, green, blue order. This code changes the storage of the pixels to blue, green, red: </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(color_type&nbsp;<wbr>==&nbsp;<wbr>PNG_COLOR_TYPE_RGB ||<br />
&nbsp;<wbr>&nbsp;<wbr>color_type&nbsp;<wbr>==&nbsp;<wbr>PNG_COLOR_TYPE_RGB_ALPHA)<br />
&nbsp;<wbr>png_set_bgr(png_ptr); </p>
<p> PNG files store RGB pixels packed into 3 or 6 bytes. This code expands them into 4 or 8 bytes for windowing systems that need them in this format: </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(color_type&nbsp;<wbr>==&nbsp;<wbr>PNG_COLOR_TYPE_RGB)<br />
&nbsp;<wbr>png_set_filler(png_ptr, filler, PNG_FILLER_BEFORE); </p>
<p> where &quot;filler&quot; is the 8 or 16-bit number to fill with, and the location is either PNG_FILLER_BEFORE or PNG_FILLER_AFTER, depending upon whether you want the filler before the RGB or after. This transformation does not affect images that already have full alpha channels. To add an opaque alpha channel, use filler=0xff or 0xffff and PNG_FILLER_AFTER which will generate RGBA pixels. </p>
<p> Note that png_set_filler() does not change the color type. If you want to do that, you can add a true alpha channel with </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(color_type&nbsp;<wbr>==&nbsp;<wbr>PNG_COLOR_TYPE_RGB ||<br />
&nbsp;<wbr>color_type&nbsp;<wbr>==&nbsp;<wbr>PNG_COLOR_TYPE_GRAY)<br />
&nbsp;<wbr>png_set_add_alpha(png_ptr, filler, PNG_FILLER_AFTER); </p>
<p> where &quot;filler&quot; contains the alpha value to assign to each pixel. This function was added in libpng-1.2.7. </p>
<p> If you are reading an image with an alpha channel, and you need the data as ARGB instead of the normal PNG format RGBA: </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(color_type&nbsp;<wbr>==&nbsp;<wbr>PNG_COLOR_TYPE_RGB_ALPHA)<br />
&nbsp;<wbr>png_set_swap_alpha(png_ptr); </p>
<p> For some uses, you may want a grayscale image to be represented as RGB. This code will do that conversion: </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(color_type&nbsp;<wbr>==&nbsp;<wbr>PNG_COLOR_TYPE_GRAY ||<br />
&nbsp;<wbr>&nbsp;<wbr>color_type&nbsp;<wbr>==&nbsp;<wbr>PNG_COLOR_TYPE_GRAY_ALPHA)<br />
&nbsp;<wbr>png_set_gray_to_rgb(png_ptr); </p>
<p> Conversely, you can convert an RGB or RGBA image to grayscale or grayscale with alpha. </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(color_type&nbsp;<wbr>==&nbsp;<wbr>PNG_COLOR_TYPE_RGB ||<br />
&nbsp;<wbr>&nbsp;<wbr>color_type&nbsp;<wbr>==&nbsp;<wbr>PNG_COLOR_TYPE_RGB_ALPHA)<br />
&nbsp;<wbr>png_set_rgb_to_gray(png_ptr, error_action,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>double red_weight, double green_weight); </p>
<p>&nbsp;<wbr>error_action&nbsp;<wbr>=&nbsp;<wbr>1: silently do the conversion </p>
<p>&nbsp;<wbr>error_action&nbsp;<wbr>=&nbsp;<wbr>2: issue a warning if the original<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>image has any pixel where<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>red&nbsp;<wbr>!=&nbsp;<wbr>green or red&nbsp;<wbr>!=&nbsp;<wbr>blue </p>
<p>&nbsp;<wbr>error_action&nbsp;<wbr>=&nbsp;<wbr>3: issue an error and abort the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>conversion if the original<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>image has any pixel where<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>red&nbsp;<wbr>!=&nbsp;<wbr>green or red&nbsp;<wbr>!=&nbsp;<wbr>blue </p>
<p>&nbsp;<wbr>red_weight:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>weight of red component </p>
<p>&nbsp;<wbr>green_weight:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>weight of green component<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>If either weight is negative, default<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>weights are used. </p>
<p> In the corresponding fixed point API the red_weight and green_weight values are simply scaled by 100,000: </p>
<p>&nbsp;<wbr>png_set_rgb_to_gray(png_ptr, error_action,<br />
&nbsp;<wbr>png_fixed_point red_weight,<br />
&nbsp;<wbr>png_fixed_point green_weight); </p>
<p> If you have set error_action = 1 or 2, you can later check whether the image really was gray, after processing the image rows, with the png_get_rgb_to_gray_status(png_ptr) function. It will return a png_byte that is zero if the image was gray or 1 if there were any non-gray pixels. Background and sBIT data will be silently converted to grayscale, using the green channel data for sBIT, regardless of the error_action setting. </p>
<p> The default values come from the PNG file cHRM chunk if present; otherwise, the defaults correspond to the ITU-R recommendation 709, and also the sRGB color space, as recommended in the Charles Poynton&#8217;s Colour FAQ, &lt;<a rel="nofollow" href="http://www.poynton.com/">http://www.poynton.com/</a>&gt;, in section 9: </p>
<p>&lt;<a rel="nofollow" href="http://www.poynton.com/notes/colour_and_gamma/ColorFAQ.html#RTFToC9">http://www.poynton.com/notes/colour_and_gamma/ColorFAQ.html#RTFToC9</a>&gt; </p>
<p>&nbsp;<wbr>Y&nbsp;<wbr>=&nbsp;<wbr>0.2126&nbsp;<wbr>*&nbsp;<wbr>R&nbsp;<wbr>+&nbsp;<wbr>0.7152&nbsp;<wbr>*&nbsp;<wbr>G&nbsp;<wbr>+&nbsp;<wbr>0.0722&nbsp;<wbr>*&nbsp;<wbr>B </p>
<p> Previous versions of this document, 1998 through 2002, recommended a slightly different formula: </p>
<p>&nbsp;<wbr>Y&nbsp;<wbr>=&nbsp;<wbr>0.212671&nbsp;<wbr>*&nbsp;<wbr>R&nbsp;<wbr>+&nbsp;<wbr>0.715160&nbsp;<wbr>*&nbsp;<wbr>G&nbsp;<wbr>+&nbsp;<wbr>0.072169&nbsp;<wbr>*&nbsp;<wbr>B </p>
<p> Libpng uses an integer approximation: </p>
<p>&nbsp;<wbr>Y&nbsp;<wbr>=&nbsp;<wbr>(6968&nbsp;<wbr>*&nbsp;<wbr>R&nbsp;<wbr>+&nbsp;<wbr>23434&nbsp;<wbr>*&nbsp;<wbr>G&nbsp;<wbr>+&nbsp;<wbr>2366&nbsp;<wbr>*&nbsp;<wbr>B)/32768 </p>
<p> The calculation is done in a linear colorspace, if the image gamma can be determined. </p>
<p> The png_set_background() function has been described already; it tells libpng to composite images with alpha or simple transparency against the supplied background color. For compatibility with versions of libpng earlier than libpng-1.5.4 it is recommended that you call the function after reading the file header, even if you don&#8217;t want to use the color in a bKGD chunk, if one exists. </p>
<p> If the PNG file contains a bKGD chunk (PNG_INFO_bKGD valid), you may use this color, or supply another color more suitable for the current display (e.g., the background color from a web page). You need to tell libpng how the color is represented, both the format of the component values in the color (the number of bits) and the gamma encoding of the color. The function takes two arguments, background_gamma_mode and need_expand to convey this information; however, only two combinations are likely to be useful: </p>
<p>&nbsp;<wbr>png_color_16 my_background;<br />
&nbsp;<wbr>png_color_16p image_background; </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(png_get_bKGD(png_ptr, info_ptr,&nbsp;<wbr>&amp;image_background))<br />
&nbsp;<wbr>png_set_background(png_ptr, image_background,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_BACKGROUND_GAMMA_FILE, 1/*needs to be expanded*/, 1);<br />
&nbsp;<wbr>else<br />
&nbsp;<wbr>png_set_background(png_ptr,&nbsp;<wbr>&amp;my_background,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_BACKGROUND_GAMMA_SCREEN, 0/*do not expand*/, 1); </p>
<p> The second call was described above &#8211; my_background is in the format of the final, display, output produced by libpng. Because you now know the format of the PNG it is possible to avoid the need to choose either 8-bit or 16-bit output and to retain palette images (the palette colors will be modified appropriately and the tRNS chunk removed.) However, if you are doing this, take great care not to ask for transformations without checking first that they apply! </p>
<p> In the first call the background color has the original bit depth and color type of the PNG file. So, for palette images the color is supplied as a palette index and for low bit greyscale images the color is a reduced bit value in image_background-&gt;gray. </p>
<p> If you didn&#8217;t call png_set_gamma() before reading the file header, for example if you need your code to remain compatible with older versions of libpng prior to libpng-1.5.4, this is the place to call it. </p>
<p> Do not call it if you called png_set_alpha_mode(); doing so will damage the settings put in place by png_set_alpha_mode(). (If png_set_alpha_mode() is supported then you can certainly do png_set_gamma() before reading the PNG header.) </p>
<p> This API unconditionally sets the screen and file gamma values, so it will override the value in the PNG file unless it is called before the PNG file reading starts. For this reason you must always call it with the PNG file value when you call it in this position: </p>
<p>if&nbsp;<wbr>(png_get_gAMA(png_ptr, info_ptr,&nbsp;<wbr>&amp;file_gamma))<br />
png_set_gamma(png_ptr, screen_gamma, file_gamma); </p>
<p>else<br />
png_set_gamma(png_ptr, screen_gamma, 0.45455); </p>
<p> If you need to reduce an RGB file to a paletted file, or if a paletted file has more entries then will fit on your screen, png_set_quantize() will do that. Note that this is a simple match quantization that merely finds the closest color available. This should work fairly well with optimized palettes, but fairly badly with linear color cubes. If you pass a palette that is larger than maximum_colors, the file will reduce the number of colors in the palette so it will fit into maximum_colors. If there is a histogram, libpng will use it to make more intelligent choices when reducing the palette. If there is no histogram, it may not do as good a job. </p>
<p>if&nbsp;<wbr>(color_type&nbsp;<wbr>&amp;&nbsp;<wbr>PNG_COLOR_MASK_COLOR)<br />
{<br />
if&nbsp;<wbr>(png_get_valid(png_ptr, info_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_INFO_PLTE))<br />
{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>png_uint_16p histogram&nbsp;<wbr>=&nbsp;<wbr>NULL; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>png_get_hIST(png_ptr, info_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&amp;histogram);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>png_set_quantize(png_ptr, palette, num_palette,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>max_screen_colors, histogram, 1);<br />
} </p>
<p>else<br />
{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>png_color std_color_cube[MAX_SCREEN_COLORS]&nbsp;<wbr>=<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>{&nbsp;<wbr>&#8230; colors &#8230;&nbsp;<wbr>}; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>png_set_quantize(png_ptr, std_color_cube,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>MAX_SCREEN_COLORS, MAX_SCREEN_COLORS,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>NULL,0);<br />
}<br />
} </p>
<p> PNG files describe monochrome as black being zero and white being one. The following code will reverse this (make black be one and white be zero): </p>
<p>if&nbsp;<wbr>(bit_depth&nbsp;<wbr>==&nbsp;<wbr>1&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>color_type&nbsp;<wbr>==&nbsp;<wbr>PNG_COLOR_TYPE_GRAY)<br />
png_set_invert_mono(png_ptr); </p>
<p> This function can also be used to invert grayscale and gray-alpha images: </p>
<p>if&nbsp;<wbr>(color_type&nbsp;<wbr>==&nbsp;<wbr>PNG_COLOR_TYPE_GRAY ||<br />
&nbsp;<wbr>color_type&nbsp;<wbr>==&nbsp;<wbr>PNG_COLOR_TYPE_GRAY_ALPHA)<br />
png_set_invert_mono(png_ptr); </p>
<p> PNG files store 16-bit pixels in network byte order (big-endian, ie. most significant bits first). This code changes the storage to the other way (little-endian, i.e. least significant bits first, the way PCs store them): </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(bit_depth&nbsp;<wbr>==&nbsp;<wbr>16)<br />
&nbsp;<wbr>png_set_swap(png_ptr); </p>
<p> If you are using packed-pixel images (1, 2, or 4 bits/pixel), and you need to change the order the pixels are packed into bytes, you can use: </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(bit_depth&nbsp;<wbr>&lt;&nbsp;<wbr>8)<br />
&nbsp;<wbr>png_set_packswap(png_ptr); </p>
<p> Finally, you can write your own transformation function if none of the existing ones meets your needs. This is done by setting a callback with </p>
<p>&nbsp;<wbr>png_set_read_user_transform_fn(png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>read_transform_fn); </p>
<p> You must supply the function </p>
<p>&nbsp;<wbr>void read_transform_fn(png_structp png_ptr, png_row_infop<br />
&nbsp;<wbr>&nbsp;<wbr>row_info, png_bytep data) </p>
<p> See pngtest.c for a working example. Your function will be called after all of the other transformations have been processed. Take care with interlaced images if you do the interlace yourself &#8211; the width of the row is the width in &#8216;row_info&#8217;, not the overall image width. </p>
<p> If supported, libpng provides two information routines that you can use to find where you are in processing the image: </p>
<p>png_get_current_pass_number(png_structp png_ptr);<br />
png_get_current_row_number(png_structp png_ptr); </p>
<p> Don&#8217;t try using these outside a transform callback &#8211; firstly they are only supported if user transforms are supported, secondly they may well return unexpected results unless the row is actually being processed at the moment they are called. </p>
<p> With interlaced images the value returned is the row in the input sub-image image. Use PNG_ROW_FROM_PASS_ROW(row, pass) and PNG_COL_FROM_PASS_COL(col, pass) to find the output pixel (x,y) given an interlaced sub-image pixel (row,col,pass). </p>
<p> The discussion of interlace handling above contains more information on how to use these values. </p>
<p> You can also set up a pointer to a user structure for use by your callback function, and you can inform libpng that your transform function will change the number of channels or bit depth with the function </p>
<p>&nbsp;<wbr>png_set_user_transform_info(png_ptr, user_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>user_depth, user_channels); </p>
<p> The user&#8217;s application, not libpng, is responsible for allocating and freeing any memory required for the user structure. </p>
<p> You can retrieve the pointer via the function png_get_user_transform_ptr(). For example: </p>
<p>&nbsp;<wbr>voidp read_user_transform_ptr&nbsp;<wbr>=<br />
&nbsp;<wbr>&nbsp;<wbr>png_get_user_transform_ptr(png_ptr); </p>
<p> The last thing to handle is interlacing; this is covered in detail below, but you must call the function here if you want libpng to handle expansion of the interlaced image. </p>
<p>&nbsp;<wbr>number_of_passes&nbsp;<wbr>=&nbsp;<wbr>png_set_interlace_handling(png_ptr); </p>
<p> After setting the transformations, libpng can update your png_info structure to reflect any transformations you&#8217;ve requested with this call. </p>
<p>&nbsp;<wbr>png_read_update_info(png_ptr, info_ptr); </p>
<p> This is most useful to update the info structure&#8217;s rowbytes field so you can use it to allocate your image memory. This function will also update your palette with the correct screen_gamma and background if these have been given with the calls above. You may only call png_read_update_info() once with a particular info_ptr. </p>
<p> After you call png_read_update_info(), you can allocate any memory you need to hold the image. The row data is simply raw byte data for all forms of images. As the actual allocation varies among applications, no example will be given. If you are allocating one large chunk, you will need to build an array of pointers to each row, as it will be needed for some of the functions below. </p>
<p> Remember: Before you call png_read_update_info(), the png_get_*() functions return the values corresponding to the original PNG image. After you call png_read_update_info the values refer to the image that libpng will output. Consequently you must call all the png_set_ functions before you call png_read_update_info(). This is particularly important for png_set_interlace_handling() &#8211; if you are going to call png_read_update_info() you must call png_set_interlace_handling() before it unless you want to receive interlaced output. </p>
<h3>Reading image data</h3>
<p> After you&#8217;ve allocated memory, you can read the image data. The simplest way to do this is in one function call. If you are allocating enough memory to hold the whole image, you can just call png_read_image() and libpng will read in all the image data and put it in the memory area supplied. You will need to pass in an array of pointers to each row. </p>
<p> This function automatically handles interlacing, so you don&#8217;t need to call png_set_interlace_handling() (unless you call png_read_update_info()) or call this function multiple times, or any of that other stuff necessary with png_read_rows(). </p>
<p>png_read_image(png_ptr, row_pointers); </p>
<p> where row_pointers is: </p>
<p>png_bytep row_pointers[height]; </p>
<p> You can point to void or char or whatever you use for pixels. </p>
<p> If you don&#8217;t want to read in the whole image at once, you can use png_read_rows() instead. If there is no interlacing (check interlace_type == PNG_INTERLACE_NONE), this is simple: </p>
<p>&nbsp;<wbr>png_read_rows(png_ptr, row_pointers, NULL,<br />
&nbsp;<wbr>&nbsp;<wbr>number_of_rows); </p>
<p> where row_pointers is the same as in the png_read_image() call. </p>
<p> If you are doing this just one row at a time, you can do this with a single row_pointer instead of an array of row_pointers: </p>
<p>&nbsp;<wbr>png_bytep row_pointer&nbsp;<wbr>=&nbsp;<wbr>row;<br />
&nbsp;<wbr>png_read_row(png_ptr, row_pointer, NULL); </p>
<p> If the file is interlaced (interlace_type != 0 in the IHDR chunk), things get somewhat harder. The only current (PNG Specification version 1.2) interlacing type for PNG is (interlace_type == PNG_INTERLACE_ADAM7); a somewhat complicated 2D interlace scheme, known as Adam7, that breaks down an image into seven smaller images of varying size, based on an 8&#215;8 grid. This number is defined (from libpng 1.5) as PNG_INTERLACE_ADAM7_PASSES in png.h </p>
<p> libpng can fill out those images or it can give them to you &quot;as is&quot;. It is almost always better to have libpng handle the interlacing for you. If you want the images filled out, there are two ways to do that. The one mentioned in the PNG specification is to expand each pixel to cover those pixels that have not been read yet (the &quot;rectangle&quot; method). This results in a blocky image for the first pass, which gradually smooths out as more pixels are read. The other method is the &quot;sparkle&quot; method, where pixels are drawn only in their final locations, with the rest of the image remaining whatever colors they were initialized to before the start of the read. The first method usually looks better, but tends to be slower, as there are more pixels to put in the rows. </p>
<p> If, as is likely, you want libpng to expand the images, call this before calling png_start_read_image() or png_read_update_info(): </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(interlace_type&nbsp;<wbr>==&nbsp;<wbr>PNG_INTERLACE_ADAM7)<br />
&nbsp;<wbr>number_of_passes<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>png_set_interlace_handling(png_ptr); </p>
<p> This will return the number of passes needed. Currently, this is seven, but may change if another interlace type is added. This function can be called even if the file is not interlaced, where it will return one pass. You then need to read the whole image &#8216;number_of_passes&#8217; times. Each time will distribute the pixels from the current pass to the correct place in the output image, so you need to supply the same rows to png_read_rows in each pass. </p>
<p> If you are not going to display the image after each pass, but are going to wait until the entire image is read in, use the sparkle effect. This effect is faster and the end result of either method is exactly the same. If you are planning on displaying the image after each pass, the &quot;rectangle&quot; effect is generally considered the better looking one. </p>
<p> If you only want the &quot;sparkle&quot; effect, just call png_read_rows() as normal, with the third parameter NULL. Make sure you make pass over the image number_of_passes times, and you don&#8217;t change the data in the rows between calls. You can change the locations of the data, just not the data. Each pass only writes the pixels appropriate for that pass, and assumes the data from previous passes is still valid. </p>
<p>&nbsp;<wbr>png_read_rows(png_ptr, row_pointers, NULL,<br />
&nbsp;<wbr>&nbsp;<wbr>number_of_rows); </p>
<p> If you only want the first effect (the rectangles), do the same as before except pass the row buffer in the third parameter, and leave the second parameter NULL. </p>
<p>&nbsp;<wbr>png_read_rows(png_ptr, NULL, row_pointers,<br />
&nbsp;<wbr>&nbsp;<wbr>number_of_rows); </p>
<p> If you don&#8217;t want libpng to handle the interlacing details, just call png_read_rows() PNG_INTERLACE_ADAM7_PASSES times to read in all the images. Each of the images is a valid image by itself; however, you will almost certainly need to distribute the pixels from each sub-image to the correct place. This is where everything gets very tricky. </p>
<p> If you want to retrieve the separate images you must pass the correct number of rows to each successive call of png_read_rows(). The calculation gets pretty complicated for small images, where some sub-images may not even exist because either their width or height ends up zero. libpng provides two macros to help you in 1.5 and later versions: </p>
<p>png_uint_32 width&nbsp;<wbr>=&nbsp;<wbr>PNG_PASS_COLS(image_width, pass_number);<br />
png_uint_32 height&nbsp;<wbr>=&nbsp;<wbr>PNG_PASS_ROWS(image_height, pass_number); </p>
<p> Respectively these tell you the width and height of the sub-image corresponding to the numbered pass. &#8216;pass&#8217; is in in the range 0 to 6 &#8211; this can be confusing because the specification refers to the same passes as 1 to 7! Be careful, you must check both the width and height before calling png_read_rows() and not call it for that pass if either is zero. </p>
<p> You can, of course, read each sub-image row by row. If you want to produce optimal code to make a pixel-by-pixel transformation of an interlaced image this is the best approach; read each row of each pass, transform it, and write it out to a new interlaced image. </p>
<p> If you want to de-interlace the image yourself libpng provides further macros to help that tell you where to place the pixels in the output image. Because the interlacing scheme is rectangular &#8211; sub-image pixels are always arranged on a rectangular grid &#8211; all you need to know for each pass is the starting column and row in the output image of the first pixel plus the spacing between each pixel. As of libpng 1.5 there are four macros to retrieve this information: </p>
<p>png_uint_32 x&nbsp;<wbr>=&nbsp;<wbr>PNG_PASS_START_COL(pass);<br />
png_uint_32 y&nbsp;<wbr>=&nbsp;<wbr>PNG_PASS_START_ROW(pass);<br />
png_uint_32 xStep&nbsp;<wbr>=&nbsp;<wbr>1U&nbsp;<wbr>&lt;&lt;&nbsp;<wbr>PNG_PASS_COL_SHIFT(pass);<br />
png_uint_32 yStep&nbsp;<wbr>=&nbsp;<wbr>1U&nbsp;<wbr>&lt;&lt;&nbsp;<wbr>PNG_PASS_ROW_SHIFT(pass); </p>
<p> These allow you to write the obvious loop: </p>
<p>png_uint_32 input_y&nbsp;<wbr>=&nbsp;<wbr>0;<br />
png_uint_32 output_y&nbsp;<wbr>=&nbsp;<wbr>PNG_PASS_START_ROW(pass); </p>
<p>while&nbsp;<wbr>(output_y&nbsp;<wbr>&lt;&nbsp;<wbr>output_image_height)<br />
{<br />
png_uint_32 input_x&nbsp;<wbr>=&nbsp;<wbr>0;<br />
png_uint_32 output_x&nbsp;<wbr>=&nbsp;<wbr>PNG_PASS_START_COL(pass); </p>
<p>while&nbsp;<wbr>(output_x&nbsp;<wbr>&lt;&nbsp;<wbr>output_image_width)<br />
{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>image[output_y][output_x]&nbsp;<wbr>=<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>subimage[pass][input_y][input_x++]; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>output_x&nbsp;<wbr>+=&nbsp;<wbr>xStep;<br />
} </p>
<p>++input_y;<br />
output_y&nbsp;<wbr>+=&nbsp;<wbr>yStep;<br />
} </p>
<p> Notice that the steps between successive output rows and columns are returned as shifts. This is possible because the pixels in the subimages are always a power of 2 apart &#8211; 1, 2, 4 or 8 pixels &#8211; in the original image. In practice you may need to directly calculate the output coordinate given an input coordinate. libpng provides two further macros for this purpose: </p>
<p>png_uint_32 output_x&nbsp;<wbr>=&nbsp;<wbr>PNG_COL_FROM_PASS_COL(input_x, pass);<br />
png_uint_32 output_y&nbsp;<wbr>=&nbsp;<wbr>PNG_ROW_FROM_PASS_ROW(input_y, pass); </p>
<p> Finally a pair of macros are provided to tell you if a particular image row or column appears in a given pass: </p>
<p>int col_in_pass&nbsp;<wbr>=&nbsp;<wbr>PNG_COL_IN_INTERLACE_PASS(output_x, pass);<br />
int row_in_pass&nbsp;<wbr>=&nbsp;<wbr>PNG_ROW_IN_INTERLACE_PASS(output_y, pass); </p>
<p> Bear in mind that you will probably also need to check the width and height of the pass in addition to the above to be sure the pass even exists! </p>
<p> With any luck you are convinced by now that you don&#8217;t want to do your own interlace handling. In reality normally the only good reason for doing this is if you are processing PNG files on a pixel-by-pixel basis and don&#8217;t want to load the whole file into memory when it is interlaced. </p>
<p> libpng includes a test program, pngvalid, that illustrates reading and writing of interlaced images. If you can&#8217;t get interlacing to work in your code and don&#8217;t want to leave it to libpng (the recommended approach), see how pngvalid.c does it. </p>
<h3>Finishing a sequential read</h3>
<p> After you are finished reading the image through the low-level interface, you can finish reading the file. If you are interested in comments or time, which may be stored either before or after the image data, you should pass the separate png_info struct if you want to keep the comments from before and after the image separate. </p>
<p>&nbsp;<wbr>png_infop end_info&nbsp;<wbr>=&nbsp;<wbr>png_create_info_struct(png_ptr); </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(!end_info)<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>png_destroy_read_struct(&amp;png_ptr,&nbsp;<wbr>&amp;info_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(png_infopp)NULL);<br />
&nbsp;<wbr>return&nbsp;<wbr>(ERROR);<br />
&nbsp;<wbr>} </p>
<p>png_read_end(png_ptr, end_info); </p>
<p> If you are not interested, you should still call png_read_end() but you can pass NULL, avoiding the need to create an end_info structure. </p>
<p>png_read_end(png_ptr,&nbsp;<wbr>(png_infop)NULL); </p>
<p> If you don&#8217;t call png_read_end(), then your file pointer will be left pointing to the first chunk after the last IDAT, which is probably not what you want if you expect to read something beyond the end of the PNG datastream. </p>
<p> When you are done, you can free all memory allocated by libpng like this: </p>
<p>png_destroy_read_struct(&amp;png_ptr,&nbsp;<wbr>&amp;info_ptr,<br />
&nbsp;<wbr>&amp;end_info); </p>
<p> or, if you didn&#8217;t create an end_info structure, </p>
<p>png_destroy_read_struct(&amp;png_ptr,&nbsp;<wbr>&amp;info_ptr,<br />
&nbsp;<wbr>(png_infopp)NULL); </p>
<p> It is also possible to individually free the info_ptr members that point to libpng-allocated storage with the following function: </p>
<p>&nbsp;<wbr>png_free_data(png_ptr, info_ptr, mask, seq) </p>
<p>&nbsp;<wbr>mask &#8211; identifies data to be freed, a mask<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>containing the bitwise OR of one or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>more of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_FREE_PLTE, PNG_FREE_TRNS,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_FREE_HIST, PNG_FREE_ICCP,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_FREE_PCAL, PNG_FREE_ROWS,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_FREE_SCAL, PNG_FREE_SPLT,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_FREE_TEXT, PNG_FREE_UNKN,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or simply PNG_FREE_ALL </p>
<p>&nbsp;<wbr>seq&nbsp;<wbr>&nbsp;<wbr>&#8211; sequence number of item to be freed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(-1 for all items) </p>
<p> This function may be safely called when the relevant storage has already been freed, or has not yet been allocated, or was allocated by the user and not by libpng, and will in those cases do nothing. The &quot;seq&quot; parameter is ignored if only one item of the selected data type, such as PLTE, is allowed. If &quot;seq&quot; is not -1, and multiple items are allowed for the data type identified in the mask, such as text or sPLT, only the n&#8217;th item in the structure is freed, where n is &quot;seq&quot;. </p>
<p> The default behavior is only to free data that was allocated internally by libpng. This can be changed, so that libpng will not free the data, or so that it will free data that was allocated by the user with png_malloc() or png_calloc() and passed in via a png_set_*() function, with </p>
<p>&nbsp;<wbr>png_data_freer(png_ptr, info_ptr, freer, mask) </p>
<p>&nbsp;<wbr>freer&nbsp;<wbr>&nbsp;<wbr>&#8211; one of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_DESTROY_WILL_FREE_DATA<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_SET_WILL_FREE_DATA<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_USER_WILL_FREE_DATA </p>
<p>&nbsp;<wbr>mask&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; which data elements are affected<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>same choices as in png_free_data() </p>
<p> This function only affects data that has already been allocated. You can call this function after reading the PNG data but before calling any png_set_*() functions, to control whether the user or the png_set_*() function is responsible for freeing any existing data that might be present, and again after the png_set_*() functions to control whether the user or png_destroy_*() is supposed to free the data. When the user assumes responsibility for libpng-allocated data, the application must use png_free() to free it, and when the user transfers responsibility to libpng for data that the user has allocated, the user must have used png_malloc() or png_calloc() to allocate it. </p>
<p> If you allocated your row_pointers in a single block, as suggested above in the description of the high level read interface, you must not transfer responsibility for freeing it to the png_set_rows or png_read_destroy function, because they would also try to free the individual row_pointers[i]. </p>
<p> If you allocated text_ptr.text, text_ptr.lang, and text_ptr.translated_keyword separately, do not transfer responsibility for freeing text_ptr to libpng, because when libpng fills a png_text structure it combines these members with the key member, and png_free_data() will free only text_ptr.key. Similarly, if you transfer responsibility for free&#8217;ing text_ptr from libpng to your application, your application must not separately free those members. </p>
<p> The png_free_data() function will turn off the &quot;valid&quot; flag for anything it frees. If you need to turn the flag off for a chunk that was freed by your application instead of by libpng, you can use </p>
<p>&nbsp;<wbr>png_set_invalid(png_ptr, info_ptr, mask); </p>
<p>&nbsp;<wbr>mask &#8211; identifies the chunks to be made invalid,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>containing the bitwise OR of one or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>more of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_INFO_gAMA, PNG_INFO_sBIT,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_INFO_cHRM, PNG_INFO_PLTE,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_INFO_tRNS, PNG_INFO_bKGD,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_INFO_hIST, PNG_INFO_pHYs,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_INFO_oFFs, PNG_INFO_tIME,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_INFO_pCAL, PNG_INFO_sRGB,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_INFO_iCCP, PNG_INFO_sPLT,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_INFO_sCAL, PNG_INFO_IDAT </p>
<p> For a more compact example of reading a PNG image, see the file example.c. </p>
<h3>Reading PNG files progressively</h3>
<p> The progressive reader is slightly different then the non-progressive reader. Instead of calling png_read_info(), png_read_rows(), and png_read_end(), you make one call to png_process_data(), which calls callbacks when it has the info, a row, or the end of the image. You set up these callbacks with png_set_progressive_read_fn(). You don&#8217;t have to worry about the input/output functions of libpng, as you are giving the library the data directly in png_process_data(). I will assume that you have read the section on reading PNG files above, so I will only highlight the differences (although I will show all of the code). </p>
<p> png_structp png_ptr; png_infop info_ptr; </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>&nbsp;<wbr>An example code fragment of how you would<br />
&nbsp;<wbr>&nbsp;<wbr>initialize the progressive reader in your<br />
&nbsp;<wbr>&nbsp;<wbr>application.&nbsp;<wbr>*/<br />
&nbsp;<wbr>int<br />
&nbsp;<wbr>initialize_png_reader()<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>png_ptr&nbsp;<wbr>=&nbsp;<wbr>png_create_read_struct<br />
&nbsp;<wbr>&nbsp;<wbr>(PNG_LIBPNG_VER_STRING,&nbsp;<wbr>(png_voidp)user_error_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>user_error_fn, user_warning_fn); </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(!png_ptr)<br />
&nbsp;<wbr>&nbsp;<wbr>return&nbsp;<wbr>(ERROR); </p>
<p>&nbsp;<wbr>info_ptr&nbsp;<wbr>=&nbsp;<wbr>png_create_info_struct(png_ptr); </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(!info_ptr)<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>png_destroy_read_struct(&amp;png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(png_infopp)NULL,&nbsp;<wbr>(png_infopp)NULL);<br />
&nbsp;<wbr>return&nbsp;<wbr>(ERROR);<br />
&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(setjmp(png_jmpbuf(png_ptr)))<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>png_destroy_read_struct(&amp;png_ptr,&nbsp;<wbr>&amp;info_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(png_infopp)NULL);<br />
&nbsp;<wbr>return&nbsp;<wbr>(ERROR);<br />
&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>This one&#8217;s new.&nbsp;<wbr>&nbsp;<wbr>You can provide functions<br />
&nbsp;<wbr>to be called when the header info is valid,<br />
&nbsp;<wbr>when each row is completed, and when the image<br />
&nbsp;<wbr>is finished.&nbsp;<wbr>&nbsp;<wbr>If you aren&#8217;t using all functions,<br />
&nbsp;<wbr>you can specify NULL parameters.&nbsp;<wbr>&nbsp;<wbr>Even when all<br />
&nbsp;<wbr>three functions are NULL, you need to call<br />
&nbsp;<wbr>png_set_progressive_read_fn().&nbsp;<wbr>&nbsp;<wbr>You can use<br />
&nbsp;<wbr>any struct as the user_ptr&nbsp;<wbr>(cast to a void pointer<br />
&nbsp;<wbr>for the function call), and retrieve the pointer<br />
&nbsp;<wbr>from inside the callbacks using the function </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>png_get_progressive_ptr(png_ptr); </p>
<p>&nbsp;<wbr>which will return a void pointer, which you have<br />
&nbsp;<wbr>to cast appropriately.<br />
&nbsp;<wbr>&nbsp;<wbr>*/<br />
&nbsp;<wbr>png_set_progressive_read_fn(png_ptr,&nbsp;<wbr>(void&nbsp;<wbr>*)user_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>info_callback, row_callback, end_callback); </p>
<p>&nbsp;<wbr>return 0;<br />
&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>A code fragment that you call as you receive blocks<br />
of data&nbsp;<wbr>*/<br />
&nbsp;<wbr>int<br />
&nbsp;<wbr>process_data(png_bytep buffer, png_uint_32 length)<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>if&nbsp;<wbr>(setjmp(png_jmpbuf(png_ptr)))<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>png_destroy_read_struct(&amp;png_ptr,&nbsp;<wbr>&amp;info_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(png_infopp)NULL);<br />
&nbsp;<wbr>return&nbsp;<wbr>(ERROR);<br />
&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>This one&#8217;s new also.&nbsp;<wbr>&nbsp;<wbr>Simply give it a chunk<br />
&nbsp;<wbr>of data from the file stream&nbsp;<wbr>(in order, of<br />
&nbsp;<wbr>course).&nbsp;<wbr>&nbsp;<wbr>On machines with segmented memory<br />
&nbsp;<wbr>models machines, don&#8217;t give it any more than<br />
&nbsp;<wbr>64K.&nbsp;<wbr>&nbsp;<wbr>The library seems to run fine with sizes<br />
&nbsp;<wbr>of 4K. Although you can give it much less if<br />
&nbsp;<wbr>necessary&nbsp;<wbr>(I assume you can give it chunks of<br />
&nbsp;<wbr>1 byte, I haven&#8217;t tried less then 256 bytes<br />
&nbsp;<wbr>yet).&nbsp;<wbr>&nbsp;<wbr>When this function returns, you may<br />
&nbsp;<wbr>want to display any rows that were generated<br />
&nbsp;<wbr>in the row callback if you don&#8217;t already do<br />
&nbsp;<wbr>so there.<br />
&nbsp;<wbr>&nbsp;<wbr>*/<br />
&nbsp;<wbr>png_process_data(png_ptr, info_ptr, buffer, length); </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>At this point you can call png_process_data_skip if<br />
&nbsp;<wbr>you want to handle data the library will skip yourself;<br />
&nbsp;<wbr>it simply returns the number of bytes to skip&nbsp;<wbr>(and stops<br />
&nbsp;<wbr>libpng skipping that number of bytes on the next<br />
&nbsp;<wbr>png_process_data call).<br />
&nbsp;<wbr>return 0;<br />
&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>This function is called&nbsp;<wbr>(as set by<br />
&nbsp;<wbr>png_set_progressive_read_fn()&nbsp;<wbr>above)&nbsp;<wbr>when enough data<br />
&nbsp;<wbr>has been supplied so all of the header has been<br />
&nbsp;<wbr>read.<br />
&nbsp;<wbr>*/<br />
&nbsp;<wbr>void<br />
&nbsp;<wbr>info_callback(png_structp png_ptr, png_infop info)<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>/*&nbsp;<wbr>Do any setup here, including setting any of<br />
&nbsp;<wbr>the transformations mentioned in the Reading<br />
&nbsp;<wbr>PNG files section.&nbsp;<wbr>&nbsp;<wbr>For now, you&nbsp;<wbr>_must_&nbsp;<wbr>call<br />
&nbsp;<wbr>either png_start_read_image()&nbsp;<wbr>or<br />
&nbsp;<wbr>png_read_update_info()&nbsp;<wbr>after all the<br />
&nbsp;<wbr>transformations are set&nbsp;<wbr>(even if you don&#8217;t set<br />
&nbsp;<wbr>any).&nbsp;<wbr>&nbsp;<wbr>You may start getting rows before<br />
&nbsp;<wbr>png_process_data()&nbsp;<wbr>returns, so this is your<br />
&nbsp;<wbr>last chance to prepare for that. </p>
<p>&nbsp;<wbr>This is where you turn on interlace handling,<br />
&nbsp;<wbr>assuming you don&#8217;t want to do it yourself. </p>
<p>&nbsp;<wbr>If you need to you can stop the processing of<br />
&nbsp;<wbr>your original input data at this point by calling<br />
&nbsp;<wbr>png_process_data_pause.&nbsp;<wbr>&nbsp;<wbr>This returns the number<br />
&nbsp;<wbr>of unprocessed bytes from the last png_process_data<br />
&nbsp;<wbr>call &#8211; it is up to you to ensure that the next call<br />
&nbsp;<wbr>sees these bytes again.&nbsp;<wbr>&nbsp;<wbr>If you don&#8217;t want to bother<br />
&nbsp;<wbr>with this you can get libpng to cache the unread<br />
&nbsp;<wbr>bytes by setting the&nbsp;<wbr>&#8216;save&#8217;&nbsp;<wbr>parameter&nbsp;<wbr>(see png.h)&nbsp;<wbr>but<br />
&nbsp;<wbr>then libpng will have to copy the data internally.<br />
&nbsp;<wbr>&nbsp;<wbr>*/<br />
&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>This function is called when each row of image<br />
&nbsp;<wbr>data is complete&nbsp;<wbr>*/<br />
&nbsp;<wbr>void<br />
&nbsp;<wbr>row_callback(png_structp png_ptr, png_bytep new_row,<br />
&nbsp;<wbr>png_uint_32 row_num, int pass)<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>/*&nbsp;<wbr>If the image is interlaced, and you turned<br />
&nbsp;<wbr>on the interlace handler, this function will<br />
&nbsp;<wbr>be called for every row in every pass.&nbsp;<wbr>&nbsp;<wbr>Some<br />
&nbsp;<wbr>of these rows will not be changed from the<br />
&nbsp;<wbr>previous pass.&nbsp;<wbr>&nbsp;<wbr>When the row is not changed,<br />
&nbsp;<wbr>the new_row variable will be NULL.&nbsp;<wbr>&nbsp;<wbr>The rows<br />
&nbsp;<wbr>and passes are called in order, so you don&#8217;t<br />
&nbsp;<wbr>really need the row_num and pass, but I&#8217;m<br />
&nbsp;<wbr>supplying them because it may make your life<br />
&nbsp;<wbr>easier. </p>
<p>&nbsp;<wbr>If you did not turn on interlace handling then<br />
&nbsp;<wbr>the callback is called for each row of each<br />
&nbsp;<wbr>sub-image when the image is interlaced.&nbsp;<wbr>&nbsp;<wbr>In this<br />
&nbsp;<wbr>case&nbsp;<wbr>&#8216;row_num&#8217;&nbsp;<wbr>is the row in the sub-image, not<br />
&nbsp;<wbr>the row in the output image as it is in all other<br />
&nbsp;<wbr>cases. </p>
<p>&nbsp;<wbr>For the non-NULL rows of interlaced images when<br />
&nbsp;<wbr>you have switched on libpng interlace handling,<br />
&nbsp;<wbr>you must call png_progressive_combine_row()<br />
&nbsp;<wbr>passing in the row and the old row.&nbsp;<wbr>&nbsp;<wbr>You can<br />
&nbsp;<wbr>call this function for NULL rows&nbsp;<wbr>(it will just<br />
&nbsp;<wbr>return)&nbsp;<wbr>and for non-interlaced images&nbsp;<wbr>(it just<br />
&nbsp;<wbr>does the memcpy for you)&nbsp;<wbr>if it will make the<br />
&nbsp;<wbr>code easier.&nbsp;<wbr>&nbsp;<wbr>Thus, you can just do this for<br />
&nbsp;<wbr>all cases if you switch on interlace handling;<br />
&nbsp;<wbr>&nbsp;<wbr>*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>png_progressive_combine_row(png_ptr, old_row,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>new_row); </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>where old_row is what was displayed for<br />
&nbsp;<wbr>previously for the row.&nbsp;<wbr>&nbsp;<wbr>Note that the first<br />
&nbsp;<wbr>pass&nbsp;<wbr>(pass&nbsp;<wbr>==&nbsp;<wbr>0, really)&nbsp;<wbr>will completely cover<br />
&nbsp;<wbr>the old row, so the rows do not have to be<br />
&nbsp;<wbr>initialized.&nbsp;<wbr>&nbsp;<wbr>After the first pass&nbsp;<wbr>(and only<br />
&nbsp;<wbr>for interlaced images), you will have to pass<br />
&nbsp;<wbr>the current row, and the function will combine<br />
&nbsp;<wbr>the old row and the new row. </p>
<p>&nbsp;<wbr>You can also call png_process_data_pause in this<br />
&nbsp;<wbr>callback &#8211; see above.<br />
&nbsp;<wbr>*/<br />
&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>void<br />
&nbsp;<wbr>end_callback(png_structp png_ptr, png_infop info)<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>/*&nbsp;<wbr>This function is called after the whole image<br />
&nbsp;<wbr>has been read, including any chunks after the<br />
&nbsp;<wbr>image&nbsp;<wbr>(up to and including the IEND).&nbsp;<wbr>&nbsp;<wbr>You<br />
&nbsp;<wbr>will usually have the same info chunk as you<br />
&nbsp;<wbr>had in the header, although some data may have<br />
&nbsp;<wbr>been added to the comments and time fields. </p>
<p>&nbsp;<wbr>Most people won&#8217;t do much here, perhaps setting<br />
&nbsp;<wbr>a flag that marks the image as finished.<br />
&nbsp;<wbr>&nbsp;<wbr>*/<br />
&nbsp;<wbr>} </p>
<h2>IV. Writing</h2>
<p> Much of this is very similar to reading. However, everything of importance is repeated here, so you won&#8217;t have to constantly look back up in the reading section to understand writing. </p>
<h3>Setup</h3>
<p> You will want to do the I/O initialization before you get into libpng, so if it doesn&#8217;t work, you don&#8217;t have anything to undo. If you are not using the standard I/O functions, you will need to replace them with custom writing functions. See the discussion under Customizing libpng. </p>
<p>&nbsp;<wbr>FILE&nbsp;<wbr>*fp&nbsp;<wbr>=&nbsp;<wbr>fopen(file_name,&nbsp;<wbr>&quot;wb&quot;); </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(!fp)<br />
&nbsp;<wbr>return&nbsp;<wbr>(ERROR); </p>
<p> Next, png_struct and png_info need to be allocated and initialized. As these can be both relatively large, you may not want to store these on the stack, unless you have stack space to spare. Of course, you will want to check if they return NULL. If you are also reading, you won&#8217;t want to name your read structure and your write structure both &quot;png_ptr&quot;; you can call them anything you like, such as &quot;read_ptr&quot; and &quot;write_ptr&quot;. Look at pngtest.c, for example. </p>
<p>&nbsp;<wbr>png_structp png_ptr&nbsp;<wbr>=&nbsp;<wbr>png_create_write_struct<br />
&nbsp;<wbr>(PNG_LIBPNG_VER_STRING,&nbsp;<wbr>(png_voidp)user_error_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>user_error_fn, user_warning_fn); </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(!png_ptr)<br />
&nbsp;<wbr>return&nbsp;<wbr>(ERROR); </p>
<p>&nbsp;<wbr>png_infop info_ptr&nbsp;<wbr>=&nbsp;<wbr>png_create_info_struct(png_ptr);<br />
&nbsp;<wbr>if&nbsp;<wbr>(!info_ptr)<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>png_destroy_write_struct(&amp;png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(png_infopp)NULL);<br />
&nbsp;<wbr>return&nbsp;<wbr>(ERROR);<br />
&nbsp;<wbr>} </p>
<p> If you want to use your own memory allocation routines, define PNG_USER_MEM_SUPPORTED and use png_create_write_struct_2() instead of png_create_write_struct(): </p>
<p>&nbsp;<wbr>png_structp png_ptr&nbsp;<wbr>=&nbsp;<wbr>png_create_write_struct_2<br />
&nbsp;<wbr>(PNG_LIBPNG_VER_STRING,&nbsp;<wbr>(png_voidp)user_error_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>user_error_fn, user_warning_fn,&nbsp;<wbr>(png_voidp)<br />
&nbsp;<wbr>&nbsp;<wbr>user_mem_ptr, user_malloc_fn, user_free_fn); </p>
<p> After you have these structures, you will need to set up the error handling. When libpng encounters an error, it expects to longjmp() back to your routine. Therefore, you will need to call setjmp() and pass the png_jmpbuf(png_ptr). If you write the file from different routines, you will need to update the png_jmpbuf(png_ptr) every time you enter a new routine that will call a png_*() function. See your documentation of setjmp/longjmp for your compiler for more information on setjmp/longjmp. See the discussion on libpng error handling in the Customizing Libpng section below for more information on the libpng error handling. </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(setjmp(png_jmpbuf(png_ptr)))<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>png_destroy_write_struct(&amp;png_ptr,&nbsp;<wbr>&amp;info_ptr);<br />
&nbsp;<wbr>fclose(fp);<br />
&nbsp;<wbr>return&nbsp;<wbr>(ERROR);<br />
&nbsp;<wbr>}<br />
&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>return; </p>
<p> If you would rather avoid the complexity of setjmp/longjmp issues, you can compile libpng with PNG_NO_SETJMP, in which case errors will result in a call to PNG_ABORT() which defaults to abort(). </p>
<p> You can #define PNG_ABORT() to a function that does something more useful than abort(), as long as your function does not return. </p>
<p> Now you need to set up the output code. The default for libpng is to use the C function fwrite(). If you use this, you will need to pass a valid FILE * in the function png_init_io(). Be sure that the file is opened in binary mode. Again, if you wish to handle writing data in another way, see the discussion on libpng I/O handling in the Customizing Libpng section below. </p>
<p>&nbsp;<wbr>png_init_io(png_ptr, fp); </p>
<p> If you are embedding your PNG into a datastream such as MNG, and don&#8217;t want libpng to write the 8-byte signature, or if you have already written the signature in your application, use </p>
<p>&nbsp;<wbr>png_set_sig_bytes(png_ptr, 8); </p>
<p> to inform libpng that it should not write a signature. </p>
<h3>Write callbacks</h3>
<p> At this point, you can set up a callback function that will be called after each row has been written, which you can use to control a progress meter or the like. It&#8217;s demonstrated in pngtest.c. You must supply a function </p>
<p>&nbsp;<wbr>void write_row_callback(png_structp png_ptr, png_uint_32 row,<br />
&nbsp;<wbr>int pass);<br />
&nbsp;<wbr>{<br />
/*&nbsp;<wbr>put your code here&nbsp;<wbr>*/<br />
&nbsp;<wbr>} </p>
<p> (You can give it another name that you like instead of &quot;write_row_callback&quot;) </p>
<p> To inform libpng about your function, use </p>
<p>&nbsp;<wbr>png_set_write_status_fn(png_ptr, write_row_callback); </p>
<p> When this function is called the row has already been completely processed and it has also been written out. The &#8216;row&#8217; and &#8216;pass&#8217; refer to the next row to be handled. For the non-interlaced case the row that was just handled is simply one less than the passed in row number, and pass will always be 0. For the interlaced case the same applies unless the row value is 0, in which case the row just handled was the last one from one of the preceding passes. Because interlacing may skip a pass you cannot be sure that the preceding pass is just &#8216;pass-1&#8217;, if you really need to know what the last pass is record (row,pass) from the callback and use the last recorded value each time. </p>
<p> As with the user transform you can find the output row using the PNG_ROW_FROM_PASS_ROW macro. </p>
<p> You now have the option of modifying how the compression library will run. The following functions are mainly for testing, but may be useful in some cases, like if you need to write PNG files extremely fast and are willing to give up some compression, or if you want to get the maximum possible compression at the expense of slower writing. If you have no special needs in this area, let the library do what it wants by not calling this function at all, as it has been tuned to deliver a good speed/compression ratio. The second parameter to png_set_filter() is the filter method, for which the only valid values are 0 (as of the July 1999 PNG specification, version 1.2) or 64 (if you are writing a PNG datastream that is to be embedded in a MNG datastream). The third parameter is a flag that indicates which filter type(s) are to be tested for each scanline. See the PNG specification for details on the specific filter types. </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>turn on or off filtering, and/or choose<br />
&nbsp;<wbr>specific filters.&nbsp;<wbr>&nbsp;<wbr>You can use either a single<br />
&nbsp;<wbr>PNG_FILTER_VALUE_NAME or the bitwise OR of one<br />
&nbsp;<wbr>or more PNG_FILTER_NAME masks.<br />
&nbsp;<wbr>&nbsp;<wbr>*/<br />
&nbsp;<wbr>png_set_filter(png_ptr, 0,<br />
&nbsp;<wbr>PNG_FILTER_NONE&nbsp;<wbr>&nbsp;<wbr>| PNG_FILTER_VALUE_NONE |<br />
&nbsp;<wbr>PNG_FILTER_SUB&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| PNG_FILTER_VALUE_SUB&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>PNG_FILTER_UP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| PNG_FILTER_VALUE_UP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>PNG_FILTER_AVG&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| PNG_FILTER_VALUE_AVG&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>PNG_FILTER_PAETH | PNG_FILTER_VALUE_PAETH|<br />
&nbsp;<wbr>PNG_ALL_FILTERS); </p>
<p> If an application wants to start and stop using particular filters during compression, it should start out with all of the filters (to ensure that the previous row of pixels will be stored in case it&#8217;s needed later), and then add and remove them after the start of compression. </p>
<p> If you are writing a PNG datastream that is to be embedded in a MNG datastream, the second parameter can be either 0 or 64. </p>
<p> The png_set_compression_*() functions interface to the zlib compression library, and should mostly be ignored unless you really know what you are doing. The only generally useful call is png_set_compression_level() which changes how much time zlib spends on trying to compress the image data. See the Compression Library (zlib.h and algorithm.txt, distributed with zlib) for details on the compression levels. </p>
<p>&nbsp;<wbr>#include zlib.h </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>Set the zlib compression level&nbsp;<wbr>*/<br />
&nbsp;<wbr>png_set_compression_level(png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>Z_BEST_COMPRESSION); </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>Set other zlib parameters for compressing IDAT&nbsp;<wbr>*/<br />
&nbsp;<wbr>png_set_compression_mem_level(png_ptr, 8);<br />
&nbsp;<wbr>png_set_compression_strategy(png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>Z_DEFAULT_STRATEGY);<br />
&nbsp;<wbr>png_set_compression_window_bits(png_ptr, 15);<br />
&nbsp;<wbr>png_set_compression_method(png_ptr, 8);<br />
&nbsp;<wbr>png_set_compression_buffer_size(png_ptr, 8192) </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>Set zlib parameters for text compression<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>If you don&#8217;t call these, the parameters<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>fall back on those defined for IDAT chunks<br />
&nbsp;<wbr>&nbsp;<wbr>*/<br />
&nbsp;<wbr>png_set_text_compression_mem_level(png_ptr, 8);<br />
&nbsp;<wbr>png_set_text_compression_strategy(png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>Z_DEFAULT_STRATEGY);<br />
&nbsp;<wbr>png_set_text_compression_window_bits(png_ptr, 15);<br />
&nbsp;<wbr>png_set_text_compression_method(png_ptr, 8); </p>
<h3>Setting the contents of info for output</h3>
<p> You now need to fill in the png_info structure with all the data you wish to write before the actual image. Note that the only thing you are allowed to write after the image is the text chunks and the time chunk (as of PNG Specification 1.2, anyway). See png_write_end() and the latest PNG specification for more information on that. If you wish to write them before the image, fill them in now, and flag that data as being valid. If you want to wait until after the data, don&#8217;t fill them until png_write_end(). For all the fields in png_info and their data types, see png.h. For explanations of what the fields contain, see the PNG specification. </p>
<p> Some of the more important parts of the png_info are: </p>
<p>&nbsp;<wbr>png_set_IHDR(png_ptr, info_ptr, width, height,<br />
&nbsp;<wbr>bit_depth, color_type, interlace_type,<br />
&nbsp;<wbr>compression_type, filter_method) </p>
<p>&nbsp;<wbr>width&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; holds the width of the image<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>in pixels&nbsp;<wbr>(up to 2^31). </p>
<p>&nbsp;<wbr>height&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; holds the height of the image<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>in pixels&nbsp;<wbr>(up to 2^31). </p>
<p>&nbsp;<wbr>bit_depth&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; holds the bit depth of one of the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>image channels.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(valid values are 1, 2, 4, 8, 16<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>and depend also on the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>color_type.&nbsp;<wbr>&nbsp;<wbr>See also significant<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bits&nbsp;<wbr>(sBIT)&nbsp;<wbr>below). </p>
<p>&nbsp;<wbr>color_type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; describes which color/alpha<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>channels are present.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_COLOR_TYPE_GRAY<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(bit depths 1, 2, 4, 8, 16)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_COLOR_TYPE_GRAY_ALPHA<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(bit depths 8, 16)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_COLOR_TYPE_PALETTE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(bit depths 1, 2, 4, 8)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_COLOR_TYPE_RGB<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(bit_depths 8, 16)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_COLOR_TYPE_RGB_ALPHA<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(bit_depths 8, 16) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_COLOR_MASK_PALETTE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_COLOR_MASK_COLOR<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_COLOR_MASK_ALPHA </p>
<p>&nbsp;<wbr>interlace_type &#8211; PNG_INTERLACE_NONE or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_INTERLACE_ADAM7 </p>
<p>&nbsp;<wbr>compression_type &#8211;&nbsp;<wbr>(must be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_COMPRESSION_TYPE_DEFAULT) </p>
<p>&nbsp;<wbr>filter_method&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>(must be PNG_FILTER_TYPE_DEFAULT<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or, if you are writing a PNG to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>be embedded in a MNG datastream,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>can also be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_INTRAPIXEL_DIFFERENCING) </p>
<p> If you call png_set_IHDR(), the call must appear before any of the other png_set_*() functions, because they might require access to some of the IHDR settings. The remaining png_set_*() functions can be called in any order. </p>
<p> If you wish, you can reset the compression_type, interlace_type, or filter_method later by calling png_set_IHDR() again; if you do this, the width, height, bit_depth, and color_type must be the same in each call. </p>
<p>&nbsp;<wbr>png_set_PLTE(png_ptr, info_ptr, palette,<br />
&nbsp;<wbr>num_palette); </p>
<p>&nbsp;<wbr>palette&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; the palette for the file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(array of png_color)<br />
&nbsp;<wbr>num_palette&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; number of entries in the palette </p>
<p>&nbsp;<wbr>png_set_gAMA(png_ptr, info_ptr, file_gamma);<br />
&nbsp;<wbr>png_set_gAMA_fixed(png_ptr, info_ptr, int_file_gamma); </p>
<p>&nbsp;<wbr>file_gamma&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; the gamma at which the image was<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>created&nbsp;<wbr>(PNG_INFO_gAMA) </p>
<p>&nbsp;<wbr>int_file_gamma &#8211; 100,000 times the gamma at which<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the image was created </p>
<p>&nbsp;<wbr>png_set_cHRM(png_ptr, info_ptr,&nbsp;<wbr>&nbsp;<wbr>white_x, white_y, red_x, red_y,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>green_x, green_y, blue_x, blue_y)<br />
&nbsp;<wbr>png_set_cHRM_XYZ(png_ptr, info_ptr, red_X, red_Y, red_Z, green_X,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>green_Y, green_Z, blue_X, blue_Y, blue_Z)<br />
&nbsp;<wbr>png_set_cHRM_fixed(png_ptr, info_ptr, int_white_x, int_white_y,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int_red_x, int_red_y, int_green_x, int_green_y,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int_blue_x, int_blue_y)<br />
&nbsp;<wbr>png_set_cHRM_XYZ_fixed(png_ptr, info_ptr, int_red_X, int_red_Y,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int_red_Z, int_green_X, int_green_Y, int_green_Z,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int_blue_X, int_blue_Y, int_blue_Z) </p>
<p>&nbsp;<wbr>{white,red,green,blue}_{x,y}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A color space encoding specified using the chromaticities<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>of the end points and the white point. </p>
<p>&nbsp;<wbr>{red,green,blue}_{X,Y,Z}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A color space encoding specified using the encoding end<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>points &#8211; the CIE tristimulus specification of the intended<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>color of the red, green and blue channels in the PNG RGB<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>data.&nbsp;<wbr>&nbsp;<wbr>The white point is simply the sum of the three end<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>points. </p>
<p>&nbsp;<wbr>png_set_sRGB(png_ptr, info_ptr, srgb_intent); </p>
<p>&nbsp;<wbr>srgb_intent&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; the rendering intent<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(PNG_INFO_sRGB)&nbsp;<wbr>The presence of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the sRGB chunk means that the pixel<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>data is in the sRGB color space.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>This chunk also implies specific<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>values of gAMA and cHRM.&nbsp;<wbr>&nbsp;<wbr>Rendering<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>intent is the CSS-1 property that<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>has been defined by the International<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Color Consortium<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(<a rel="nofollow" href="http://www.color.org">http://www.color.org</a>).<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>It can be one of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_sRGB_INTENT_SATURATION,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_sRGB_INTENT_PERCEPTUAL,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_sRGB_INTENT_ABSOLUTE, or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_sRGB_INTENT_RELATIVE. </p>
<p>&nbsp;<wbr>png_set_sRGB_gAMA_and_cHRM(png_ptr, info_ptr,<br />
&nbsp;<wbr>srgb_intent); </p>
<p>&nbsp;<wbr>srgb_intent&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; the rendering intent<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(PNG_INFO_sRGB)&nbsp;<wbr>The presence of the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>sRGB chunk means that the pixel<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>data is in the sRGB color space.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>This function also causes gAMA and<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cHRM chunks with the specific values<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>that are consistent with sRGB to be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>written. </p>
<p>&nbsp;<wbr>png_set_iCCP(png_ptr, info_ptr, name, compression_type,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>profile, proflen); </p>
<p>&nbsp;<wbr>name&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; The profile name. </p>
<p>&nbsp;<wbr>compression_type &#8211; The compression type;&nbsp;<wbr>always<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_COMPRESSION_TYPE_BASE for PNG 1.0.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>You may give NULL to this argument to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ignore it. </p>
<p>&nbsp;<wbr>profile&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; International Color Consortium color<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>profile data. May contain NULs. </p>
<p>&nbsp;<wbr>proflen&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; length of profile data in bytes. </p>
<p>&nbsp;<wbr>png_set_sBIT(png_ptr, info_ptr, sig_bit); </p>
<p>&nbsp;<wbr>sig_bit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; the number of significant bits for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(PNG_INFO_sBIT)&nbsp;<wbr>each of the gray, red,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>green, and blue channels, whichever are<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>appropriate for the given color type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(png_color_16) </p>
<p>&nbsp;<wbr>png_set_tRNS(png_ptr, info_ptr, trans_alpha,<br />
&nbsp;<wbr>num_trans, trans_color); </p>
<p>&nbsp;<wbr>trans_alpha&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; array of alpha&nbsp;<wbr>(transparency)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>entries for palette&nbsp;<wbr>(PNG_INFO_tRNS) </p>
<p>&nbsp;<wbr>num_trans&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; number of transparent entries<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(PNG_INFO_tRNS) </p>
<p>&nbsp;<wbr>trans_color&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; graylevel or color sample values<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(in order red, green, blue)&nbsp;<wbr>of the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>single transparent color for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>non-paletted images&nbsp;<wbr>(PNG_INFO_tRNS) </p>
<p>&nbsp;<wbr>png_set_hIST(png_ptr, info_ptr, hist); </p>
<p>&nbsp;<wbr>hist&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; histogram of palette&nbsp;<wbr>(array of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>png_uint_16)&nbsp;<wbr>(PNG_INFO_hIST) </p>
<p>&nbsp;<wbr>png_set_tIME(png_ptr, info_ptr, mod_time); </p>
<p>&nbsp;<wbr>mod_time&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; time image was last modified<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(PNG_VALID_tIME) </p>
<p>&nbsp;<wbr>png_set_bKGD(png_ptr, info_ptr, background); </p>
<p>&nbsp;<wbr>background&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; background color&nbsp;<wbr>(of type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>png_color_16p)&nbsp;<wbr>(PNG_VALID_bKGD) </p>
<p>&nbsp;<wbr>png_set_text(png_ptr, info_ptr, text_ptr, num_text); </p>
<p>&nbsp;<wbr>text_ptr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; array of png_text holding image<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>comments </p>
<p>&nbsp;<wbr>text_ptr[i].compression &#8211; type of compression used<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>on&nbsp;<wbr>&quot;text&quot;&nbsp;<wbr>PNG_TEXT_COMPRESSION_NONE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_TEXT_COMPRESSION_zTXt<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_ITXT_COMPRESSION_NONE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_ITXT_COMPRESSION_zTXt<br />
&nbsp;<wbr>text_ptr[i].key&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; keyword for comment.&nbsp;<wbr>&nbsp;<wbr>Must contain<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1-79 characters.<br />
&nbsp;<wbr>text_ptr[i].text&nbsp;<wbr>&nbsp;<wbr>&#8211; text comments for current<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>keyword.&nbsp;<wbr>&nbsp;<wbr>Can be NULL or empty.<br />
&nbsp;<wbr>text_ptr[i].text_length &#8211; length of text string,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>after decompression, 0 for iTXt<br />
&nbsp;<wbr>text_ptr[i].itxt_length &#8211; length of itxt string,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>after decompression, 0 for tEXt/zTXt<br />
&nbsp;<wbr>text_ptr[i].lang&nbsp;<wbr>&nbsp;<wbr>&#8211; language of comment&nbsp;<wbr>(NULL or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>empty for unknown).<br />
&nbsp;<wbr>text_ptr[i].translated_keyword&nbsp;<wbr>&nbsp;<wbr>&#8211; keyword in UTF-8&nbsp;<wbr>(NULL<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or empty for unknown). </p>
<p>&nbsp;<wbr>Note that the itxt_length, lang, and lang_key<br />
&nbsp;<wbr>members of the text_ptr structure only exist when the<br />
&nbsp;<wbr>library is built with iTXt chunk support.&nbsp;<wbr>&nbsp;<wbr>Prior to<br />
&nbsp;<wbr>libpng-1.4.0 the library was built by default without<br />
&nbsp;<wbr>iTXt support. Also note that when iTXt is supported,<br />
&nbsp;<wbr>they contain NULL pointers when the&nbsp;<wbr>&quot;compression&quot;<br />
&nbsp;<wbr>field contains PNG_TEXT_COMPRESSION_NONE or<br />
&nbsp;<wbr>PNG_TEXT_COMPRESSION_zTXt. </p>
<p>&nbsp;<wbr>num_text&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; number of comments </p>
<p>&nbsp;<wbr>png_set_sPLT(png_ptr, info_ptr,&nbsp;<wbr>&amp;palette_ptr,<br />
&nbsp;<wbr>num_spalettes); </p>
<p>&nbsp;<wbr>palette_ptr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; array of png_sPLT_struct structures<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>to be added to the list of palettes<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>in the info structure.<br />
&nbsp;<wbr>num_spalettes&nbsp;<wbr>&nbsp;<wbr>&#8211; number of palette structures to be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>added. </p>
<p>&nbsp;<wbr>png_set_oFFs(png_ptr, info_ptr, offset_x, offset_y,<br />
&nbsp;<wbr>&nbsp;<wbr>unit_type); </p>
<p>&nbsp;<wbr>offset_x&nbsp;<wbr>&nbsp;<wbr>&#8211; positive offset from the left<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>edge of the screen </p>
<p>&nbsp;<wbr>offset_y&nbsp;<wbr>&nbsp;<wbr>&#8211; positive offset from the top<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>edge of the screen </p>
<p>&nbsp;<wbr>unit_type &#8211; PNG_OFFSET_PIXEL, PNG_OFFSET_MICROMETER </p>
<p>&nbsp;<wbr>png_set_pHYs(png_ptr, info_ptr, res_x, res_y,<br />
&nbsp;<wbr>&nbsp;<wbr>unit_type); </p>
<p>&nbsp;<wbr>res_x&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; pixels/unit physical resolution<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>in x direction </p>
<p>&nbsp;<wbr>res_y&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; pixels/unit physical resolution<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>in y direction </p>
<p>&nbsp;<wbr>unit_type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; PNG_RESOLUTION_UNKNOWN,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_RESOLUTION_METER </p>
<p>&nbsp;<wbr>png_set_sCAL(png_ptr, info_ptr, unit, width, height) </p>
<p>&nbsp;<wbr>unit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; physical scale units&nbsp;<wbr>(an integer) </p>
<p>&nbsp;<wbr>width&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; width of a pixel in physical scale units </p>
<p>&nbsp;<wbr>height&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; height of a pixel in physical scale units<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(width and height are doubles) </p>
<p>&nbsp;<wbr>png_set_sCAL_s(png_ptr, info_ptr, unit, width, height) </p>
<p>&nbsp;<wbr>unit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; physical scale units&nbsp;<wbr>(an integer) </p>
<p>&nbsp;<wbr>width&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; width of a pixel in physical scale units<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>expressed as a string </p>
<p>&nbsp;<wbr>height&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; height of a pixel in physical scale units<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(width and height are strings like&nbsp;<wbr>&quot;2.54&quot;) </p>
<p>&nbsp;<wbr>png_set_unknown_chunks(png_ptr, info_ptr,&nbsp;<wbr>&amp;unknowns,<br />
&nbsp;<wbr>num_unknowns) </p>
<p>&nbsp;<wbr>unknowns&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; array of png_unknown_chunk<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>structures holding unknown chunks<br />
&nbsp;<wbr>unknowns[i].name&nbsp;<wbr>&nbsp;<wbr>&#8211; name of unknown chunk<br />
&nbsp;<wbr>unknowns[i].data&nbsp;<wbr>&nbsp;<wbr>&#8211; data of unknown chunk<br />
&nbsp;<wbr>unknowns[i].size&nbsp;<wbr>&nbsp;<wbr>&#8211; size of unknown chunk&#8217;s data<br />
&nbsp;<wbr>unknowns[i].location &#8211; position to write chunk in file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0: do not write chunk<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_HAVE_IHDR: before PLTE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_HAVE_PLTE: before IDAT<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_AFTER_IDAT: after IDAT </p>
<p> The &quot;location&quot; member is set automatically according to what part of the output file has already been written. You can change its value after calling png_set_unknown_chunks() as demonstrated in pngtest.c. Within each of the &quot;locations&quot;, the chunks are sequenced according to their position in the structure (that is, the value of &quot;i&quot;, which is the order in which the chunk was either read from the input file or defined with png_set_unknown_chunks). </p>
<p> A quick word about text and num_text. text is an array of png_text structures. num_text is the number of valid structures in the array. Each png_text structure holds a language code, a keyword, a text value, and a compression type. </p>
<p> The compression types have the same valid numbers as the compression types of the image data. Currently, the only valid number is zero. However, you can store text either compressed or uncompressed, unlike images, which always have to be compressed. So if you don&#8217;t want the text compressed, set the compression type to PNG_TEXT_COMPRESSION_NONE. Because tEXt and zTXt chunks don&#8217;t have a language field, if you specify PNG_TEXT_COMPRESSION_NONE or PNG_TEXT_COMPRESSION_zTXt any language code or translated keyword will not be written out. </p>
<p> Until text gets around a few hundred bytes, it is not worth compressing it. After the text has been written out to the file, the compression type is set to PNG_TEXT_COMPRESSION_NONE_WR or PNG_TEXT_COMPRESSION_zTXt_WR, so that it isn&#8217;t written out again at the end (in case you are calling png_write_end() with the same struct). </p>
<p> The keywords that are given in the PNG Specification are: </p>
<p>&nbsp;<wbr>Title&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Short&nbsp;<wbr>(one line)&nbsp;<wbr>title or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>caption for image </p>
<p>&nbsp;<wbr>Author&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Name of image&#8217;s creator </p>
<p>&nbsp;<wbr>Description&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Description of image&nbsp;<wbr>(possibly long) </p>
<p>&nbsp;<wbr>Copyright&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Copyright notice </p>
<p>&nbsp;<wbr>Creation Time&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Time of original image creation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(usually RFC 1123 format, see below) </p>
<p>&nbsp;<wbr>Software&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Software used to create the image </p>
<p>&nbsp;<wbr>Disclaimer&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Legal disclaimer </p>
<p>&nbsp;<wbr>Warning&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Warning of nature of content </p>
<p>&nbsp;<wbr>Source&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Device used to create the image </p>
<p>&nbsp;<wbr>Comment&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Miscellaneous comment;&nbsp;<wbr>conversion<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>from other image format </p>
<p> The keyword-text pairs work like this. Keywords should be short simple descriptions of what the comment is about. Some typical keywords are found in the PNG specification, as is some recommendations on keywords. You can repeat keywords in a file. You can even write some text before the image and some after. For example, you may want to put a description of the image before the image, but leave the disclaimer until after, so viewers working over modem connections don&#8217;t have to wait for the disclaimer to go over the modem before they start seeing the image. Finally, keywords should be full words, not abbreviations. Keywords and text are in the ISO 8859-1 (Latin-1) character set (a superset of regular ASCII) and can not contain NUL characters, and should not contain control or other unprintable characters. To make the comments widely readable, stick with basic ASCII, and avoid machine specific character set extensions like the IBM-PC character set. The keyword must be present, but you can leave off the text string on non-compressed pairs. Compressed pairs must have a text string, as only the text string is compressed anyway, so the compression would be meaningless. </p>
<p> PNG supports modification time via the png_time structure. Two conversion routines are provided, png_convert_from_time_t() for time_t and png_convert_from_struct_tm() for struct tm. The time_t routine uses gmtime(). You don&#8217;t have to use either of these, but if you wish to fill in the png_time structure directly, you should provide the time in universal time (GMT) if possible instead of your local time. Note that the year number is the full year (e.g. 1998, rather than 98 &#8211; PNG is year 2000 compliant!), and that months start with 1. </p>
<p> If you want to store the time of the original image creation, you should use a plain tEXt chunk with the &quot;Creation Time&quot; keyword. This is necessary because the &quot;creation time&quot; of a PNG image is somewhat vague, depending on whether you mean the PNG file, the time the image was created in a non-PNG format, a still photo from which the image was scanned, or possibly the subject matter itself. In order to facilitate machine-readable dates, it is recommended that the &quot;Creation Time&quot; tEXt chunk use RFC 1123 format dates (e.g. &quot;22 May 1997 18:07:10 GMT&quot;), although this isn&#8217;t a requirement. Unlike the tIME chunk, the &quot;Creation Time&quot; tEXt chunk is not expected to be automatically changed by the software. To facilitate the use of RFC 1123 dates, a function png_convert_to_rfc1123(png_ptr, png_timep) is provided to convert from PNG time to an RFC 1123 format string. </p>
<h3>Writing unknown chunks</h3>
<p> You can use the png_set_unknown_chunks function to queue up chunks for writing. You give it a chunk name, raw data, and a size; that&#8217;s all there is to it. The chunks will be written by the next following png_write_info_before_PLTE, png_write_info, or png_write_end function. Any chunks previously read into the info structure&#8217;s unknown-chunk list will also be written out in a sequence that satisfies the PNG specification&#8217;s ordering rules. </p>
<h3>The high-level write interface</h3>
<p> At this point there are two ways to proceed; through the high-level write interface, or through a sequence of low-level write operations. You can use the high-level interface if your image data is present in the info structure. All defined output transformations are permitted, enabled by the following masks. </p>
<p>&nbsp;<wbr>PNG_TRANSFORM_IDENTITY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>No transformation<br />
&nbsp;<wbr>PNG_TRANSFORM_PACKING&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pack 1, 2 and 4-bit samples<br />
&nbsp;<wbr>PNG_TRANSFORM_PACKSWAP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Change order of packed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pixels to LSB first<br />
&nbsp;<wbr>PNG_TRANSFORM_INVERT_MONO&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Invert monochrome images<br />
&nbsp;<wbr>PNG_TRANSFORM_SHIFT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Normalize pixels to the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>sBIT depth<br />
&nbsp;<wbr>PNG_TRANSFORM_BGR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Flip RGB to BGR, RGBA<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>to BGRA<br />
&nbsp;<wbr>PNG_TRANSFORM_SWAP_ALPHA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Flip RGBA to ARGB or GA<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>to AG<br />
&nbsp;<wbr>PNG_TRANSFORM_INVERT_ALPHA&nbsp;<wbr>&nbsp;<wbr>Change alpha from opacity<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>to transparency<br />
&nbsp;<wbr>PNG_TRANSFORM_SWAP_ENDIAN&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Byte-swap 16-bit samples<br />
&nbsp;<wbr>PNG_TRANSFORM_STRIP_FILLER&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Strip out filler<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bytes&nbsp;<wbr>(deprecated).<br />
&nbsp;<wbr>PNG_TRANSFORM_STRIP_FILLER_BEFORE Strip out leading<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>filler bytes<br />
&nbsp;<wbr>PNG_TRANSFORM_STRIP_FILLER_AFTER&nbsp;<wbr>&nbsp;<wbr>Strip out trailing<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>filler bytes </p>
<p> If you have valid image data in the info structure (you can use png_set_rows() to put image data in the info structure), simply do this: </p>
<p>&nbsp;<wbr>png_write_png(png_ptr, info_ptr, png_transforms, NULL) </p>
<p> where png_transforms is an integer containing the bitwise OR of some set of transformation flags. This call is equivalent to png_write_info(), followed the set of transformations indicated by the transform mask, then png_write_image(), and finally png_write_end(). </p>
<p> (The final parameter of this call is not yet used. Someday it might point to transformation parameters required by some future output transform.) </p>
<p> You must use png_transforms and not call any png_set_transform() functions when you use png_write_png(). </p>
<h3>The low-level write interface</h3>
<p> If you are going the low-level route instead, you are now ready to write all the file information up to the actual image data. You do this with a call to png_write_info(). </p>
<p>&nbsp;<wbr>png_write_info(png_ptr, info_ptr); </p>
<p> Note that there is one transformation you may need to do before png_write_info(). In PNG files, the alpha channel in an image is the level of opacity. If your data is supplied as a level of transparency, you can invert the alpha channel before you write it, so that 0 is fully transparent and 255 (in 8-bit or paletted images) or 65535 (in 16-bit images) is fully opaque, with </p>
<p>&nbsp;<wbr>png_set_invert_alpha(png_ptr); </p>
<p> This must appear before png_write_info() instead of later with the other transformations because in the case of paletted images the tRNS chunk data has to be inverted before the tRNS chunk is written. If your image is not a paletted image, the tRNS data (which in such cases represents a single color to be rendered as transparent) won&#8217;t need to be changed, and you can safely do this transformation after your png_write_info() call. </p>
<p> If you need to write a private chunk that you want to appear before the PLTE chunk when PLTE is present, you can write the PNG info in two steps, and insert code to write your own chunk between them: </p>
<p>&nbsp;<wbr>png_write_info_before_PLTE(png_ptr, info_ptr);<br />
&nbsp;<wbr>png_set_unknown_chunks(png_ptr, info_ptr, &#8230;);<br />
&nbsp;<wbr>png_write_info(png_ptr, info_ptr); </p>
<p> After you&#8217;ve written the file information, you can set up the library to handle any special transformations of the image data. The various ways to transform the data will be described in the order that they should occur. This is important, as some of these change the color type and/or bit depth of the data, and some others only work on certain color types and bit depths. Even though each transformation checks to see if it has data that it can do something with, you should make sure to only enable a transformation if it will be valid for the data. For example, don&#8217;t swap red and blue on grayscale data. </p>
<p> PNG files store RGB pixels packed into 3 or 6 bytes. This code tells the library to strip input data that has 4 or 8 bytes per pixel down to 3 or 6 bytes (or strip 2 or 4-byte grayscale+filler data to 1 or 2 bytes per pixel). </p>
<p>&nbsp;<wbr>png_set_filler(png_ptr, 0, PNG_FILLER_BEFORE); </p>
<p> where the 0 is unused, and the location is either PNG_FILLER_BEFORE or PNG_FILLER_AFTER, depending upon whether the filler byte in the pixel is stored XRGB or RGBX. </p>
<p> PNG files pack pixels of bit depths 1, 2, and 4 into bytes as small as they can, resulting in, for example, 8 pixels per byte for 1 bit files. If the data is supplied at 1 pixel per byte, use this code, which will correctly pack the pixels into a single byte: </p>
<p>&nbsp;<wbr>png_set_packing(png_ptr); </p>
<p> PNG files reduce possible bit depths to 1, 2, 4, 8, and 16. If your data is of another bit depth, you can write an sBIT chunk into the file so that decoders can recover the original data if desired. </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>Set the true bit depth of the image data&nbsp;<wbr>*/<br />
&nbsp;<wbr>if&nbsp;<wbr>(color_type&nbsp;<wbr>&amp;&nbsp;<wbr>PNG_COLOR_MASK_COLOR)<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>sig_bit.red&nbsp;<wbr>=&nbsp;<wbr>true_bit_depth;<br />
&nbsp;<wbr>sig_bit.green&nbsp;<wbr>=&nbsp;<wbr>true_bit_depth;<br />
&nbsp;<wbr>sig_bit.blue&nbsp;<wbr>=&nbsp;<wbr>true_bit_depth;<br />
&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>else<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>sig_bit.gray&nbsp;<wbr>=&nbsp;<wbr>true_bit_depth;<br />
&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(color_type&nbsp;<wbr>&amp;&nbsp;<wbr>PNG_COLOR_MASK_ALPHA)<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>sig_bit.alpha&nbsp;<wbr>=&nbsp;<wbr>true_bit_depth;<br />
&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>png_set_sBIT(png_ptr, info_ptr,&nbsp;<wbr>&amp;sig_bit); </p>
<p> If the data is stored in the row buffer in a bit depth other than one supported by PNG (e.g. 3 bit data in the range 0-7 for a 4-bit PNG), this will scale the values to appear to be the correct bit depth as is required by PNG. </p>
<p>&nbsp;<wbr>png_set_shift(png_ptr,&nbsp;<wbr>&amp;sig_bit); </p>
<p> PNG files store 16-bit pixels in network byte order (big-endian, ie. most significant bits first). This code would be used if they are supplied the other way (little-endian, i.e. least significant bits first, the way PCs store them): </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(bit_depth&nbsp;<wbr>&gt;&nbsp;<wbr>8)<br />
&nbsp;<wbr>png_set_swap(png_ptr); </p>
<p> If you are using packed-pixel images (1, 2, or 4 bits/pixel), and you need to change the order the pixels are packed into bytes, you can use: </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(bit_depth&nbsp;<wbr>&lt;&nbsp;<wbr>8)<br />
&nbsp;<wbr>png_set_packswap(png_ptr); </p>
<p> PNG files store 3 color pixels in red, green, blue order. This code would be used if they are supplied as blue, green, red: </p>
<p>&nbsp;<wbr>png_set_bgr(png_ptr); </p>
<p> PNG files describe monochrome as black being zero and white being one. This code would be used if the pixels are supplied with this reversed (black being one and white being zero): </p>
<p>&nbsp;<wbr>png_set_invert_mono(png_ptr); </p>
<p> Finally, you can write your own transformation function if none of the existing ones meets your needs. This is done by setting a callback with </p>
<p>&nbsp;<wbr>png_set_write_user_transform_fn(png_ptr,<br />
&nbsp;<wbr>write_transform_fn); </p>
<p> You must supply the function </p>
<p>&nbsp;<wbr>void write_transform_fn(png_structp png_ptr, png_row_infop<br />
&nbsp;<wbr>row_info, png_bytep data) </p>
<p> See pngtest.c for a working example. Your function will be called before any of the other transformations are processed. If supported libpng also supplies an information routine that may be called from your callback: </p>
<p>png_get_current_row_number(png_ptr);<br />
png_get_current_pass_number(png_ptr); </p>
<p> This returns the current row passed to the transform. With interlaced images the value returned is the row in the input sub-image image. Use PNG_ROW_FROM_PASS_ROW(row, pass) and PNG_COL_FROM_PASS_COL(col, pass) to find the output pixel (x,y) given an interlaced sub-image pixel (row,col,pass). </p>
<p> The discussion of interlace handling above contains more information on how to use these values. </p>
<p> You can also set up a pointer to a user structure for use by your callback function. </p>
<p>&nbsp;<wbr>png_set_user_transform_info(png_ptr, user_ptr, 0, 0); </p>
<p> The user_channels and user_depth parameters of this function are ignored when writing; you can set them to zero as shown. </p>
<p> You can retrieve the pointer via the function png_get_user_transform_ptr(). For example: </p>
<p>&nbsp;<wbr>voidp write_user_transform_ptr&nbsp;<wbr>=<br />
&nbsp;<wbr>png_get_user_transform_ptr(png_ptr); </p>
<p> It is possible to have libpng flush any pending output, either manually, or automatically after a certain number of lines have been written. To flush the output stream a single time call: </p>
<p>&nbsp;<wbr>png_write_flush(png_ptr); </p>
<p> and to have libpng flush the output stream periodically after a certain number of scanlines have been written, call: </p>
<p>&nbsp;<wbr>png_set_flush(png_ptr, nrows); </p>
<p> Note that the distance between rows is from the last time png_write_flush() was called, or the first row of the image if it has never been called. So if you write 50 lines, and then png_set_flush 25, it will flush the output on the next scanline, and every 25 lines thereafter, unless png_write_flush() is called before 25 more lines have been written. If nrows is too small (less than about 10 lines for a 640 pixel wide RGB image) the image compression may decrease noticeably (although this may be acceptable for real-time applications). Infrequent flushing will only degrade the compression performance by a few percent over images that do not use flushing. </p>
<h3>Writing the image data</h3>
<p> That&#8217;s it for the transformations. Now you can write the image data. The simplest way to do this is in one function call. If you have the whole image in memory, you can just call png_write_image() and libpng will write the image. You will need to pass in an array of pointers to each row. This function automatically handles interlacing, so you don&#8217;t need to call png_set_interlace_handling() or call this function multiple times, or any of that other stuff necessary with png_write_rows(). </p>
<p>&nbsp;<wbr>png_write_image(png_ptr, row_pointers); </p>
<p> where row_pointers is: </p>
<p>&nbsp;<wbr>png_byte&nbsp;<wbr>*row_pointers[height]; </p>
<p> You can point to void or char or whatever you use for pixels. </p>
<p> If you don&#8217;t want to write the whole image at once, you can use png_write_rows() instead. If the file is not interlaced, this is simple: </p>
<p>&nbsp;<wbr>png_write_rows(png_ptr, row_pointers,<br />
&nbsp;<wbr>number_of_rows); </p>
<p> row_pointers is the same as in the png_write_image() call. </p>
<p> If you are just writing one row at a time, you can do this with a single row_pointer instead of an array of row_pointers: </p>
<p>&nbsp;<wbr>png_bytep row_pointer&nbsp;<wbr>=&nbsp;<wbr>row; </p>
<p>&nbsp;<wbr>png_write_row(png_ptr, row_pointer); </p>
<p> When the file is interlaced, things can get a good deal more complicated. The only currently (as of the PNG Specification version 1.2, dated July 1999) defined interlacing scheme for PNG files is the &quot;Adam7&quot; interlace scheme, that breaks down an image into seven smaller images of varying size. libpng will build these images for you, or you can do them yourself. If you want to build them yourself, see the PNG specification for details of which pixels to write when. </p>
<p> If you don&#8217;t want libpng to handle the interlacing details, just use png_set_interlace_handling() and call png_write_rows() the correct number of times to write all the sub-images (png_set_interlace_handling() returns the number of sub-images.) </p>
<p> If you want libpng to build the sub-images, call this before you start writing any rows: </p>
<p>&nbsp;<wbr>number_of_passes&nbsp;<wbr>=&nbsp;<wbr>png_set_interlace_handling(png_ptr); </p>
<p> This will return the number of passes needed. Currently, this is seven, but may change if another interlace type is added. </p>
<p> Then write the complete image number_of_passes times. </p>
<p>&nbsp;<wbr>png_write_rows(png_ptr, row_pointers, number_of_rows); </p>
<p> Think carefully before you write an interlaced image. Typically code that reads such images reads all the image data into memory, uncompressed, before doing any processing. Only code that can display an image on the fly can take advantage of the interlacing and even then the image has to be exactly the correct size for the output device, because scaling an image requires adjacent pixels and these are not available until all the passes have been read. </p>
<p> If you do write an interlaced image you will hardly ever need to handle the interlacing yourself. Call png_set_interlace_handling() and use the approach described above. </p>
<p> The only time it is conceivable that you will really need to write an interlaced image pass-by-pass is when you have read one pass by pass and made some pixel-by-pixel transformation to it, as described in the read code above. In this case use the PNG_PASS_ROWS and PNG_PASS_COLS macros to determine the size of each sub-image in turn and simply write the rows you obtained from the read code. </p>
<h3>Finishing a sequential write</h3>
<p> After you are finished writing the image, you should finish writing the file. If you are interested in writing comments or time, you should pass an appropriately filled png_info pointer. If you are not interested, you can pass NULL. </p>
<p>&nbsp;<wbr>png_write_end(png_ptr, info_ptr); </p>
<p> When you are done, you can free all memory used by libpng like this: </p>
<p>&nbsp;<wbr>png_destroy_write_struct(&amp;png_ptr,&nbsp;<wbr>&amp;info_ptr); </p>
<p> It is also possible to individually free the info_ptr members that point to libpng-allocated storage with the following function: </p>
<p>&nbsp;<wbr>png_free_data(png_ptr, info_ptr, mask, seq) </p>
<p>&nbsp;<wbr>mask&nbsp;<wbr>&nbsp;<wbr>&#8211; identifies data to be freed, a mask<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>containing the bitwise OR of one or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>more of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_FREE_PLTE, PNG_FREE_TRNS,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_FREE_HIST, PNG_FREE_ICCP,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_FREE_PCAL, PNG_FREE_ROWS,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_FREE_SCAL, PNG_FREE_SPLT,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_FREE_TEXT, PNG_FREE_UNKN,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or simply PNG_FREE_ALL </p>
<p>&nbsp;<wbr>seq&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; sequence number of item to be freed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(-1 for all items) </p>
<p> This function may be safely called when the relevant storage has already been freed, or has not yet been allocated, or was allocated by the user and not by libpng, and will in those cases do nothing. The &quot;seq&quot; parameter is ignored if only one item of the selected data type, such as PLTE, is allowed. If &quot;seq&quot; is not -1, and multiple items are allowed for the data type identified in the mask, such as text or sPLT, only the n&#8217;th item in the structure is freed, where n is &quot;seq&quot;. </p>
<p> If you allocated data such as a palette that you passed in to libpng with png_set_*, you must not free it until just before the call to png_destroy_write_struct(). </p>
<p> The default behavior is only to free data that was allocated internally by libpng. This can be changed, so that libpng will not free the data, or so that it will free data that was allocated by the user with png_malloc() or png_calloc() and passed in via a png_set_*() function, with </p>
<p>&nbsp;<wbr>png_data_freer(png_ptr, info_ptr, freer, mask) </p>
<p>&nbsp;<wbr>freer&nbsp;<wbr>&nbsp;<wbr>&#8211; one of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_DESTROY_WILL_FREE_DATA<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_SET_WILL_FREE_DATA<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_USER_WILL_FREE_DATA </p>
<p>&nbsp;<wbr>mask&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; which data elements are affected<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>same choices as in png_free_data() </p>
<p> For example, to transfer responsibility for some data from a read structure to a write structure, you could use </p>
<p>&nbsp;<wbr>png_data_freer(read_ptr, read_info_ptr,<br />
&nbsp;<wbr>PNG_USER_WILL_FREE_DATA,<br />
&nbsp;<wbr>PNG_FREE_PLTE|PNG_FREE_tRNS|PNG_FREE_hIST) </p>
<p>&nbsp;<wbr>png_data_freer(write_ptr, write_info_ptr,<br />
&nbsp;<wbr>PNG_DESTROY_WILL_FREE_DATA,<br />
&nbsp;<wbr>PNG_FREE_PLTE|PNG_FREE_tRNS|PNG_FREE_hIST) </p>
<p> thereby briefly reassigning responsibility for freeing to the user but immediately afterwards reassigning it once more to the write_destroy function. Having done this, it would then be safe to destroy the read structure and continue to use the PLTE, tRNS, and hIST data in the write structure. </p>
<p> This function only affects data that has already been allocated. You can call this function before calling after the png_set_*() functions to control whether the user or png_destroy_*() is supposed to free the data. When the user assumes responsibility for libpng-allocated data, the application must use png_free() to free it, and when the user transfers responsibility to libpng for data that the user has allocated, the user must have used png_malloc() or png_calloc() to allocate it. </p>
<p> If you allocated text_ptr.text, text_ptr.lang, and text_ptr.translated_keyword separately, do not transfer responsibility for freeing text_ptr to libpng, because when libpng fills a png_text structure it combines these members with the key member, and png_free_data() will free only text_ptr.key. Similarly, if you transfer responsibility for free&#8217;ing text_ptr from libpng to your application, your application must not separately free those members. For a more compact example of writing a PNG image, see the file example.c. </p>
<h2>V. Modifying/Customizing libpng:</h2>
<p> There are two issues here. The first is changing how libpng does standard things like memory allocation, input/output, and error handling. The second deals with more complicated things like adding new chunks, adding new transformations, and generally changing how libpng works. Both of those are compile-time issues; that is, they are generally determined at the time the code is written, and there is rarely a need to provide the user with a means of changing them. </p>
<p> Memory allocation, input/output, and error handling </p>
<p> All of the memory allocation, input/output, and error handling in libpng goes through callbacks that are user-settable. The default routines are in pngmem.c, pngrio.c, pngwio.c, and pngerror.c, respectively. To change these functions, call the appropriate png_set_*_fn() function. </p>
<p> Memory allocation is done through the functions png_malloc(), png_calloc(), and png_free(). The png_malloc() and png_free() functions currently just call the standard C functions and png_calloc() calls png_malloc() and then clears the newly allocated memory to zero; note that png_calloc(png_ptr, size) is not the same as the calloc(number, size) function provided by stdlib.h. There is limited support for certain systems with segmented memory architectures and the types of pointers declared by png.h match this; you will have to use appropriate pointers in your application. Since it is unlikely that the method of handling memory allocation on a platform will change between applications, these functions must be modified in the library at compile time. If you prefer to use a different method of allocating and freeing data, you can use png_create_read_struct_2() or png_create_write_struct_2() to register your own functions as described above. These functions also provide a void pointer that can be retrieved via </p>
<p>&nbsp;<wbr>mem_ptr=png_get_mem_ptr(png_ptr); </p>
<p> Your replacement memory functions must have prototypes as follows: </p>
<p>&nbsp;<wbr>png_voidp malloc_fn(png_structp png_ptr,<br />
&nbsp;<wbr>png_alloc_size_t size); </p>
<p>&nbsp;<wbr>void free_fn(png_structp png_ptr, png_voidp ptr); </p>
<p> Your malloc_fn() must return NULL in case of failure. The png_malloc() function will normally call png_error() if it receives a NULL from the system memory allocator or from your replacement malloc_fn(). </p>
<p> Your free_fn() will never be called with a NULL ptr, since libpng&#8217;s png_free() checks for NULL before calling free_fn(). </p>
<p> Input/Output in libpng is done through png_read() and png_write(), which currently just call fread() and fwrite(). The FILE * is stored in png_struct and is initialized via png_init_io(). If you wish to change the method of I/O, the library supplies callbacks that you can set through the function png_set_read_fn() and png_set_write_fn() at run time, instead of calling the png_init_io() function. These functions also provide a void pointer that can be retrieved via the function png_get_io_ptr(). For example: </p>
<p>&nbsp;<wbr>png_set_read_fn(png_structp read_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>voidp read_io_ptr, png_rw_ptr read_data_fn) </p>
<p>&nbsp;<wbr>png_set_write_fn(png_structp write_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>voidp write_io_ptr, png_rw_ptr write_data_fn,<br />
&nbsp;<wbr>&nbsp;<wbr>png_flush_ptr output_flush_fn); </p>
<p>&nbsp;<wbr>voidp read_io_ptr&nbsp;<wbr>=&nbsp;<wbr>png_get_io_ptr(read_ptr);<br />
&nbsp;<wbr>voidp write_io_ptr&nbsp;<wbr>=&nbsp;<wbr>png_get_io_ptr(write_ptr); </p>
<p> The replacement I/O functions must have prototypes as follows: </p>
<p>&nbsp;<wbr>void user_read_data(png_structp png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>png_bytep data, png_size_t length); </p>
<p>&nbsp;<wbr>void user_write_data(png_structp png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>png_bytep data, png_size_t length); </p>
<p>&nbsp;<wbr>void user_flush_data(png_structp png_ptr); </p>
<p> The user_read_data() function is responsible for detecting and handling end-of-data errors. </p>
<p> Supplying NULL for the read, write, or flush functions sets them back to using the default C stream functions, which expect the io_ptr to point to a standard *FILE structure. It is probably a mistake to use NULL for one of write_data_fn and output_flush_fn but not both of them, unless you have built libpng with PNG_NO_WRITE_FLUSH defined. It is an error to read from a write stream, and vice versa. </p>
<p> Error handling in libpng is done through png_error() and png_warning(). Errors handled through png_error() are fatal, meaning that png_error() should never return to its caller. Currently, this is handled via setjmp() and longjmp() (unless you have compiled libpng with PNG_NO_SETJMP, in which case it is handled via PNG_ABORT()), but you could change this to do things like exit() if you should wish, as long as your function does not return. </p>
<p> On non-fatal errors, png_warning() is called to print a warning message, and then control returns to the calling code. By default png_error() and png_warning() print a message on stderr via fprintf() unless the library is compiled with PNG_NO_CONSOLE_IO defined (because you don&#8217;t want the messages) or PNG_NO_STDIO defined (because fprintf() isn&#8217;t available). If you wish to change the behavior of the error functions, you will need to set up your own message callbacks. These functions are normally supplied at the time that the png_struct is created. It is also possible to redirect errors and warnings to your own replacement functions after png_create_*_struct() has been called by calling: </p>
<p>&nbsp;<wbr>png_set_error_fn(png_structp png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>png_voidp error_ptr, png_error_ptr error_fn,<br />
&nbsp;<wbr>&nbsp;<wbr>png_error_ptr warning_fn); </p>
<p>&nbsp;<wbr>png_voidp error_ptr&nbsp;<wbr>=&nbsp;<wbr>png_get_error_ptr(png_ptr); </p>
<p> If NULL is supplied for either error_fn or warning_fn, then the libpng default function will be used, calling fprintf() and/or longjmp() if a problem is encountered. The replacement error functions should have parameters as follows: </p>
<p>&nbsp;<wbr>void user_error_fn(png_structp png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>png_const_charp error_msg); </p>
<p>&nbsp;<wbr>void user_warning_fn(png_structp png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>png_const_charp warning_msg); </p>
<p> The motivation behind using setjmp() and longjmp() is the C++ throw and catch exception handling methods. This makes the code much easier to write, as there is no need to check every return code of every function call. However, there are some uncertainties about the status of local variables after a longjmp, so the user may want to be careful about doing anything after setjmp returns non-zero besides returning itself. Consult your compiler documentation for more details. For an alternative approach, you may wish to use the &quot;cexcept&quot; facility (see <a rel="nofollow" href="http://cexcept.sourceforge.net">http://cexcept.sourceforge.net</a>), which is illustrated in pngvalid.c and in contrib/visupng. </p>
<h3>Custom chunks</h3>
<p> If you need to read or write custom chunks, you may need to get deeper into the libpng code. The library now has mechanisms for storing and writing chunks of unknown type; you can even declare callbacks for custom chunks. However, this may not be good enough if the library code itself needs to know about interactions between your chunk and existing `intrinsic&#8217; chunks. </p>
<p> If you need to write a new intrinsic chunk, first read the PNG specification. Acquire a first level of understanding of how it works. Pay particular attention to the sections that describe chunk names, and look at how other chunks were designed, so you can do things similarly. Second, check out the sections of libpng that read and write chunks. Try to find a chunk that is similar to yours and use it as a template. More details can be found in the comments inside the code. It is best to handle private or unknown chunks in a generic method, via callback functions, instead of by modifying libpng functions. This is illustrated in pngtest.c, which uses a callback function to handle a private &quot;vpAg&quot; chunk and the new &quot;sTER&quot; chunk, which are both unknown to libpng. </p>
<p> If you wish to write your own transformation for the data, look through the part of the code that does the transformations, and check out some of the simpler ones to get an idea of how they work. Try to find a similar transformation to the one you want to add and copy off of it. More details can be found in the comments inside the code itself. </p>
<h3>Configuring for 16-bit platforms</h3>
<p> You will want to look into zconf.h to tell zlib (and thus libpng) that it cannot allocate more then 64K at a time. Even if you can, the memory won&#8217;t be accessible. So limit zlib and libpng to 64K by defining MAXSEG_64K. </p>
<h3>Configuring for DOS</h3>
<p> For DOS users who only have access to the lower 640K, you will have to limit zlib&#8217;s memory usage via a png_set_compression_mem_level() call. See zlib.h or zconf.h in the zlib library for more information. </p>
<h3>Configuring for Medium Model</h3>
<p> Libpng&#8217;s support for medium model has been tested on most of the popular compilers. Make sure MAXSEG_64K gets defined, USE_FAR_KEYWORD gets defined, and FAR gets defined to far in pngconf.h, and you should be all set. Everything in the library (except for zlib&#8217;s structure) is expecting far data. You must use the typedefs with the p or pp on the end for pointers (or at least look at them and be careful). Make note that the rows of data are defined as png_bytepp, which is an &quot;unsigned char far * far *&quot;. </p>
<h3>Configuring for gui/windowing platforms:</h3>
<p> You will need to write new error and warning functions that use the GUI interface, as described previously, and set them to be the error and warning functions at the time that png_create_*_struct() is called, in order to have them available during the structure initialization. They can be changed later via png_set_error_fn(). On some compilers, you may also have to change the memory allocators (png_malloc, etc.). </p>
<h3>Configuring for compiler xxx:</h3>
<p> All includes for libpng are in pngconf.h. If you need to add, change or delete an include, this is the place to do it. The includes that are not needed outside libpng are placed in pngpriv.h, which is only used by the routines inside libpng itself. The files in libpng proper only include pngpriv.h and png.h, which %14%in turn includes pngconf.h. in turn includes pngconf.h and, as of libpng-1.5.0, pnglibconf.h. As of libpng-1.5.0, pngpriv.h also includes three other private header files, pngstruct.h, pnginfo.h, and pngdebug.h, which contain material that previously appeared in the public headers. </p>
<h3>Configuring zlib:</h3>
<p> There are special functions to configure the compression. Perhaps the most useful one changes the compression level, which currently uses input compression values in the range 0 &#8211; 9. The library normally uses the default compression level (Z_DEFAULT_COMPRESSION = 6). Tests have shown that for a large majority of images, compression values in the range 3-6 compress nearly as well as higher levels, and do so much faster. For online applications it may be desirable to have maximum speed (Z_BEST_SPEED = 1). With versions of zlib after v0.99, you can also specify no compression (Z_NO_COMPRESSION = 0), but this would create files larger than just storing the raw bitmap. You can specify the compression level by calling: </p>
<p>&nbsp;<wbr>#include zlib.h<br />
&nbsp;<wbr>png_set_compression_level(png_ptr, level); </p>
<p> Another useful one is to reduce the memory level used by the library. The memory level defaults to 8, but it can be lowered if you are short on memory (running DOS, for example, where you only have 640K). Note that the memory level does have an effect on compression; among other things, lower levels will result in sections of incompressible data being emitted in smaller stored blocks, with a correspondingly larger relative overhead of up to 15% in the worst case. </p>
<p>&nbsp;<wbr>#include zlib.h<br />
&nbsp;<wbr>png_set_compression_mem_level(png_ptr, level); </p>
<p> The other functions are for configuring zlib. They are not recommended for normal use and may result in writing an invalid PNG file. See zlib.h for more information on what these mean. </p>
<p>&nbsp;<wbr>#include zlib.h<br />
&nbsp;<wbr>png_set_compression_strategy(png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>strategy); </p>
<p>&nbsp;<wbr>png_set_compression_window_bits(png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>window_bits); </p>
<p>&nbsp;<wbr>png_set_compression_method(png_ptr, method); </p>
<p>&nbsp;<wbr>png_set_compression_buffer_size(png_ptr, size); </p>
<p> As of libpng version 1.5.4, additional APIs became available to set these separately for non-IDAT compressed chunks such as zTXt, iTXt, and iCCP: </p>
<p>&nbsp;<wbr>#include zlib.h<br />
&nbsp;<wbr>#if PNG_LIBPNG_VER&nbsp;<wbr>&gt;=&nbsp;<wbr>10504<br />
&nbsp;<wbr>png_set_text_compression_level(png_ptr, level); </p>
<p>&nbsp;<wbr>png_set_text_compression_mem_level(png_ptr, level); </p>
<p>&nbsp;<wbr>png_set_text_compression_strategy(png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>strategy); </p>
<p>&nbsp;<wbr>png_set_text_compression_window_bits(png_ptr,<br />
&nbsp;<wbr>&nbsp;<wbr>window_bits); </p>
<p>&nbsp;<wbr>png_set_text_compression_method(png_ptr, method);<br />
&nbsp;<wbr>#endif </p>
<h3>Controlling row filtering</h3>
<p> If you want to control whether libpng uses filtering or not, which filters are used, and how it goes about picking row filters, you can call one of these functions. The selection and configuration of row filters can have a significant impact on the size and encoding speed and a somewhat lesser impact on the decoding speed of an image. Filtering is enabled by default for RGB and grayscale images (with and without alpha), but not for paletted images nor for any images with bit depths less than 8 bits/pixel. </p>
<p> The &#8216;method&#8217; parameter sets the main filtering method, which is currently only &#8216;0&#8217; in the PNG 1.2 specification. The &#8216;filters&#8217; parameter sets which filter(s), if any, should be used for each scanline. Possible values are PNG_ALL_FILTERS and PNG_NO_FILTERS to turn filtering on and off, respectively. </p>
<p> Individual filter types are PNG_FILTER_NONE, PNG_FILTER_SUB, PNG_FILTER_UP, PNG_FILTER_AVG, PNG_FILTER_PAETH, which can be bitwise ORed together with &#8216;|&#8217; to specify one or more filters to use. These filters are described in more detail in the PNG specification. If you intend to change the filter type during the course of writing the image, you should start with flags set for all of the filters you intend to use so that libpng can initialize its internal structures appropriately for all of the filter types. (Note that this means the first row must always be adaptively filtered, because libpng currently does not allocate the filter buffers until png_write_row() is called for the first time.) </p>
<p>&nbsp;<wbr>filters&nbsp;<wbr>=&nbsp;<wbr>PNG_FILTER_NONE | PNG_FILTER_SUB<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_FILTER_UP | PNG_FILTER_AVG |<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_FILTER_PAETH | PNG_ALL_FILTERS; </p>
<p>&nbsp;<wbr>png_set_filter(png_ptr, PNG_FILTER_TYPE_BASE,<br />
&nbsp;<wbr>filters);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>The second parameter can also be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PNG_INTRAPIXEL_DIFFERENCING if you are<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>writing a PNG to be embedded in a MNG<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>datastream.&nbsp;<wbr>&nbsp;<wbr>This parameter must be the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>same as the value of filter_method used<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>in png_set_IHDR(). </p>
<p> It is also possible to influence how libpng chooses from among the available filters. This is done in one or both of two ways &#8211; by telling it how important it is to keep the same filter for successive rows, and by telling it the relative computational costs of the filters. </p>
<p>&nbsp;<wbr>double weights[3]&nbsp;<wbr>=&nbsp;<wbr>{1.5, 1.3, 1.1},<br />
&nbsp;<wbr>costs[PNG_FILTER_VALUE_LAST]&nbsp;<wbr>=<br />
&nbsp;<wbr>{1.0, 1.3, 1.3, 1.5, 1.7}; </p>
<p>&nbsp;<wbr>png_set_filter_heuristics(png_ptr,<br />
&nbsp;<wbr>PNG_FILTER_HEURISTIC_WEIGHTED, 3,<br />
&nbsp;<wbr>weights, costs); </p>
<p> The weights are multiplying factors that indicate to libpng that the row filter should be the same for successive rows unless another row filter is that many times better than the previous filter. In the above example, if the previous 3 filters were SUB, SUB, NONE, the SUB filter could have a &quot;sum of absolute differences&quot; 1.5 x 1.3 times higher than other filters and still be chosen, while the NONE filter could have a sum 1.1 times higher than other filters and still be chosen. Unspecified weights are taken to be 1.0, and the specified weights should probably be declining like those above in order to emphasize recent filters over older filters. </p>
<p> The filter costs specify for each filter type a relative decoding cost to be considered when selecting row filters. This means that filters with higher costs are less likely to be chosen over filters with lower costs, unless their &quot;sum of absolute differences&quot; is that much smaller. The costs do not necessarily reflect the exact computational speeds of the various filters, since this would unduly influence the final image size. </p>
<p> Note that the numbers above were invented purely for this example and are given only to help explain the function usage. Little testing has been done to find optimum values for either the costs or the weights. </p>
<h3>Removing unwanted object code</h3>
<p> There are a bunch of #define&#8217;s in pngconf.h that control what parts of libpng are compiled. All the defines end in _SUPPORTED. If you are never going to use a capability, you can change the #define to #undef before recompiling libpng and save yourself code and data space, or you can turn off individual capabilities with defines that begin with PNG_NO_. </p>
<p> In libpng-1.5.0 and later, the #define&#8217;s are in pnglibconf.h instead. </p>
<p> You can also turn all of the transforms and ancillary chunk capabilities off en masse with compiler directives that define PNG_NO_READ[or WRITE]_TRANSFORMS, or PNG_NO_READ[or WRITE]_ANCILLARY_CHUNKS, or all four, along with directives to turn on any of the capabilities that you do want. The PNG_NO_READ[or WRITE]_TRANSFORMS directives disable the extra transformations but still leave the library fully capable of reading and writing PNG files with all known public chunks. Use of the PNG_NO_READ[or WRITE]_ANCILLARY_CHUNKS directive produces a library that is incapable of reading or writing ancillary chunks. If you are not using the progressive reading capability, you can turn that off with PNG_NO_PROGRESSIVE_READ (don&#8217;t confuse this with the INTERLACING capability, which you&#8217;ll still have). </p>
<p> All the reading and writing specific code are in separate files, so the linker should only grab the files it needs. However, if you want to make sure, or if you are building a stand alone library, all the reading files start with &quot;pngr&quot; and all the writing files start with &quot;pngw&quot;. The files that don&#8217;t match either (like png.c, pngtrans.c, etc.) are used for both reading and writing, and always need to be included. The progressive reader is in pngpread.c </p>
<p> If you are creating or distributing a dynamically linked library (a .so or DLL file), you should not remove or disable any parts of the library, as this will cause applications linked with different versions of the library to fail if they call functions not available in your library. The size of the library itself should not be an issue, because only those sections that are actually used will be loaded into memory. </p>
<h3>Requesting debug printout</h3>
<p> The macro definition PNG_DEBUG can be used to request debugging printout. Set it to an integer value in the range 0 to 3. Higher numbers result in increasing amounts of debugging information. The information is printed to the &quot;stderr&quot; file, unless another file name is specified in the PNG_DEBUG_FILE macro definition. </p>
<p> When PNG_DEBUG &gt; 0, the following functions (macros) become available: </p>
<p>png_debug(level, message)<br />
png_debug1(level, message, p1)<br />
png_debug2(level, message, p1, p2) </p>
<p> in which &quot;level&quot; is compared to PNG_DEBUG to decide whether to print the message, &quot;message&quot; is the formatted string to be printed, and p1 and p2 are parameters that are to be embedded in the string according to printf-style formatting directives. For example, </p>
<p>png_debug1(2,&nbsp;<wbr>&quot;foo=%d, foo); </p>
<p> is expanded to </p>
<p>if&nbsp;<wbr>(PNG_DEBUG&nbsp;<wbr>&gt;&nbsp;<wbr>2)<br />
fprintf(PNG_DEBUG_FILE,&nbsp;<wbr>&quot;foo=%d, foo); </p>
<p> When PNG_DEBUG is defined but is zero, the macros aren&#8217;t defined, but you can still use PNG_DEBUG to control your own debugging: </p>
<p>#ifdef PNG_DEBUG<br />
&nbsp;<wbr>fprintf(stderr, &#8230;<br />
#endif </p>
<p> When PNG_DEBUG = 1, the macros are defined, but only png_debug statements having level = 0 will be printed. There aren&#8217;t any such statements in this version of libpng, but if you insert some they will be printed. </p>
<h2>VI. MNG support</h2>
<p> The MNG specification (available at <a rel="nofollow" href="http://www.libpng.org/pub/mng)">http://www.libpng.org/pub/mng)</a> allows certain extensions to PNG for PNG images that are embedded in MNG datastreams. Libpng can support some of these extensions. To enable them, use the png_permit_mng_features() function: </p>
<p>feature_set&nbsp;<wbr>=&nbsp;<wbr>png_permit_mng_features(png_ptr, mask) </p>
<p>mask is a png_uint_32 containing the bitwise OR of the<br />
&nbsp;<wbr>&nbsp;<wbr>features you want to enable.&nbsp;<wbr>&nbsp;<wbr>These include<br />
&nbsp;<wbr>&nbsp;<wbr>PNG_FLAG_MNG_EMPTY_PLTE<br />
&nbsp;<wbr>&nbsp;<wbr>PNG_FLAG_MNG_FILTER_64<br />
&nbsp;<wbr>&nbsp;<wbr>PNG_ALL_MNG_FEATURES </p>
<p>feature_set is a png_uint_32 that is the bitwise AND of<br />
your mask with the set of MNG features that is<br />
supported by the version of libpng that you are using. </p>
<p> It is an error to use this function when reading or writing a standalone PNG file with the PNG 8-byte signature. The PNG datastream must be wrapped in a MNG datastream. As a minimum, it must have the MNG 8-byte signature and the MHDR and MEND chunks. Libpng does not provide support for these or any other MNG chunks; your application must provide its own support for them. You may wish to consider using libmng (available at <a rel="nofollow" href="http://www.libmng.com)">http://www.libmng.com)</a> instead. </p>
<h2>VII. Changes to Libpng from version 0.88</h2>
<p> It should be noted that versions of libpng later than 0.96 are not distributed by the original libpng author, Guy Schalnat, nor by Andreas Dilger, who had taken over from Guy during 1996 and 1997, and distributed versions 0.89 through 0.96, but rather by another member of the original PNG Group, Glenn Randers-Pehrson. Guy and Andreas are still alive and well, but they have moved on to other things. </p>
<p> The old libpng functions png_read_init(), png_write_init(), png_info_init(), png_read_destroy(), and png_write_destroy() have been moved to PNG_INTERNAL in version 0.95 to discourage their use. These functions will be removed from libpng version 1.4.0. </p>
<p> The preferred method of creating and initializing the libpng structures is via the png_create_read_struct(), png_create_write_struct(), and png_create_info_struct() because they isolate the size of the structures from the application, allow version error checking, and also allow the use of custom error handling routines during the initialization, which the old functions do not. The functions png_read_destroy() and png_write_destroy() do not actually free the memory that libpng allocated for these structs, but just reset the data structures, so they can be used instead of png_destroy_read_struct() and png_destroy_write_struct() if you feel there is too much system overhead allocating and freeing the png_struct for each image read. </p>
<p> Setting the error callbacks via png_set_message_fn() before png_read_init() as was suggested in libpng-0.88 is no longer supported because this caused applications that do not use custom error functions to fail if the png_ptr was not initialized to zero. It is still possible to set the error callbacks AFTER png_read_init(), or to change them with png_set_error_fn(), which is essentially the same function, but with a new name to force compilation errors with applications that try to use the old method. </p>
<p> Starting with version 1.0.7, you can find out which version of the library you are using at run-time: </p>
<p>png_uint_32 libpng_vn&nbsp;<wbr>=&nbsp;<wbr>png_access_version_number(); </p>
<p> The number libpng_vn is constructed from the major version, minor version with leading zero, and release number with leading zero, (e.g., libpng_vn for version 1.0.7 is 10007). </p>
<p> Note that this function does not take a png_ptr, so you can call it before you&#8217;ve created one. </p>
<p> You can also check which version of png.h you used when compiling your application: </p>
<p>png_uint_32 application_vn&nbsp;<wbr>=&nbsp;<wbr>PNG_LIBPNG_VER; </p>
<h2>VIII. Changes to Libpng from version 1.0.x to 1.2.x</h2>
<p> Support for user memory management was enabled by default. To accomplish this, the functions png_create_read_struct_2(), png_create_write_struct_2(), png_set_mem_fn(), png_get_mem_ptr(), png_malloc_default(), and png_free_default() were added. </p>
<p> Support for the iTXt chunk has been enabled by default as of version 1.2.41. </p>
<p> Support for certain MNG features was enabled. </p>
<p> Support for numbered error messages was added. However, we never got around to actually numbering the error messages. The function png_set_strip_error_numbers() was added (Note: the prototype for this function was inadvertently removed from png.h in PNG_NO_ASSEMBLER_CODE builds of libpng-1.2.15. It was restored in libpng-1.2.36). </p>
<p> The png_malloc_warn() function was added at libpng-1.2.3. This issues a png_warning and returns NULL instead of aborting when it fails to acquire the requested memory allocation. </p>
<p> Support for setting user limits on image width and height was enabled by default. The functions png_set_user_limits(), png_get_user_width_max(), and png_get_user_height_max() were added at libpng-1.2.6. </p>
<p> The png_set_add_alpha() function was added at libpng-1.2.7. </p>
<p> The function png_set_expand_gray_1_2_4_to_8() was added at libpng-1.2.9. Unlike png_set_gray_1_2_4_to_8(), the new function does not expand the tRNS chunk to alpha. The png_set_gray_1_2_4_to_8() function is deprecated. </p>
<p> A number of macro definitions in support of runtime selection of assembler code features (especially Intel MMX code support) were added at libpng-1.2.0: </p>
<p>&nbsp;<wbr>PNG_ASM_FLAG_MMX_SUPPORT_COMPILED<br />
&nbsp;<wbr>PNG_ASM_FLAG_MMX_SUPPORT_IN_CPU<br />
&nbsp;<wbr>PNG_ASM_FLAG_MMX_READ_COMBINE_ROW<br />
&nbsp;<wbr>PNG_ASM_FLAG_MMX_READ_INTERLACE<br />
&nbsp;<wbr>PNG_ASM_FLAG_MMX_READ_FILTER_SUB<br />
&nbsp;<wbr>PNG_ASM_FLAG_MMX_READ_FILTER_UP<br />
&nbsp;<wbr>PNG_ASM_FLAG_MMX_READ_FILTER_AVG<br />
&nbsp;<wbr>PNG_ASM_FLAG_MMX_READ_FILTER_PAETH<br />
&nbsp;<wbr>PNG_ASM_FLAGS_INITIALIZED<br />
&nbsp;<wbr>PNG_MMX_READ_FLAGS<br />
&nbsp;<wbr>PNG_MMX_FLAGS<br />
&nbsp;<wbr>PNG_MMX_WRITE_FLAGS<br />
&nbsp;<wbr>PNG_MMX_FLAGS </p>
<p> We added the following functions in support of runtime selection of assembler code features: </p>
<p>&nbsp;<wbr>png_get_mmx_flagmask()<br />
&nbsp;<wbr>png_set_mmx_thresholds()<br />
&nbsp;<wbr>png_get_asm_flags()<br />
&nbsp;<wbr>png_get_mmx_bitdepth_threshold()<br />
&nbsp;<wbr>png_get_mmx_rowbytes_threshold()<br />
&nbsp;<wbr>png_set_asm_flags() </p>
<p> We replaced all of these functions with simple stubs in libpng-1.2.20, when the Intel assembler code was removed due to a licensing issue. </p>
<p> These macros are deprecated: </p>
<p>&nbsp;<wbr>PNG_READ_TRANSFORMS_NOT_SUPPORTED<br />
&nbsp;<wbr>PNG_PROGRESSIVE_READ_NOT_SUPPORTED<br />
&nbsp;<wbr>PNG_NO_SEQUENTIAL_READ_SUPPORTED<br />
&nbsp;<wbr>PNG_WRITE_TRANSFORMS_NOT_SUPPORTED<br />
&nbsp;<wbr>PNG_READ_ANCILLARY_CHUNKS_NOT_SUPPORTED<br />
&nbsp;<wbr>PNG_WRITE_ANCILLARY_CHUNKS_NOT_SUPPORTED </p>
<p> They have been replaced, respectively, by: </p>
<p>&nbsp;<wbr>PNG_NO_READ_TRANSFORMS<br />
&nbsp;<wbr>PNG_NO_PROGRESSIVE_READ<br />
&nbsp;<wbr>PNG_NO_SEQUENTIAL_READ<br />
&nbsp;<wbr>PNG_NO_WRITE_TRANSFORMS<br />
&nbsp;<wbr>PNG_NO_READ_ANCILLARY_CHUNKS<br />
&nbsp;<wbr>PNG_NO_WRITE_ANCILLARY_CHUNKS </p>
<p> PNG_MAX_UINT was replaced with PNG_UINT_31_MAX. It has been deprecated since libpng-1.0.16 and libpng-1.2.6. </p>
<p> The function<br />
&nbsp;<wbr>png_check_sig(sig, num) was replaced with<br />
&nbsp;<wbr>!png_sig_cmp(sig, 0, num) It has been deprecated since libpng-0.90. </p>
<p> The function<br />
&nbsp;<wbr>png_set_gray_1_2_4_to_8() which also expands tRNS to alpha was replaced with<br />
&nbsp;<wbr>png_set_expand_gray_1_2_4_to_8() which does not. It has been deprecated since libpng-1.0.18 and 1.2.9. </p>
<h2>IX. Changes to Libpng from version 1.0.x/1.2.x to 1.4.x</h2>
<p> Private libpng prototypes and macro definitions were moved from png.h and pngconf.h into a new pngpriv.h header file. </p>
<p> Functions png_set_benign_errors(), png_benign_error(), and png_chunk_benign_error() were added. </p>
<p> Support for setting the maximum amount of memory that the application will allocate for reading chunks was added, as a security measure. The functions png_set_chunk_cache_max() and png_get_chunk_cache_max() were added to the library. </p>
<p> We implemented support for I/O states by adding png_ptr member io_state and functions png_get_io_chunk_name() and png_get_io_state() in pngget.c </p>
<p> We added PNG_TRANSFORM_GRAY_TO_RGB to the available high-level input transforms. </p>
<p> Checking for and reporting of errors in the IHDR chunk is more thorough. </p>
<p> Support for global arrays was removed, to improve thread safety. </p>
<p> Some obsolete/deprecated macros and functions have been removed. </p>
<p> Typecasted NULL definitions such as<br />
#define png_voidp_NULL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(png_voidp)NULL were eliminated. If you used these in your application, just use NULL instead. </p>
<p> The png_struct and info_struct members &quot;trans&quot; and &quot;trans_values&quot; were changed to &quot;trans_alpha&quot; and &quot;trans_color&quot;, respectively. </p>
<p> The obsolete, unused pnggccrd.c and pngvcrd.c files and related makefiles were removed. </p>
<p> The PNG_1_0_X and PNG_1_2_X macros were eliminated. </p>
<p> The PNG_LEGACY_SUPPORTED macro was eliminated. </p>
<p> Many WIN32_WCE #ifdefs were removed. </p>
<p> The functions png_read_init(info_ptr), png_write_init(info_ptr), png_info_init(info_ptr), png_read_destroy(), and png_write_destroy() have been removed. They have been deprecated since libpng-0.95. </p>
<p> The png_permit_empty_plte() was removed. It has been deprecated since libpng-1.0.9. Use png_permit_mng_features() instead. </p>
<p> We removed the obsolete stub functions png_get_mmx_flagmask(), png_set_mmx_thresholds(), png_get_asm_flags(), png_get_mmx_bitdepth_threshold(), png_get_mmx_rowbytes_threshold(), png_set_asm_flags(), and png_mmx_supported() </p>
<p> We removed the obsolete png_check_sig(), png_memcpy_check(), and png_memset_check() functions. Instead use !png_sig_cmp(), png_memcpy(), and png_memset(), respectively. </p>
<p> The function png_set_gray_1_2_4_to_8() was removed. It has been deprecated since libpng-1.0.18 and 1.2.9, when it was replaced with png_set_expand_gray_1_2_4_to_8() because the former function also expanded any tRNS chunk to an alpha channel. </p>
<p> Macros for png_get_uint_16, png_get_uint_32, and png_get_int_32 were added and are used by default instead of the corresponding functions. Unfortunately, from libpng-1.4.0 until 1.4.4, the png_get_uint_16 macro (but not the function) incorrectly returned a value of type png_uint_32. </p>
<p> We changed the prototype for png_malloc() from<br />
&nbsp;<wbr>png_malloc(png_structp png_ptr, png_uint_32 size) to<br />
&nbsp;<wbr>png_malloc(png_structp png_ptr, png_alloc_size_t size) </p>
<p> This also applies to the prototype for the user replacement malloc_fn(). </p>
<p> The png_calloc() function was added and is used in place of of &quot;png_malloc(); memset();&quot; except in the case in png_read_png() where the array consists of pointers; in this case a &quot;for&quot; loop is used after the png_malloc() to set the pointers to NULL, to give robust. behavior in case the application runs out of memory part-way through the process. </p>
<p> We changed the prototypes of png_get_compression_buffer_size() and png_set_compression_buffer_size() to work with png_size_t instead of png_uint_32. </p>
<p> Support for numbered error messages was removed by default, since we never got around to actually numbering the error messages. The function png_set_strip_error_numbers() was removed from the library by default. </p>
<p> The png_zalloc() and png_zfree() functions are no longer exported. The png_zalloc() function no longer zeroes out the memory that it allocates. Applications that called png_zalloc(png_ptr, number, size) can call png_calloc(png_ptr, number*size) instead, and can call png_free() instead of png_zfree(). </p>
<p> Support for dithering was disabled by default in libpng-1.4.0, because it has not been well tested and doesn&#8217;t actually &quot;dither&quot;. The code was not removed, however, and could be enabled by building libpng with PNG_READ_DITHER_SUPPORTED defined. In libpng-1.4.2, this support was reenabled, but the function was renamed png_set_quantize() to reflect more accurately what it actually does. At the same time, the PNG_DITHER_[RED,GREEN_BLUE]_BITS macros were also renamed to PNG_QUANTIZE_[RED,GREEN,BLUE]_BITS, and PNG_READ_DITHER_SUPPORTED was renamed to PNG_READ_QUANTIZE_SUPPORTED. </p>
<p> We removed the trailing &#8216;.&#8217; from the warning and error messages. </p>
<h2>X. Changes to Libpng from version 1.4.x to 1.5.x</h2>
<p> From libpng-1.4.0 until 1.4.4, the png_get_uint_16 macro (but not the function) incorrectly returned a value of type png_uint_32. </p>
<p> Checking for invalid palette index on read or write was added at libpng 1.5.10. When an invalid index is found, libpng issues a benign error. This is enabled by default but can be disabled in each png_ptr with </p>
<p>png_set_check_for_invalid_index(png_ptr, allowed); </p>
<p>allowed&nbsp;<wbr>&nbsp;<wbr>&#8211; one of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0: disable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1: enable </p>
<p> A. Changes that affect users of libpng </p>
<p> There are no substantial API changes between the non-deprecated parts of the 1.4.5 API and the 1.5.0 API; however, the ability to directly access members of the main libpng control structures, png_struct and png_info, deprecated in earlier versions of libpng, has been completely removed from libpng 1.5. </p>
<p> We no longer include zlib.h in png.h. Applications that need access to information in zlib.h will need to add the &#8216;#include &quot;zlib.h&quot;&#8217; directive. It does not matter whether it is placed prior to or after the &#8216;&quot;#include png.h&quot;&#8217; directive. </p>
<p> The png_sprintf(), png_strcpy(), and png_strncpy() macros are no longer used and were removed. </p>
<p> We moved the png_strlen(), png_memcpy(), png_memset(), and png_memcmp() macros into a private header file (pngpriv.h) that is not accessible to applications. </p>
<p> In png_get_iCCP, the type of &quot;profile&quot; was changed from png_charpp to png_bytepp, and in png_set_iCCP, from png_charp to png_const_bytep. </p>
<p> There are changes of form in png.h, including new and changed macros to declare parts of the API. Some API functions with arguments that are pointers to data not modified within the function have been corrected to declare these arguments with PNG_CONST. </p>
<p> Much of the internal use of C macros to control the library build has also changed and some of this is visible in the exported header files, in particular the use of macros to control data and API elements visible during application compilation may require significant revision to application code. (It is extremely rare for an application to do this.) </p>
<p> Any program that compiled against libpng 1.4 and did not use deprecated features or access internal library structures should compile and work against libpng 1.5, except for the change in the prototype for png_get_iCCP() and png_set_iCCP() API functions mentioned above. </p>
<p> libpng 1.5.0 adds PNG_ PASS macros to help in the reading and writing of interlaced images. The macros return the number of rows and columns in each pass and information that can be used to de-interlace and (if absolutely necessary) interlace an image. </p>
<p> libpng 1.5.0 adds an API png_longjmp(png_ptr, value). This API calls the application-provided png_longjmp_ptr on the internal, but application initialized, longjmp buffer. It is provided as a convenience to avoid the need to use the png_jmpbuf macro, which had the unnecessary side effect of resetting the internal png_longjmp_ptr value. </p>
<p> libpng 1.5.0 includes a complete fixed point API. By default this is present along with the corresponding floating point API. In general the fixed point API is faster and smaller than the floating point one because the PNG file format used fixed point, not floating point. This applies even if the library uses floating point in internal calculations. A new macro, PNG_FLOATING_ARITHMETIC_SUPPORTED, reveals whether the library uses floating point arithmetic (the default) or fixed point arithmetic internally for performance critical calculations such as gamma correction. In some cases, the gamma calculations may produce slightly different results. This has changed the results in png_rgb_to_gray and in alpha composition (png_set_background for example). This applies even if the original image was already linear (gamma == 1.0) and, therefore, it is not necessary to linearize the image. This is because libpng has *not* been changed to optimize that case correctly, yet. </p>
<p> Fixed point support for the sCAL chunk comes with an important caveat; the sCAL specification uses a decimal encoding of floating point values and the accuracy of PNG fixed point values is insufficient for representation of these values. Consequently a &quot;string&quot; API (png_get_sCAL_s and png_set_sCAL_s) is the only reliable way of reading arbitrary sCAL chunks in the absence of either the floating point API or internal floating point calculations. </p>
<p> Applications no longer need to include the optional distribution header file pngusr.h or define the corresponding macros during application build in order to see the correct variant of the libpng API. From 1.5.0 application code can check for the corresponding _SUPPORTED macro: </p>
<p> #ifdef PNG_INCH_CONVERSIONS_SUPPORTED<br />
/*&nbsp;<wbr>code that uses the inch conversion APIs.&nbsp;<wbr>*/ #endif </p>
<p> This macro will only be defined if the inch conversion functions have been compiled into libpng. The full set of macros, and whether or not support has been compiled in, are available in the header file pnglibconf.h. This header file is specific to the libpng build. Notice that prior to 1.5.0 the _SUPPORTED macros would always have the default definition unless reset by pngusr.h or by explicit settings on the compiler command line. These settings may produce compiler warnings or errors in 1.5.0 because of macro redefinition. </p>
<p> From libpng-1.4.0 until 1.4.4, the png_get_uint_16 macro (but not the function) incorrectly returned a value of type png_uint_32. libpng 1.5.0 is consistent with the implementation in 1.4.5 and 1.2.x (where the macro did not exist.) </p>
<p> Applications can now choose whether to use these macros or to call the corresponding function by defining PNG_USE_READ_MACROS or PNG_NO_USE_READ_MACROS before including png.h. Notice that this is only supported from 1.5.0 -defining PNG_NO_USE_READ_MACROS prior to 1.5.0 will lead to a link failure. </p>
<p> Prior to libpng-1.5.4, the zlib compressor used the same set of parameters when compressing the IDAT data and textual data such as zTXt and iCCP. In libpng-1.5.4 we reinitialized the zlib stream for each type of data. We added five png_set_text_*() functions for setting the parameters to use with textual data. </p>
<p> Prior to libpng-1.5.4, the PNG_READ_16_TO_8_ACCURATE_SCALE_SUPPORTED option was off by default, and slightly inaccurate scaling occurred. This option can no longer be turned off, and the choice of accurate or inaccurate 16-to-8 scaling is by using the new png_set_scale_16_to_8() API for accurate scaling or the old png_set_strip_16_to_8() API for simple chopping. </p>
<p> Prior to libpng-1.5.4, the png_set_user_limits() function could only be used to reduce the width and height limits from the value of PNG_USER_WIDTH_MAX and PNG_USER_HEIGHT_MAX, although this document said that it could be used to override them. Now this function will reduce or increase the limits. </p>
<p> Starting in libpng-1.5.10, the user limits can be set en masse with the configuration option PNG_SAFE_LIMITS_SUPPORTED. If this option is enabled, a set of &quot;safe&quot; limits is applied in pngpriv.h. These can be overridden by application calls to png_set_user_limits(), png_set_user_chunk_cache_max(), and/or png_set_user_malloc_max() that increase or decrease the limits. Also, in libpng-1.5.10 the default width and height limits were increased from 1,000,000 to 0x7ffffff (i.e., made unlimited). Therefore, the limits are now<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>default&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>safe<br />
png_user_width_max&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x7fffffff&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1,000,000<br />
png_user_height_max&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x7fffffff&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1,000,000<br />
png_user_chunk_cache_max&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>(unlimited)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>128<br />
png_user_chunk_malloc_max 0&nbsp;<wbr>(unlimited)&nbsp;<wbr>8,000,000 </p>
<p> B. Changes to the build and configuration of libpng </p>
<p> Details of internal changes to the library code can be found in the CHANGES file and in the GIT repository logs. These will be of no concern to the vast majority of library users or builders; however, the few who configure libpng to a non-default feature set may need to change how this is done. </p>
<p> There should be no need for library builders to alter build scripts if these use the distributed build support &#8211; configure or the makefiles &#8211; however, users of the makefiles may care to update their build scripts to build pnglibconf.h where the corresponding makefile does not do so. </p>
<p> Building libpng with a non-default configuration has changed completely. The old method using pngusr.h should still work correctly even though the way pngusr.h is used in the build has been changed; however, library builders will probably want to examine the changes to take advantage of new capabilities and to simplify their build system. </p>
<p> B.1 Specific changes to library configuration capabilities </p>
<p> The library now supports a complete fixed point implementation and can thus be used on systems that have no floating point support or very limited or slow support. Previously gamma correction, an essential part of complete PNG support, required reasonably fast floating point. </p>
<p> As part of this the choice of internal implementation has been made independent of the choice of fixed versus floating point APIs and all the missing fixed point APIs have been implemented. </p>
<p> The exact mechanism used to control attributes of API functions has changed. A single set of operating system independent macro definitions is used and operating system specific directives are defined in pnglibconf.h </p>
<p> As part of this the mechanism used to choose procedure call standards on those systems that allow a choice has been changed. At present this only affects certain Microsoft (DOS, Windows) and IBM (OS/2) operating systems running on Intel processors. As before, PNGAPI is defined where required to control the exported API functions; however, two new macros, PNGCBAPI and PNGCAPI, are used instead for callback functions (PNGCBAPI) and (PNGCAPI) for functions that must match a C library prototype (currently only png_longjmp_ptr, which must match the C longjmp function.) The new approach is documented in pngconf.h </p>
<p> Despite these changes, libpng 1.5.0 only supports the native C function calling standard on those platforms tested so far (__cdecl on Microsoft Windows). This is because the support requirements for alternative calling conventions seem to no longer exist. Developers who find it necessary to set PNG_API_RULE to 1 should advise the mailing list (png-mng-implement) of this and library builders who use Openwatcom and therefore set PNG_API_RULE to 2 should also contact the mailing list. </p>
<p> A new test program, pngvalid, is provided in addition to pngtest. pngvalid validates the arithmetic accuracy of the gamma correction calculations and includes a number of validations of the file format. A subset of the full range of tests is run when &quot;make check&quot; is done (in the &#8216;configure&#8217; build.) pngvalid also allows total allocated memory usage to be evaluated and performs additional memory overwrite validation. </p>
<p> Many changes to individual feature macros have been made. The following are the changes most likely to be noticed by library builders who configure libpng: </p>
<p> 1) All feature macros now have consistent naming: </p>
<p> #define PNG_NO_feature turns the feature off #define PNG_feature_SUPPORTED turns the feature on </p>
<p> pnglibconf.h contains one line for each feature macro which is either: </p>
<p> #define PNG_feature_SUPPORTED </p>
<p> if the feature is supported or: </p>
<p> /*#undef PNG_feature_SUPPORTED*/ </p>
<p> if it is not. Library code consistently checks for the &#8216;SUPPORTED&#8217; macro. It does not, and libpng applications should not, check for the &#8216;NO&#8217; macro which will not normally be defined even if the feature is not supported. The &#8216;NO&#8217; macros are only used internally for setting or not setting the corresponding &#8216;SUPPORTED&#8217; macros. </p>
<p> Compatibility with the old names is provided as follows: </p>
<p> PNG_INCH_CONVERSIONS turns on PNG_INCH_CONVERSIONS_SUPPORTED </p>
<p> And the following definitions disable the corresponding feature: </p>
<p> PNG_SETJMP_NOT_SUPPORTED disables SETJMP PNG_READ_TRANSFORMS_NOT_SUPPORTED disables READ_TRANSFORMS PNG_NO_READ_COMPOSITED_NODIV disables READ_COMPOSITE_NODIV PNG_WRITE_TRANSFORMS_NOT_SUPPORTED disables WRITE_TRANSFORMS PNG_READ_ANCILLARY_CHUNKS_NOT_SUPPORTED disables READ_ANCILLARY_CHUNKS PNG_WRITE_ANCILLARY_CHUNKS_NOT_SUPPORTED disables WRITE_ANCILLARY_CHUNKS </p>
<p> Library builders should remove use of the above, inconsistent, names. </p>
<p> 2) Warning and error message formatting was previously conditional on the STDIO feature. The library has been changed to use the CONSOLE_IO feature instead. This means that if CONSOLE_IO is disabled the library no longer uses the <a href="/docs/linux/man/3-printf/">printf</a>(3) functions, even though the default read/write implementations use (FILE) style stdio.h functions. </p>
<p> 3) Three feature macros now control the fixed/floating point decisions: </p>
<p> PNG_FLOATING_POINT_SUPPORTED enables the floating point APIs </p>
<p> PNG_FIXED_POINT_SUPPORTED enables the fixed point APIs; however, in practice these are normally required internally anyway (because the PNG file format is fixed point), therefore in most cases PNG_NO_FIXED_POINT merely stops the function from being exported. </p>
<p> PNG_FLOATING_ARITHMETIC_SUPPORTED chooses between the internal floating point implementation or the fixed point one. Typically the fixed point implementation is larger and slower than the floating point implementation on a system that supports floating point; however, it may be faster on a system which lacks floating point hardware and therefore uses a software emulation. </p>
<p> 4) Added PNG_{READ,WRITE}_INT_FUNCTIONS_SUPPORTED. This allows the functions to read and write ints to be disabled independently of PNG_USE_READ_MACROS, which allows libpng to be built with the functions even though the default is to use the macros &#8211; this allows applications to choose at app buildtime whether or not to use macros (previously impossible because the functions weren&#8217;t in the default build.) </p>
<p> B.2 Changes to the configuration mechanism </p>
<p> Prior to libpng-1.5.0 library builders who needed to configure libpng had either to modify the exported pngconf.h header file to add system specific configuration or had to write feature selection macros into pngusr.h and cause this to be included into pngconf.h by defining PNG_USER_CONFIG. The latter mechanism had the disadvantage that an application built without PNG_USER_CONFIG defined would see the unmodified, default, libpng API and thus would probably fail to link. </p>
<p> These mechanisms still work in the configure build and in any makefile build that builds pnglibconf.h, although the feature selection macros have changed somewhat as described above. In 1.5.0, however, pngusr.h is processed only once, when the exported header file pnglibconf.h is built. pngconf.h no longer includes pngusr.h, therefore pngusr.h is ignored after the build of pnglibconf.h and it is never included in an application build. </p>
<p> The rarely used alternative of adding a list of feature macros to the CFLAGS setting in the build also still works; however, the macros will be copied to pnglibconf.h and this may produce macro redefinition warnings when the individual C files are compiled. </p>
<p> All configuration now only works if pnglibconf.h is built from scripts/pnglibconf.dfa. This requires the program awk. Brian Kernighan (the original author of awk) maintains C source code of that awk and this and all known later implementations (often called by subtly different names &#8211; nawk and gawk for example) are adequate to build pnglibconf.h. The Sun Microsystems (now Oracle) program &#8216;awk&#8217; is an earlier version and does not work; this may also apply to other systems that have a functioning awk called &#8216;nawk&#8217;. </p>
<p> Configuration options are now documented in scripts/pnglibconf.dfa. This file also includes dependency information that ensures a configuration is consistent; that is, if a feature is switched off dependent features are also removed. As a recommended alternative to using feature macros in pngusr.h a system builder may also define equivalent options in pngusr.dfa (or, indeed, any file) and add that to the configuration by setting DFA_XTRA to the file name. The makefiles in contrib/pngminim illustrate how to do this, and a case where pngusr.h is still required. </p>
<h2>XI. Detecting libpng</h2>
<p> The png_get_io_ptr() function has been present since libpng-0.88, has never changed, and is unaffected by conditional compilation macros. It is the best choice for use in configure scripts for detecting the presence of any libpng version since 0.88. In an autoconf &quot;configure.in&quot; you could use </p>
<p>&nbsp;<wbr>AC_CHECK_LIB(png, png_get_io_ptr, &#8230; </p>
<h2>XII. Source code repository</h2>
<p> Since about February 2009, version 1.2.34, libpng has been under &quot;git&quot; source control. The git repository was built from old libpng-x.y.z.tar.gz files going back to version 0.70. You can access the git repository (read only) at </p>
<p>&nbsp;<wbr><a href="git://libpng.git.sourceforge.net/gitroot/libpng">git://libpng.git.sourceforge.net/gitroot/libpng</a> </p>
<p> or you can browse it via &quot;gitweb&quot; at </p>
<p>&nbsp;<wbr><a rel="nofollow" href="http://libpng.git.sourceforge.net/git/gitweb.cgi?p=libpng">http://libpng.git.sourceforge.net/git/gitweb.cgi?p=libpng</a> </p>
<p> Patches can be sent to glennrp at users.sourceforge.net or to png-mng-implement at lists.sourceforge.net or you can upload them to the libpng bug tracker at </p>
<p>&nbsp;<wbr><a rel="nofollow" href="http://libpng.sourceforge.net">http://libpng.sourceforge.net</a> </p>
<p> We also accept patches built from the tar or zip distributions, and simple verbal discriptions of bug fixes, reported either to the SourceForge bug tracker, to the png-mng-implement at lists.sf.net mailing list, or directly to glennrp. </p>
<h2>XIII. Coding style</h2>
<p> Our coding style is similar to the &quot;Allman&quot; style, with curly braces on separate lines: </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(condition)<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>action;<br />
&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>else if&nbsp;<wbr>(another condition)<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>another action;<br />
&nbsp;<wbr>} </p>
<p> The braces can be omitted from simple one-line actions: </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>(condition)<br />
&nbsp;<wbr>return&nbsp;<wbr>(0); </p>
<p> We use 3-space indentation, except for continued statements which are usually indented the same as the first line of the statement plus four more spaces. </p>
<p> For macro definitions we use 2-space indentation, always leaving the &quot;#&quot; in the first column. </p>
<p>&nbsp;<wbr>#ifndef PNG_NO_FEATURE<br />
&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>ifndef PNG_FEATURE_SUPPORTED<br />
&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>define PNG_FEATURE_SUPPORTED<br />
&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>endif<br />
&nbsp;<wbr>#endif </p>
<p> Comments appear with the leading &quot;/*&quot; at the same indentation as the statement that follows the comment: </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>Single-line comment&nbsp;<wbr>*/<br />
&nbsp;<wbr>statement; </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>This is a multiple-line<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>comment.<br />
&nbsp;<wbr>&nbsp;<wbr>*/<br />
&nbsp;<wbr>statement; </p>
<p> Very short comments can be placed after the end of the statement to which they pertain: </p>
<p>&nbsp;<wbr>statement;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>comment&nbsp;<wbr>*/ </p>
<p> We don&#8217;t use C++ style (&quot;//&quot;) comments. We have, however, used them in the past in some now-abandoned MMX assembler code. </p>
<p> Functions and their curly braces are not indented, and exported functions are marked with PNGAPI: </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>This is a public function that is visible to<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>application programmers. It does thus-and-so.<br />
&nbsp;<wbr>&nbsp;<wbr>*/<br />
&nbsp;<wbr>void PNGAPI<br />
&nbsp;<wbr>png_exported_function(png_ptr, png_info, foo)<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>body;<br />
&nbsp;<wbr>} </p>
<p> The prototypes for all exported functions appear in png.h, above the comment that says </p>
<p>&nbsp;<wbr>/*&nbsp;<wbr>Maintainer: Put new public prototypes here &#8230;&nbsp;<wbr>*/ </p>
<p> We mark all non-exported functions with &quot;/* PRIVATE */&quot;&quot;: </p>
<p>&nbsp;<wbr>void&nbsp;<wbr>/*&nbsp;<wbr>PRIVATE&nbsp;<wbr>*/<br />
&nbsp;<wbr>png_non_exported_function(png_ptr, png_info, foo)<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>body;<br />
&nbsp;<wbr>} </p>
<p> The prototypes for non-exported functions (except for those in pngtest) appear in pngpriv.h above the comment that says </p>
<p>&nbsp;<wbr>&nbsp;<wbr>/*&nbsp;<wbr>Maintainer: Put new private prototypes here&nbsp;<wbr>^&nbsp;<wbr>and in libpngpf.3&nbsp;<wbr>*/ </p>
<p> To avoid polluting the global namespace, the names of all exported functions and variables begin with &quot;png_&quot;, and all publicly visible C preprocessor macros begin with &quot;PNG&quot;. We request that applications that use libpng *not* begin any of their own symbols with either of these strings. </p>
<p> We put a space after each comma and after each semicolon in &quot;for&quot; statements, and we put spaces before and after each C binary operator and after &quot;for&quot; or &quot;while&quot;, and before &quot;?&quot;. We don&#8217;t put a space between a typecast and the expression being cast, nor do we put one between a function name and the left parenthesis that follows it: </p>
<p>&nbsp;<wbr>for&nbsp;<wbr>(i&nbsp;<wbr>=&nbsp;<wbr>2;&nbsp;<wbr>i&nbsp;<wbr>&gt;&nbsp;<wbr>0;&nbsp;<wbr>&#8211;i)<br />
&nbsp;<wbr>y[i]&nbsp;<wbr>=&nbsp;<wbr>a(x)&nbsp;<wbr>+&nbsp;<wbr>(int)b; </p>
<p> We prefer #ifdef and #ifndef to #if defined() and if !defined() when there is only one macro being tested. </p>
<p> We prefer to express integers that are used as bit masks in hex format, with an even number of lower-case hex digits (e.g., 0x00, 0xff, 0x0100). </p>
<p> We do not use the TAB character for indentation in the C sources. </p>
<p> Lines do not exceed 80 characters. </p>
<p> Other rules can be inferred by inspecting the libpng source. </p>
<h2>XIV. Y2K Compliance in libpng</h2>
<p> September 27, 2012 </p>
<p> Since the PNG Development group is an ad-hoc body, we can&#8217;t make an official declaration. </p>
<p> This is your unofficial assurance that libpng from version 0.71 and upward through 1.5.13 are Y2K compliant. It is my belief that earlier versions were also Y2K compliant. </p>
<p> Libpng only has two year fields. One is a 2-byte unsigned integer that will hold years up to 65535. The other holds the date in text format, and will hold years up to 9999. </p>
<p> The integer is<br />
&nbsp;<wbr>&quot;png_uint_16 year&quot;&nbsp;<wbr>in png_time_struct. </p>
<p> The string is<br />
&nbsp;<wbr>&quot;char time_buffer[29]&quot;&nbsp;<wbr>in png_struct.&nbsp;<wbr>&nbsp;<wbr>This will no longer be used in libpng-1.6.x and will be removed from libpng-1.7.0. </p>
<p> There are seven time-related functions: </p>
<p>&nbsp;<wbr>png_convert_to_rfc_1123()&nbsp;<wbr>in png.c<br />
(formerly png_convert_to_rfc_1152()&nbsp;<wbr>in error)<br />
&nbsp;<wbr>png_convert_from_struct_tm()&nbsp;<wbr>in pngwrite.c, called<br />
in pngwrite.c<br />
&nbsp;<wbr>png_convert_from_time_t()&nbsp;<wbr>in pngwrite.c<br />
&nbsp;<wbr>png_get_tIME()&nbsp;<wbr>in pngget.c<br />
&nbsp;<wbr>png_handle_tIME()&nbsp;<wbr>in pngrutil.c, called in pngread.c<br />
&nbsp;<wbr>png_set_tIME()&nbsp;<wbr>in pngset.c<br />
&nbsp;<wbr>png_write_tIME()&nbsp;<wbr>in pngwutil.c, called in pngwrite.c </p>
<p> All appear to handle dates properly in a Y2K environment. The png_convert_from_time_t() function calls gmtime() to convert from system clock time, which returns (year &#8211; 1900), which we properly convert to the full 4-digit year. There is a possibility that applications using libpng are not passing 4-digit years into the png_convert_to_rfc_1123() function, or that they are incorrectly passing only a 2-digit year instead of &quot;year &#8211; 1900&quot; into the png_convert_from_struct_tm() function, but this is not under our control. The libpng documentation has always stated that it works with 4-digit years, and the APIs have been documented as such. </p>
<p> The tIME chunk itself is also Y2K compliant. It uses a 2-byte unsigned integer to hold the year, and can hold years as large as 65535. </p>
<p> zlib, upon which libpng depends, is also Y2K compliant. It contains no date-related code. </p>
<p>Glenn Randers-Pehrson<br />
libpng maintainer<br />
PNG Development Group </p>
<h2>NOTE</h2>
<p> Note about libpng version numbers: </p>
<p> Due to various miscommunications, unforeseen code incompatibilities and occasional factors outside the authors&#8217; control, version numbering on the library has not always been consistent and straightforward. The following table summarizes matters since version 0.89c, which was the first widely used release: </p>
<p>&nbsp;<wbr>source&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>png.h&nbsp;<wbr>&nbsp;<wbr>png.h&nbsp;<wbr>&nbsp;<wbr>shared-lib<br />
&nbsp;<wbr>version&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>string&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int&nbsp;<wbr>&nbsp;<wbr>version<br />
&nbsp;<wbr>&#8212;&#8212;-&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8212;&#8212;&nbsp;<wbr>&nbsp;<wbr>&#8212;&#8211; &#8212;&#8212;&#8212;-<br />
&nbsp;<wbr>0.89c&nbsp;<wbr>(&quot;beta 3&quot;)&nbsp;<wbr>&nbsp;<wbr>0.89&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>89&nbsp;<wbr>&nbsp;<wbr>1.0.89<br />
&nbsp;<wbr>0.90&nbsp;<wbr>&nbsp;<wbr>(&quot;beta 4&quot;)&nbsp;<wbr>&nbsp;<wbr>0.90&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>90&nbsp;<wbr>&nbsp;<wbr>0.90<br />
&nbsp;<wbr>0.95&nbsp;<wbr>&nbsp;<wbr>(&quot;beta 5&quot;)&nbsp;<wbr>&nbsp;<wbr>0.95&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>95&nbsp;<wbr>&nbsp;<wbr>0.95<br />
&nbsp;<wbr>0.96&nbsp;<wbr>&nbsp;<wbr>(&quot;beta 6&quot;)&nbsp;<wbr>&nbsp;<wbr>0.96&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>96&nbsp;<wbr>&nbsp;<wbr>0.96<br />
&nbsp;<wbr>0.97b&nbsp;<wbr>(&quot;beta 7&quot;)&nbsp;<wbr>&nbsp;<wbr>1.00.97&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>97&nbsp;<wbr>&nbsp;<wbr>1.0.1<br />
&nbsp;<wbr>0.97c&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.97&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>97&nbsp;<wbr>&nbsp;<wbr>2.0.97<br />
&nbsp;<wbr>0.98&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.98&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>98&nbsp;<wbr>&nbsp;<wbr>2.0.98<br />
&nbsp;<wbr>0.99&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.99&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>98&nbsp;<wbr>&nbsp;<wbr>2.0.99<br />
&nbsp;<wbr>0.99a-m&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.99&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>99&nbsp;<wbr>&nbsp;<wbr>2.0.99<br />
&nbsp;<wbr>1.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>100&nbsp;<wbr>&nbsp;<wbr>2.1.0<br />
&nbsp;<wbr>1.0.0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1.0.0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>100&nbsp;<wbr>&nbsp;<wbr>2.1.0<br />
&nbsp;<wbr>1.0.0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(from here on, the&nbsp;<wbr>&nbsp;<wbr>100&nbsp;<wbr>&nbsp;<wbr>2.1.0<br />
&nbsp;<wbr>1.0.1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>png.h string is&nbsp;<wbr>&nbsp;<wbr>10001&nbsp;<wbr>&nbsp;<wbr>2.1.0<br />
&nbsp;<wbr>1.0.1a-e identical to the 10002&nbsp;<wbr>&nbsp;<wbr>from here on, the<br />
&nbsp;<wbr>1.0.2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>source version)&nbsp;<wbr>&nbsp;<wbr>10002&nbsp;<wbr>&nbsp;<wbr>shared library is 2.V<br />
&nbsp;<wbr>1.0.2a-b&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10003&nbsp;<wbr>&nbsp;<wbr>where V is the source<br />
&nbsp;<wbr>1.0.1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10001&nbsp;<wbr>&nbsp;<wbr>code version except as<br />
&nbsp;<wbr>1.0.1a-e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10002&nbsp;<wbr>&nbsp;<wbr>2.1.0.1a-e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>noted.<br />
&nbsp;<wbr>1.0.2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10002&nbsp;<wbr>&nbsp;<wbr>2.1.0.2<br />
&nbsp;<wbr>1.0.2a-b&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10003&nbsp;<wbr>&nbsp;<wbr>2.1.0.2a-b<br />
&nbsp;<wbr>1.0.3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10003&nbsp;<wbr>&nbsp;<wbr>2.1.0.3<br />
&nbsp;<wbr>1.0.3a-d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10004&nbsp;<wbr>&nbsp;<wbr>2.1.0.3a-d<br />
&nbsp;<wbr>1.0.4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10004&nbsp;<wbr>&nbsp;<wbr>2.1.0.4<br />
&nbsp;<wbr>1.0.4a-f&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10005&nbsp;<wbr>&nbsp;<wbr>2.1.0.4a-f<br />
&nbsp;<wbr>1.0.5&nbsp;<wbr>(+&nbsp;<wbr>2 patches)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10005&nbsp;<wbr>&nbsp;<wbr>2.1.0.5<br />
&nbsp;<wbr>1.0.5a-d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10006&nbsp;<wbr>&nbsp;<wbr>2.1.0.5a-d<br />
&nbsp;<wbr>1.0.5e-r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10100&nbsp;<wbr>&nbsp;<wbr>2.1.0.5e-r<br />
&nbsp;<wbr>1.0.5s-v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10006&nbsp;<wbr>&nbsp;<wbr>2.1.0.5s-v<br />
&nbsp;<wbr>1.0.6&nbsp;<wbr>(+&nbsp;<wbr>3 patches)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10006&nbsp;<wbr>&nbsp;<wbr>2.1.0.6<br />
&nbsp;<wbr>1.0.6d-g&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10007&nbsp;<wbr>&nbsp;<wbr>2.1.0.6d-g<br />
&nbsp;<wbr>1.0.6h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10007&nbsp;<wbr>&nbsp;<wbr>10.6h<br />
&nbsp;<wbr>1.0.6i&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10007&nbsp;<wbr>&nbsp;<wbr>10.6i<br />
&nbsp;<wbr>1.0.6j&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10007&nbsp;<wbr>&nbsp;<wbr>2.1.0.6j<br />
&nbsp;<wbr>1.0.7beta11-14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>DLLNUM&nbsp;<wbr>&nbsp;<wbr>10007&nbsp;<wbr>&nbsp;<wbr>2.1.0.7beta11-14<br />
&nbsp;<wbr>1.0.7beta15-18&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10007&nbsp;<wbr>&nbsp;<wbr>2.1.0.7beta15-18<br />
&nbsp;<wbr>1.0.7rc1-2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10007&nbsp;<wbr>&nbsp;<wbr>2.1.0.7rc1-2<br />
&nbsp;<wbr>1.0.7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10007&nbsp;<wbr>&nbsp;<wbr>2.1.0.7<br />
&nbsp;<wbr>1.0.8beta1-4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10008&nbsp;<wbr>&nbsp;<wbr>2.1.0.8beta1-4<br />
&nbsp;<wbr>1.0.8rc1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10008&nbsp;<wbr>&nbsp;<wbr>2.1.0.8rc1<br />
&nbsp;<wbr>1.0.8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10008&nbsp;<wbr>&nbsp;<wbr>2.1.0.8<br />
&nbsp;<wbr>1.0.9beta1-6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10009&nbsp;<wbr>&nbsp;<wbr>2.1.0.9beta1-6<br />
&nbsp;<wbr>1.0.9rc1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10009&nbsp;<wbr>&nbsp;<wbr>2.1.0.9rc1<br />
&nbsp;<wbr>1.0.9beta7-10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10009&nbsp;<wbr>&nbsp;<wbr>2.1.0.9beta7-10<br />
&nbsp;<wbr>1.0.9rc2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10009&nbsp;<wbr>&nbsp;<wbr>2.1.0.9rc2<br />
&nbsp;<wbr>1.0.9&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10009&nbsp;<wbr>&nbsp;<wbr>2.1.0.9<br />
&nbsp;<wbr>1.0.10beta1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10010&nbsp;<wbr>&nbsp;<wbr>2.1.0.10beta1<br />
&nbsp;<wbr>1.0.10rc1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10010&nbsp;<wbr>&nbsp;<wbr>2.1.0.10rc1<br />
&nbsp;<wbr>1.0.10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10010&nbsp;<wbr>&nbsp;<wbr>2.1.0.10<br />
&nbsp;<wbr>1.0.11beta1-3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10011&nbsp;<wbr>&nbsp;<wbr>2.1.0.11beta1-3<br />
&nbsp;<wbr>1.0.11rc1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10011&nbsp;<wbr>&nbsp;<wbr>2.1.0.11rc1<br />
&nbsp;<wbr>1.0.11&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10011&nbsp;<wbr>&nbsp;<wbr>2.1.0.11<br />
&nbsp;<wbr>1.0.12beta1-2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10012&nbsp;<wbr>&nbsp;<wbr>2.1.0.12beta1-2<br />
&nbsp;<wbr>1.0.12rc1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10012&nbsp;<wbr>&nbsp;<wbr>2.1.0.12rc1<br />
&nbsp;<wbr>1.0.12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10012&nbsp;<wbr>&nbsp;<wbr>2.1.0.12<br />
&nbsp;<wbr>1.1.0a-f&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10100&nbsp;<wbr>&nbsp;<wbr>2.1.1.0a-f abandoned<br />
&nbsp;<wbr>1.2.0beta1-2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10200&nbsp;<wbr>&nbsp;<wbr>2.1.2.0beta1-2<br />
&nbsp;<wbr>1.2.0beta3-5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10200&nbsp;<wbr>&nbsp;<wbr>3.1.2.0beta3-5<br />
&nbsp;<wbr>1.2.0rc1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10200&nbsp;<wbr>&nbsp;<wbr>3.1.2.0rc1<br />
&nbsp;<wbr>1.2.0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10200&nbsp;<wbr>&nbsp;<wbr>3.1.2.0<br />
&nbsp;<wbr>1.2.1beta-4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10201&nbsp;<wbr>&nbsp;<wbr>3.1.2.1beta1-4<br />
&nbsp;<wbr>1.2.1rc1-2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10201&nbsp;<wbr>&nbsp;<wbr>3.1.2.1rc1-2<br />
&nbsp;<wbr>1.2.1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10201&nbsp;<wbr>&nbsp;<wbr>3.1.2.1<br />
&nbsp;<wbr>1.2.2beta1-6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10202&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.2.2beta1-6<br />
&nbsp;<wbr>1.0.13beta1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10013&nbsp;<wbr>&nbsp;<wbr>10.so.0.1.0.13beta1<br />
&nbsp;<wbr>1.0.13rc1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10013&nbsp;<wbr>&nbsp;<wbr>10.so.0.1.0.13rc1<br />
&nbsp;<wbr>1.2.2rc1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10202&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.2.2rc1<br />
&nbsp;<wbr>1.0.13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10013&nbsp;<wbr>&nbsp;<wbr>10.so.0.1.0.13<br />
&nbsp;<wbr>1.2.2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10202&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.2.2<br />
&nbsp;<wbr>1.2.3rc1-6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10203&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.2.3rc1-6<br />
&nbsp;<wbr>1.2.3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10203&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.2.3<br />
&nbsp;<wbr>1.2.4beta1-3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10204&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.2.4beta1-3<br />
&nbsp;<wbr>1.2.4rc1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10204&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.2.4rc1<br />
&nbsp;<wbr>1.0.14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10014&nbsp;<wbr>&nbsp;<wbr>10.so.0.1.0.14<br />
&nbsp;<wbr>1.2.4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10204&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.2.4<br />
&nbsp;<wbr>1.2.5beta1-2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10205&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.2.5beta1-2<br />
&nbsp;<wbr>1.0.15rc1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10015&nbsp;<wbr>&nbsp;<wbr>10.so.0.1.0.15rc1<br />
&nbsp;<wbr>1.0.15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10015&nbsp;<wbr>&nbsp;<wbr>10.so.0.1.0.15<br />
&nbsp;<wbr>1.2.5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10205&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.2.5<br />
&nbsp;<wbr>1.2.6beta1-4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10206&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.2.6beta1-4<br />
&nbsp;<wbr>1.2.6rc1-5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10206&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.2.6rc1-5<br />
&nbsp;<wbr>1.0.16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10016&nbsp;<wbr>&nbsp;<wbr>10.so.0.1.0.16<br />
&nbsp;<wbr>1.2.6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10206&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.2.6<br />
&nbsp;<wbr>1.2.7beta1-2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10207&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.2.7beta1-2<br />
&nbsp;<wbr>1.0.17rc1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10017&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.0.17rc1<br />
&nbsp;<wbr>1.2.7rc1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10207&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.2.7rc1<br />
&nbsp;<wbr>1.0.17&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10017&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.0.17<br />
&nbsp;<wbr>1.2.7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10207&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.2.7<br />
&nbsp;<wbr>1.2.8beta1-5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10208&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.2.8beta1-5<br />
&nbsp;<wbr>1.0.18rc1-5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10018&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.0.18rc1-5<br />
&nbsp;<wbr>1.2.8rc1-5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10208&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.2.8rc1-5<br />
&nbsp;<wbr>1.0.18&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10018&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.0.18<br />
&nbsp;<wbr>1.2.8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10208&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.2.8<br />
&nbsp;<wbr>1.2.9beta1-3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10209&nbsp;<wbr>&nbsp;<wbr>12.so.0.1.2.9beta1-3<br />
&nbsp;<wbr>1.2.9beta4-11&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10209&nbsp;<wbr>&nbsp;<wbr>12.so.0.9[.0]<br />
&nbsp;<wbr>1.2.9rc1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10209&nbsp;<wbr>&nbsp;<wbr>12.so.0.9[.0]<br />
&nbsp;<wbr>1.2.9&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10209&nbsp;<wbr>&nbsp;<wbr>12.so.0.9[.0]<br />
&nbsp;<wbr>1.2.10beta1-7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10210&nbsp;<wbr>&nbsp;<wbr>12.so.0.10[.0]<br />
&nbsp;<wbr>1.2.10rc1-2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10210&nbsp;<wbr>&nbsp;<wbr>12.so.0.10[.0]<br />
&nbsp;<wbr>1.2.10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10210&nbsp;<wbr>&nbsp;<wbr>12.so.0.10[.0]<br />
&nbsp;<wbr>1.4.0beta1-6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10400&nbsp;<wbr>&nbsp;<wbr>14.so.0.0[.0]<br />
&nbsp;<wbr>1.2.11beta1-4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10210&nbsp;<wbr>&nbsp;<wbr>12.so.0.11[.0]<br />
&nbsp;<wbr>1.4.0beta7-8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10400&nbsp;<wbr>&nbsp;<wbr>14.so.0.0[.0]<br />
&nbsp;<wbr>1.2.11&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10211&nbsp;<wbr>&nbsp;<wbr>12.so.0.11[.0]<br />
&nbsp;<wbr>1.2.12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10212&nbsp;<wbr>&nbsp;<wbr>12.so.0.12[.0]<br />
&nbsp;<wbr>1.4.0beta9-14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10400&nbsp;<wbr>&nbsp;<wbr>14.so.0.0[.0]<br />
&nbsp;<wbr>1.2.13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10213&nbsp;<wbr>&nbsp;<wbr>12.so.0.13[.0]<br />
&nbsp;<wbr>1.4.0beta15-36&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10400&nbsp;<wbr>&nbsp;<wbr>14.so.0.0[.0]<br />
&nbsp;<wbr>1.4.0beta37-87&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10400&nbsp;<wbr>&nbsp;<wbr>14.so.14.0[.0]<br />
&nbsp;<wbr>1.4.0rc01&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10400&nbsp;<wbr>&nbsp;<wbr>14.so.14.0[.0]<br />
&nbsp;<wbr>1.4.0beta88-109&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10400&nbsp;<wbr>&nbsp;<wbr>14.so.14.0[.0]<br />
&nbsp;<wbr>1.4.0rc02-08&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10400&nbsp;<wbr>&nbsp;<wbr>14.so.14.0[.0]<br />
&nbsp;<wbr>1.4.0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10400&nbsp;<wbr>&nbsp;<wbr>14.so.14.0[.0]<br />
&nbsp;<wbr>1.4.1beta01-03&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10401&nbsp;<wbr>&nbsp;<wbr>14.so.14.1[.0]<br />
&nbsp;<wbr>1.4.1rc01&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10401&nbsp;<wbr>&nbsp;<wbr>14.so.14.1[.0]<br />
&nbsp;<wbr>1.4.1beta04-12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10401&nbsp;<wbr>&nbsp;<wbr>14.so.14.1[.0]<br />
&nbsp;<wbr>1.4.1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10401&nbsp;<wbr>&nbsp;<wbr>14.so.14.1[.0]<br />
&nbsp;<wbr>1.4.2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10402&nbsp;<wbr>&nbsp;<wbr>14.so.14.2[.0]<br />
&nbsp;<wbr>1.4.3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10403&nbsp;<wbr>&nbsp;<wbr>14.so.14.3[.0]<br />
&nbsp;<wbr>1.4.4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10404&nbsp;<wbr>&nbsp;<wbr>14.so.14.4[.0]<br />
&nbsp;<wbr>1.5.0beta01-58&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10500&nbsp;<wbr>&nbsp;<wbr>15.so.15.0[.0]<br />
&nbsp;<wbr>1.5.0rc01-07&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10500&nbsp;<wbr>&nbsp;<wbr>15.so.15.0[.0]<br />
&nbsp;<wbr>1.5.0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10500&nbsp;<wbr>&nbsp;<wbr>15.so.15.0[.0]<br />
&nbsp;<wbr>1.5.1beta01-11&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10501&nbsp;<wbr>&nbsp;<wbr>15.so.15.1[.0]<br />
&nbsp;<wbr>1.5.1rc01-02&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10501&nbsp;<wbr>&nbsp;<wbr>15.so.15.1[.0]<br />
&nbsp;<wbr>1.5.1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10501&nbsp;<wbr>&nbsp;<wbr>15.so.15.1[.0]<br />
&nbsp;<wbr>1.5.2beta01-03&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10502&nbsp;<wbr>&nbsp;<wbr>15.so.15.2[.0]<br />
&nbsp;<wbr>1.5.2rc01-03&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10502&nbsp;<wbr>&nbsp;<wbr>15.so.15.2[.0]<br />
&nbsp;<wbr>1.5.2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10502&nbsp;<wbr>&nbsp;<wbr>15.so.15.2[.0]<br />
&nbsp;<wbr>1.5.3beta01-10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10503&nbsp;<wbr>&nbsp;<wbr>15.so.15.3[.0]<br />
&nbsp;<wbr>1.5.3rc01-02&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10503&nbsp;<wbr>&nbsp;<wbr>15.so.15.3[.0]<br />
&nbsp;<wbr>1.5.3beta11&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10503&nbsp;<wbr>&nbsp;<wbr>15.so.15.3[.0]<br />
&nbsp;<wbr>1.5.3&nbsp;<wbr>[omitted]<br />
&nbsp;<wbr>1.5.4beta01-08&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10504&nbsp;<wbr>&nbsp;<wbr>15.so.15.4[.0]<br />
&nbsp;<wbr>1.5.4rc01&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10504&nbsp;<wbr>&nbsp;<wbr>15.so.15.4[.0]<br />
&nbsp;<wbr>1.5.4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10504&nbsp;<wbr>&nbsp;<wbr>15.so.15.4[.0]<br />
&nbsp;<wbr>1.5.5beta01-08&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10505&nbsp;<wbr>&nbsp;<wbr>15.so.15.5[.0]<br />
&nbsp;<wbr>1.5.5rc01&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10505&nbsp;<wbr>&nbsp;<wbr>15.so.15.5[.0]<br />
&nbsp;<wbr>1.5.5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10505&nbsp;<wbr>&nbsp;<wbr>15.so.15.5[.0]<br />
&nbsp;<wbr>1.5.6beta01-07&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10506&nbsp;<wbr>&nbsp;<wbr>15.so.15.6[.0]<br />
&nbsp;<wbr>1.5.6rc01-03&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10506&nbsp;<wbr>&nbsp;<wbr>15.so.15.6[.0]<br />
&nbsp;<wbr>1.5.6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10506&nbsp;<wbr>&nbsp;<wbr>15.so.15.6[.0]<br />
&nbsp;<wbr>1.5.7beta01-05&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10507&nbsp;<wbr>&nbsp;<wbr>15.so.15.7[.0]<br />
&nbsp;<wbr>1.5.7rc01-03&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10507&nbsp;<wbr>&nbsp;<wbr>15.so.15.7[.0]<br />
&nbsp;<wbr>1.5.7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10507&nbsp;<wbr>&nbsp;<wbr>15.so.15.7[.0]<br />
&nbsp;<wbr>1.5.8beta01&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10508&nbsp;<wbr>&nbsp;<wbr>15.so.15.8[.0]<br />
&nbsp;<wbr>1.5.8rc01&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10508&nbsp;<wbr>&nbsp;<wbr>15.so.15.8[.0]<br />
&nbsp;<wbr>1.5.8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10508&nbsp;<wbr>&nbsp;<wbr>15.so.15.8[.0]<br />
&nbsp;<wbr>1.5.9beta01-02&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10509&nbsp;<wbr>&nbsp;<wbr>15.so.15.9[.0]<br />
&nbsp;<wbr>1.5.9rc01&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10509&nbsp;<wbr>&nbsp;<wbr>15.so.15.9[.0]<br />
&nbsp;<wbr>1.5.9&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10509&nbsp;<wbr>&nbsp;<wbr>15.so.15.9[.0]<br />
&nbsp;<wbr>1.5.10beta01-05&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10510&nbsp;<wbr>&nbsp;<wbr>15.so.15.10[.0]<br />
&nbsp;<wbr>1.5.10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10510&nbsp;<wbr>&nbsp;<wbr>15.so.15.10[.0]<br />
&nbsp;<wbr>1.5.11beta01&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10511&nbsp;<wbr>&nbsp;<wbr>15.so.15.11[.0]<br />
&nbsp;<wbr>1.5.11rc01-05&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10511&nbsp;<wbr>&nbsp;<wbr>15.so.15.11[.0]<br />
&nbsp;<wbr>1.5.11&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10511&nbsp;<wbr>&nbsp;<wbr>15.so.15.11[.0]<br />
&nbsp;<wbr>1.5.12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10512&nbsp;<wbr>&nbsp;<wbr>15.so.15.12[.0]<br />
&nbsp;<wbr>1.5.13beta01-02&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10513&nbsp;<wbr>&nbsp;<wbr>15.so.15.13[.0]<br />
&nbsp;<wbr>1.5.13rc01&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10513&nbsp;<wbr>&nbsp;<wbr>15.so.15.13[.0]<br />
&nbsp;<wbr>1.5.13&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10513&nbsp;<wbr>&nbsp;<wbr>15.so.15.13[.0] </p>
<p> Henceforth the source version will match the shared-library minor and patch numbers; the shared-library major version number will be used for changes in backward compatibility, as it is intended. The PNG_PNGLIB_VER macro, which is not used within libpng but is available for applications, is an unsigned integer of the form xyyzz corresponding to the source version x.y.z (leading zeros in y and z). Beta versions were given the previous public release number plus a letter, until version 1.0.6j; from then on they were given the upcoming public release number plus &quot;betaNN&quot; or &quot;rcN&quot;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-png/">png</a>(5),</code> <a href="/docs/linux/man/3-libpngpf/">libpngpf</a>(3),<code> <a href="/docs/linux/man/3-zlib/">zlib</a>(3),</code> <a href="/docs/linux/man/5-deflate/">deflate</a>(5),and<code> <a href="/docs/linux/man/5-zlib/">zlib</a>(5)</code> </p>
<p> <i>libpng</i>:</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://libpng.sourceforge.net">http://libpng.sourceforge.net</a> (follow the [DOWNLOAD] link) <a rel="nofollow" href="http://www.libpng.org/pub/png">http://www.libpng.org/pub/png</a> </p>
</dl>
<p> <i>zlib</i>:</p>
<dl>
<dt>
<dd> (generally) at the same location as <i>libpng</i> or at<br />
 <a href="ftp://ftp.info-zip.org/pub/infozip/zlib">ftp://ftp.info-zip.org/pub/infozip/zlib</a> </p>
</dl>
<p> <i>PNG</i>specification:<i>RFC</i>2083</p>
<dl>
<dt>
<dd> (generally) at the same location as <i>libpng</i> or at<br />
 <a href="ftp://ds.internic.net/rfc/rfc2083.txt">ftp://ds.internic.net/rfc/rfc2083.txt</a><br />
 or (as a W3C Recommendation) at<br />
 <a rel="nofollow" href="http://www.w3.org/TR/REC-png.html">http://www.w3.org/TR/REC-png.html</a> </p>
</dl>
<p> In the case of any inconsistency between the PNG specification and this library, the specification takes precedence. </p>
<h2>AUTHORS</h2>
<p> This man page: Glenn Randers-Pehrson &lt;glennrp at users.sourceforge.net&gt; </p>
<p> The contributing authors would like to thank all those who helped with testing, bug fixes, and patience. This wouldn&#8217;t have been possible without all of you. </p>
<p> Thanks to Frank J. T. Wojcik for helping with the documentation. </p>
<p> Libpng version 1.5.13 &#8211; September 27, 2012: Initially created in 1995 by Guy Eric Schalnat, then of Group 42, Inc. Currently maintained by Glenn Randers-Pehrson (glennrp at users.sourceforge.net). </p>
<p> Supported by the PNG development group<br />
 png-mng-implement at lists.sf.net (subscription required; visit png-mng-implement at lists.sourceforge.net (subscription required; visit <a rel="nofollow" href="https://lists.sourceforge.net/lists/listinfo/png-mng-implement">https://lists.sourceforge.net/lists/listinfo/png-mng-implement</a> to subscribe). </p>
<h2>COPYRIGHT NOTICE, DISCLAIMER, and LICENSE:</h2>
<p> (This copy of the libpng notices is provided for your convenience. In case of any discrepancy between this copy and the notices in the file png.h that is included in the libpng distribution, the latter shall prevail.) </p>
<p> If you modify libpng you may insert additional notices immediately following this sentence. </p>
<p> This code is released under the libpng license. </p>
<p> libpng versions 1.2.6, August 15, 2004, through 1.5.13, September 27, 2012, are Copyright (c) 2004,2006-2007 Glenn Randers-Pehrson, and are distributed according to the same disclaimer and license as libpng-1.2.5 with the following individual added to the list of Contributing Authors </p>
<p>Cosmin Truta </p>
<p> libpng versions 1.0.7, July 1, 2000, through 1.2.5 &#8211; October 3, 2002, are Copyright (c) 2000-2002 Glenn Randers-Pehrson, and are distributed according to the same disclaimer and license as libpng-1.0.6 with the following individuals added to the list of Contributing Authors </p>
<p>Simon-Pierre Cadieux<br />
Eric S. Raymond<br />
Gilles Vollant </p>
<p> and with the following additions to the disclaimer: </p>
<p>There is no warranty against interference with your<br />
enjoyment of the library or against infringement.<br />
There is no warranty that our efforts or the library<br />
will fulfill any of your particular purposes or needs.<br />
This library is provided with all faults, and the entire<br />
risk of satisfactory quality, performance, accuracy, and<br />
effort is with the user. </p>
<p> libpng versions 0.97, January 1998, through 1.0.6, March 20, 2000, are Copyright (c) 1998, 1999 Glenn Randers-Pehrson Distributed according to the same disclaimer and license as libpng-0.96, with the following individuals added to the list of Contributing Authors: </p>
<p>Tom Lane<br />
Glenn Randers-Pehrson<br />
Willem van Schaik </p>
<p> libpng versions 0.89, June 1996, through 0.96, May 1997, are Copyright (c) 1996, 1997 Andreas Dilger Distributed according to the same disclaimer and license as libpng-0.88, with the following individuals added to the list of Contributing Authors: </p>
<p>John Bowler<br />
Kevin Bracey<br />
Sam Bushell<br />
Magnus Holmgren<br />
Greg Roelofs<br />
Tom Tanner </p>
<p> libpng versions 0.5, May 1995, through 0.88, January 1996, are Copyright (c) 1995, 1996 Guy Eric Schalnat, Group 42, Inc. </p>
<p> For the purposes of this copyright and license, &quot;Contributing Authors&quot; is defined as the following set of individuals: </p>
<p>Andreas Dilger<br />
Dave Martindale<br />
Guy Eric Schalnat<br />
Paul Schmidt<br />
Tim Wegner </p>
<p> The PNG Reference Library is supplied &quot;AS IS&quot;. The Contributing Authors and Group 42, Inc. disclaim all warranties, expressed or implied, including, without limitation, the warranties of merchantability and of fitness for any purpose. The Contributing Authors and Group 42, Inc. assume no liability for direct, indirect, incidental, special, exemplary, or consequential damages, which may result from the use of the PNG Reference Library, even if advised of the possibility of such damage. </p>
<p> Permission is hereby granted to use, copy, modify, and distribute this source code, or portions hereof, for any purpose, without fee, subject to the following restrictions: </p>
<p> 1. The origin of this source code must not be misrepresented. </p>
<p> 2. Altered versions must be plainly marked as such and<br />
must not be misrepresented as being the original source. </p>
<p> 3. This Copyright notice may not be removed or altered from<br />
any source or altered source distribution. </p>
<p> The Contributing Authors and Group 42, Inc. specifically permit, without fee, and encourage the use of this source code as a component to supporting the PNG file format in commercial products. If you use this source code in a product, acknowledgment is not required but would be appreciated. </p>
<p> A &quot;png_get_copyright&quot; function is available, for convenient use in &quot;about&quot; boxes and the like: </p>
<p>printf(&quot;%s&quot;,png_get_copyright(NULL)); </p>
<p> Also, the PNG logo (in PNG format, of course) is supplied in the files &quot;pngbar.png&quot; and &quot;pngbar.jpg (88&#215;31) and &quot;pngnow.png&quot; (98&#215;31). </p>
<p> Libpng is OSI Certified Open Source Software. OSI Certified Open Source is a certification mark of the Open Source Initiative. </p>
<p> Glenn Randers-Pehrson glennrp at users.sourceforge.net September 27, 2012 </p>
<h2>Index</h2>
