#!/usr/local/bin/nu

if ('TODO.item' | path exists) {
   let $r = (ls TODO.item | where modified > (date now) - 10min | length)
      if ($r == 0) {
         touch -m 'TODO.item'
         cat TODO.item
      } else {
         error make {msg:"exit code != 0"}
      }
}