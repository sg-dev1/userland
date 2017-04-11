{
    'includes': {
      '../../../config.gypi',
    },
    'targets': [
      {
        'target_name': 'rtp_reader_static',
        'type': 'static_library',
        'dependencies': [
          '<(DEPTH)/userland/containers/containers.gyp:containers_static',
        ],
        #'defines': [
        #  'DEFINE_FOO',
        #  'DEFINE_A_VALUE=value',
        #],
        'include_dirs': [
          '<(DEPTH)/userland',
        ],
        'sources': [
          'rtp_reader.c',
          'rtp_h264.c',
          'rtp_mpeg4.c',
          'rtp_base64.c',
        ],
      },
    ],
}
