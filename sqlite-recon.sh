#!/bin/bash
DB='encrypted.db'
while IFS= read -r line
do
  echo "$line"
  sqlcipher $DB    'PRAGMA key='$line';
                    select * from flag;'
done < rockyou.txt
