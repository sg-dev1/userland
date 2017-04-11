{
    'includes': {
      '../../../config.gypi',
    },
    'targets': [
      {
        'target_name': 'avi_reader_static',
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
          'avi_reader.c',
        ],
      },
      {
        'target_name': 'avi_writer_static',
        'type': 'static_library',
        'dependencies': [
          '<(DEPTH)/userland/containers/containers.gyp:containers_static',
        ],
        'include_dirs': [
          '<(DEPTH)/userland',
        ],
        'sources': [
          'avi_writer.c',
        ],
      },
    ],
}
