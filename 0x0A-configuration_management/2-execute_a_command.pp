# kill process killmenow

exec { 'kill_process':
  command     => '/usr/bin/pkill -f "killmenow"',
  refreshonly => true,
  onlyif      => '/usr/bin/pgrep -f "killmenow"',
}
