{
    'includes': {
      '../../../../config.gypi',
    },
    'targets': [
      {
        'target_name': 'mmal_core_static',
        'type': 'static_library',
        'dependencies': [
          '<(DEPTH)/userland/interface/vcos/pthreads/vcos_pthreads.gyp:vcos_pthreads_static',
          #'xyzzy',
          #'../bar/bar.gyp:bar',
        ],
        #'defines': [
        #  'DEFINE_FOO',
        #  'DEFINE_A_VALUE=value',
        #],
        'include_dirs': [
          '..',
        ],
        'sources': [
          'mmal_format.c',
          'mmal_port.c',
          'mmal_port_clock.c',
          'mmal_component.c',
          'mmal_buffer.c',
          'mmal_queue.c',
          'mmal_pool.c',
          'mmal_events.c',
          'mmal_logging.c',
          'mmal_clock.c',
        ],
      },
    ],
}
