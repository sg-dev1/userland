{
    'includes': {
      '../../config.gypi',
    },
    'targets': [
      {
        'target_name': 'containers_static',
        'type': 'static_library',
        'dependencies': [
          '<(DEPTH)/userland/interface/vcos/pthreads/vcos_pthreads.gyp:vcos_pthreads_static',
          #'xyzzy',
          #'../bar/bar.gyp:bar',
          # TODO do cyclic dependencies work in gyp?
          #'<(DEPTH)/userland/containers/mp4/mp4.gyp:mp4_reader_static',
          #'<(DEPTH)/userland/containers/mp4/mp4.gyp:mp4_writer_static',
          #'<(DEPTH)/userland/containers/mpeg/mpeg.gyp:ps_reader_static',
          #'<(DEPTH)/userland/containers/mpga/mpga.gyp:mpga_reader_static',
          #'<(DEPTH)/userland/containers/binary/binary.gyp:binary_reader_static',
          #'<(DEPTH)/userland/containers/binary/binary.gyp:binary_writer_static',
          #'<(DEPTH)/userland/containers/mkv/mkv.gyp:mkv_reader_static',
          #'<(DEPTH)/userland/containers/wav/wav.gyp:wav_reader_static',
          #'<(DEPTH)/userland/containers/asf/asf.gyp:asf_reader_static',
          #'<(DEPTH)/userland/containers/asf/asf.gyp:asf_writer_static',
          #'<(DEPTH)/userland/containers/flash/flash.gyp:flash_reader_static',
          #'<(DEPTH)/userland/containers/avi/avi.gyp:avi_reader_static',
          #'<(DEPTH)/userland/containers/avi/avi.gyp:avi_writer_static',
          #'<(DEPTH)/userland/containers/rtp/rtp.gyp:rtp_reader_static',
          #'<(DEPTH)/userland/containers/rtsp/rtsp.gyp:rtsp_reader_static',
          #'<(DEPTH)/userland/containers/rcv/rcv.gyp:rcv_reader_static',
          #'<(DEPTH)/userland/containers/rv9/rv9.gyp:rv9_reader_static',
          #'<(DEPTH)/userland/containers/qsynth/qsynth.gyp:qsynth_reader_static',
          #'<(DEPTH)/userland/containers/simple/simple.gyp:simple_reader_static',
          #'<(DEPTH)/userland/containers/simple/simple.gyp:simple_writer_static',
          #'<(DEPTH)/userland/containers/raw/raw.gyp:raw_video_reader_static',
          #'<(DEPTH)/userland/containers/raw/raw.gyp:raw_video_writer_static',
          #'<(DEPTH)/userland/containers/dummy/dummy.gyp:dummy_writer_static',
          #'<(DEPTH)/userland/containers/metadata/id3/id3.gyp:id3_metadata_reader_static',
        ],
        'defines': [
          # TODO find out: same as cmake's add_definitions( -DENABLE_CONTAINER_IO_HTTP )
          'ENABLE_CONTAINER_IO_HTTP',
        #  'DEFINE_FOO',
        #  'DEFINE_A_VALUE=value',
        ],
        'include_dirs': [
          '<(DEPTH)/userland/interface/vcos',
        ],
        'sources': [
          # Containers core library
          'core/containers.c',
          'core/containers_io.c',
          'core/containers_io_helpers.c',
          'core/containers_codecs.c',
          'core/containers_utils.c',
          'core/containers_writer_utils.c',
          'core/containers_loader.c',
          'core/containers_filters.c',
          'core/containers_logging.c',
          'core/containers_uri.c',
          'core/containers_bits.c',
          'core/containers_list.c',
          'core/containers_index.c',
          # Containers io library
          'io/io_file.c',
          'io/io_null.c',
          'io/io_net.c',
          'io/io_pktfile.c',
          'io/io_http.c',
          # Containers net library
          'net/net_sockets_common.c',
          'net/net_sockets_bsd.c',
          # # windows only (just comment out)
          # 'net/net_sockets_win32.c',
          # 'net/net_sockets_null.c',
          # Packetizers library
          'core/packetizers.c',
          'mpga/mpga_packetizer.c',
          'mpgv/mpgv_packetizer.c',
          'pcm/pcm_packetizer.c',
          'h264/avc1_packetizer.c',
        ],
      },
    ],
}
