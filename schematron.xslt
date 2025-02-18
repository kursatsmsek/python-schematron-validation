<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

    <xsl:output method="xml" indent="yes" />

    <xsl:template match="/doc">
        <root>
            <xsl:for-each select="item">
                <xsl:variable name="itemText" select="."/>

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
