# kill process killmenow

exec { 'pkillmenow':
  command  => '/usr/bin/kill killmenow',
  provider => 'shell',
  returns  => [0, 1],
}
