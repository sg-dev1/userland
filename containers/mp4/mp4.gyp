{
    'includes': {
      '../../../config.gypi',
    },
    'targets': [
      {
        'target_name': 'mp4_reader_static',
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
          'mp4_reader.c',
        ],
      },
      {
        'target_name': 'mp4_writer_static',
        'type': 'static_library',
        'dependencies': [
          '<(DEPTH)/userland/containers/containers.gyp:containers_static',
        ],
        'include_dirs': [
          '<(DEPTH)/userland',
        ],
        'sources': [
          'mp4_writer.c',
        ],
      },
    ],
}
