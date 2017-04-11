{
    'includes': {
      '../../../../config.gypi',
    },
    'targets': [
      {
        'target_name': 'mmal_components_static',
        'type': 'static_library',
        'dependencies': [
          #'<(DEPTH)/userland/interface/vcos/vcos_pthreads.gyp:vcos_pthreads_static',
          '<(DEPTH)/userland/interface/mmal/core/mmal_core.gyp:mmal_core_static',
          '<(DEPTH)/userland/interface/mmal/util/mmal_util.gyp:mmal_util_static',
          '<(DEPTH)/userland/containers/containers.gyp:containers_static',
          #TODO ${container_libs} ???
        ],
        #'defines': [
        #  'DEFINE_FOO',
        #  'DEFINE_A_VALUE=value',
        #],
        'include_dirs': [
          '..',
        ],
        'sources': [
          'container_reader.c',
          'null_sink.c',
          'passthrough.c',
          'scheduler.c',
          'splitter.c',
          'copy.c',
          'artificial_camera.c',
          'aggregator.c',
          'clock.c',
          'spdif.c',
        ],
      },
    ],
}
