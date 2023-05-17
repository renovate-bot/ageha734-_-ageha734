#!/usr/local/bin/nu

let mdlist = (ls *.md)
let count = 0

if ($mdlist | length) > 0 {
   let cnt = ($mdlist | get name |
       each { | it | open $it | lines |
            each { | line |
                 if ($line | str contains '- [ ] ') {
                      'found'
                 }
            }
       } | flatten | length
   )
   if $cnt > 0 {
      echo $'💦($cnt)'
   }
}