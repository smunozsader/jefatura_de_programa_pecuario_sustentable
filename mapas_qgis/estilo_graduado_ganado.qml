<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.16" simplifyDrawingHints="1" readOnly="0" simplifyDrawingTol="1" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" simplifyLocal="1" maxScale="0" minScale="100000000" labelsEnabled="1" simplifyMaxScale="1" simplifyAlgorithm="0">
  <renderer-v2 graduatedMethod="GraduatedColor" symbollevels="0" enableorderby="0" type="graduatedSymbol" attr="pareto_ganadero_yucatan_FINAL_ganado_bovino" forceraster="0">
    <ranges>
      <!-- Muy Alto: 80,000+ cabezas (Tizimín, Valladolid) - Rojo intenso -->
      <range render="true" symbol="0" lower="80000.000000" upper="150000.000000" label="Muy Alto (80,000+ cabezas)"/>
      <!-- Alto: 50,000-79,999 cabezas - Rojo medio-alto -->
      <range render="true" symbol="1" lower="50000.000000" upper="79999.000000" label="Alto (50,000-79,999 cabezas)"/>
      <!-- Medio-Alto: 35,000-49,999 cabezas - Rojo medio -->
      <range render="true" symbol="2" lower="35000.000000" upper="49999.000000" label="Medio-Alto (35,000-49,999 cabezas)"/>
      <!-- Medio: 20,000-34,999 cabezas - Rojo claro -->
      <range render="true" symbol="3" lower="20000.000000" upper="34999.000000" label="Medio (20,000-34,999 cabezas)"/>
      <!-- Bajo: 10,000-19,999 cabezas - Rosa -->
      <range render="true" symbol="4" lower="10000.000000" upper="19999.000000" label="Bajo (10,000-19,999 cabezas)"/>
      <!-- Muy Bajo: 1-9,999 cabezas - Rosa muy claro -->
      <range render="true" symbol="5" lower="1.000000" upper="9999.000000" label="Muy Bajo (1-9,999 cabezas)"/>
    </ranges>
    <symbols>
      <!-- Muy Alto: Rojo intenso #B22222 -->
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
          <prop k="outline_width" v="1.2"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
        </layer>
      </symbol>
      <!-- Alto: Rojo medio-alto #CD5C5C -->
      <symbol force_rhr="0" alpha="1" clip_to_extent="1" name="1" type="fill">
        <layer enabled="1" class="SimpleFill" locked="0" pass="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="205,92,92,255"/>
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
      <!-- Medio-Alto: Rojo medio #DC143C -->
      <symbol force_rhr="0" alpha="1" clip_to_extent="1" name="2" type="fill">
        <layer enabled="1" class="SimpleFill" locked="0" pass="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="220,20,60,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="255,255,255,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.8"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
        </layer>
      </symbol>
      <!-- Medio: Rojo claro #F08080 -->
      <symbol force_rhr="0" alpha="0.9" clip_to_extent="1" name="3" type="fill">
        <layer enabled="1" class="SimpleFill" locked="0" pass="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="240,128,128,230"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="128,128,128,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.6"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
        </layer>
      </symbol>
      <!-- Bajo: Rosa #FFA0A0 -->
      <symbol force_rhr="0" alpha="0.7" clip_to_extent="1" name="4" type="fill">
        <layer enabled="1" class="SimpleFill" locked="0" pass="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,160,160,180"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="128,128,128,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.4"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
        </layer>
      </symbol>
      <!-- Muy Bajo: Rosa muy claro #FFE4E1 -->
      <symbol force_rhr="0" alpha="0.5" clip_to_extent="1" name="5" type="fill">
        <layer enabled="1" class="SimpleFill" locked="0" pass="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,228,225,130"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="128,128,128,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.2"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
        </layer>
      </symbol>
    </symbols>
    <source-symbol>
      <symbol force_rhr="0" alpha="1" clip_to_extent="1" name="0" type="fill">
        <layer enabled="1" class="SimpleFill" locked="0" pass="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,0,0,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
        </layer>
      </symbol>
    </source-symbol>
    <colorramp name="[source]" type="gradient">
      <prop k="color1" v="255,245,240,255"/>
      <prop k="color2" v="103,0,13,255"/>
      <prop k="discrete" v="0"/>
      <prop k="rampType" v="gradient"/>
      <prop k="stops" v="0.13;254,224,210,255:0.26;252,187,161,255:0.39;252,146,114,255:0.52;251,106,74,255:0.65;239,59,44,255:0.78;203,24,29,255:0.9;165,15,21,255"/>
    </colorramp>
    <classificationMethod id="Jenks">
      <symmetricMode enabled="0" symmetrypoint="0" astride="0"/>
      <labelFormat labelprecision="0" format="%1 - %2" trimtrailingzeroes="1"/>
      <parameters>
        <Option/>
      </parameters>
      <extraInformation/>
    </classificationMethod>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <!-- Etiquetas solo para los municipios de mayor concentración -->
  <labeling type="rule-based">
    <rules key="{a85c4044-1234-1234-1234-123456789abc}">
      <rule key="{b85c4044-5678-5678-5678-123456789def}" filter="&quot;pareto_ganadero_yucatan_FINAL_ganado_bovino&quot; >= 35000">
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