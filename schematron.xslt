<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

    <!-- XSLT çıktısını XML formatında yapıyoruz -->
    <xsl:output method="xml" indent="yes" />

    <!-- Temel şablon: kök öğe (doc) üzerinde işlem yap -->
    <xsl:template match="/doc">
        <root>
            <!-- Her <item> öğesini döngüyle işleyip kontrol et -->
            <xsl:for-each select="item">
                <xsl:variable name="itemText" select="."/>

                <!-- Item'ın uzunluğunu kontrol et -->
                <xsl:choose>
                    <xsl:when test="string-length($itemText) &lt; 5">
                        <validationError>
                            <xsl:value-of select="'Item is too short: '"/>
                            <xsl:value-of select="$itemText"/>
                        </validationError>
                    </xsl:when>
                    <xsl:otherwise>
                        <validItem>
                            <xsl:value-of select="$itemText"/>
                        </validItem>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:for-each>
        </root>
    </xsl:template>

</xsl:stylesheet>
