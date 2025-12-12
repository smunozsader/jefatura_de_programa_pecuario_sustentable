<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.16" simplifyDrawingHints="1" readOnly="0" simplifyDrawingTol="1" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" simplifyLocal="1" maxScale="0" minScale="100000000" labelsEnabled="1" simplifyMaxScale="1" simplifyAlgorithm="0">
  <renderer-v2 symbollevels="0" enableorderby="0" type="categorizedSymbol" attr="pareto_ganadero_yucatan_FINAL_pareto_grupo" forceraster="0">
    <categories>
      <category render="true" symbol="0" value="Pareto" label="11 Municipios PARETO (80.3% concentración)"/>
      <category render="true" symbol="1" value="Resto" label="95 Municipios RESTO (19.7% concentración)"/>
      <category render="true" symbol="2" value="" label="Sin datos"/>
    </categories>
    <symbols>
      <!-- Municipios PARETO - Rojo intenso para destacar -->
      <symbol force_rhr="0" alpha="1" clip_to_extent="1" name="0" type="fill">
        <layer enabled="1" class="SimpleFill" locked="0" pass="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="178,34,34,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="255,255,255,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="1.0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
        </layer>
      </symbol>
      <!-- Municipios RESTO - Verde claro -->
      <symbol force_rhr="0" alpha="0.6" clip_to_extent="1" name="1" type="fill">
        <layer enabled="1" class="SimpleFill" locked="0" pass="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="144,238,144,180"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="85,107,47,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.3"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
        </layer>
      </symbol>
      <!-- Sin datos - Gris -->
      <symbol force_rhr="0" alpha="0.3" clip_to_extent="1" name="2" type="fill">
        <layer enabled="1" class="SimpleFill" locked="0" pass="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="211,211,211,100"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="128,128,128,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.1"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <!-- Etiquetas para municipios Pareto -->
  <labeling type="rule-based">
    <rules key="{a85c4044-1234-1234-1234-123456789abc}">
      <rule key="{b85c4044-5678-5678-5678-123456789def}" filter="&quot;pareto_ganadero_yucatan_FINAL_pareto_grupo&quot; = 'Pareto'">
        <settings calloutType="simple">
          <text-style fontSize="8" textOrientation="horizontal" fontCapitals="0" fontUnderline="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontFamily="Arial" fontStrikeout="0" textOpacity="1" fontLetterSpacing="0" fontSizeUnit="Point" blendMode="0" fontItalic="0" fontWordSpacing="0" textColor="255,255,255,255" previewBkgrdColor="255,255,255,255" fieldName="pareto_ganadero_yucatan_FINAL_municipio" fontWeight="75" fontKerning="1" namedStyle="Bold" multilineHeight="1" isExpression="0" useSubstitutions="0">
            <text-buffer bufferSize="1.0" bufferSizeUnits="MM" bufferColor="0,0,0,255" bufferNoFill="0" bufferOpacity="0.8" bufferJoinStyle="128" bufferDraw="1" bufferBlendMode="0" bufferSizeMapUnitScale="3x:0,0,0,0,0,0"/>
          </text-style>
          <text-format autoWrapLength="0" wrapChar="" formatNumbers="0" decimals="3" placeDirectionSymbol="0" addDirectionSymbol="0" multilineAlign="3" useMaxLineLengthForAutoWrap="1" leftDirectionSymbol="&lt;" rightDirectionSymbol=">" reverseDirectionSymbol="0" plussign="0"/>
          <placement centroidInside="1" maxCurvedCharAngleOut="-25" geometryGeneratorEnabled="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" layerType="PolygonGeometry" centroidWhole="0" maxCurvedCharAngleIn="25" fitInPolygonOnly="1" dist="0" priority="10" offsetUnits="MM" geometryGenerator="" repeatDistance="0" offsetType="0" xOffset="0" yOffset="0" placementFlags="10" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" quadOffset="4" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" preserveRotation="1" rotationAngle="0" repeatDistanceUnits="MM" overrunDistanceUnit="MM" overrunDistance="0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorType="PointGeometry" placement="0" distUnits="MM" distMapUnitScale="3x:0,0,0,0,0,0"/>
        </settings>
      </rule>
    </rules>
  </labeling>
  <blendMode>0</blendMode>
</qgis>