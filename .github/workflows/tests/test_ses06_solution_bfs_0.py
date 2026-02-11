test = {
  'name': 'test_ses06_solution_bfs_0',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ex_graph = create_bfs_graph()
          >>> bfs_dists = bfs(ex_graph, 'John')
          >>> [bfs_dists['Donald'], bfs_dists['Jared']]
          [4, 3]
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ses06 import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
