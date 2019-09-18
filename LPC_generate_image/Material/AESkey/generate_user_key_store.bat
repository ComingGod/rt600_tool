blhost -p com10 -- key-provisioning enroll
blhost -p com10 -- key-provisioning set_user_key 11 userkey.bin
blhost -p com10 -- key-provisioning read_key_store key_store_user.bin

pause