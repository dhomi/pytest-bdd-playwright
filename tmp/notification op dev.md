Deze curl gaat bijv naar de dev omgeving, de test omgeving heb ik geen toegang toe maar wellicht darshan wel, maar voor nu is dev misschien goed genoeg?

``` 
curl --location 'https://api-dev.cdn.cldsvc.net/system/v1/notifications/esp' \
--header 'Content-Type: application/xml' \
--header 'apikey: 545d1a46-2ed4-4593-b1c3-eecdb90c443d' \
--data '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v1="http://schemas.postnl.nl/parcels/customerInteraction/notifications/emailBasicSubscriptionService/v1.0/" xmlns:com="http://schemas.postnl.nl/parcels/customerInteraction/notifications/common/">
<soapenv:Header/>
<soapenv:Body>
<v1:CreateRequest>
<v1:KlantNr>13371340</v1:KlantNr>
</v1:CreateRequest>
</soapenv:Body>
</soapenv:Envelope>
'

``` 
Deze call maakt voor het Business Portal scenario een 'standaard' klant aan. 
De volgende call verwijderd die klant dan weer;

```

curl --location 'https://api-dev.cdn.cldsvc.net/system/v1/notifications/esp' \
--header 'Content-Type: application/xml' \
--header 'apikey: 545d1a46-2ed4-4593-b1c3-eecdb90c443d' \
--data '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v1="http://schemas.postnl.nl/parcels/customerInteraction/notifications/emailBasicSubscriptionService/v1.0/" xmlns:com="http://schemas.postnl.nl/parcels/customerInteraction/notifications/common/">
<soapenv:Header/>
<soapenv:Body>
<v1:DeleteRequest>
<v1:KlantNr>13371340</v1:KlantNr>
</v1:DeleteRequest>
</soapenv:Body>
</soapenv:Envelope>
'

```