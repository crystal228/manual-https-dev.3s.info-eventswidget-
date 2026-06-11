# Test Cases

## TC-001. Open constructor page

Priority: High

Preconditions: Browser is available, network connection is active.

Steps:
1. Open `https://dev.3s.info/eventswidget/`.
2. Wait until page load is completed.

Expected result: Page is opened, constructor controls and embed-code textarea are visible.

Status: Pass

## TC-002. Generate default preview

Priority: High

Preconditions: Constructor page is opened.

Steps:
1. Do not change default settings.
2. Click `Сгенерировать превью`.
3. Check preview iframe and generated embed-code.

Expected result: Preview is generated and visually matches iframe attributes from embed-code.

Status: Fail

## TC-003. Generate widget with red theme

Priority: High

Preconditions: Constructor page is opened.

Steps:
1. Select red color theme.
2. Click `Сгенерировать превью`.
3. Check generated embed-code.

Expected result: Embed-code contains `theme=red`.

Status: Fail

## TC-004. Select event categories

Priority: Medium

Preconditions: Constructor page is opened.

Steps:
1. Select `Affiliate`.
2. Select `Fintech`.
3. Click `Сгенерировать превью`.
4. Check generated embed-code.

Expected result: Embed-code contains selected event categories.

Status: Pass

## TC-005. Select countries

Priority: Medium

Preconditions: Constructor page is opened.

Steps:
1. Select `Россия`.
2. Select `США`.
3. Select `Онлайн`.
4. Click `Сгенерировать превью`.
5. Check generated embed-code.

Expected result: Embed-code contains selected countries.

Status: Pass

## TC-006. Set custom width and height

Priority: High

Preconditions: Constructor page is opened.

Steps:
1. Set width to `500`.
2. Set height to `600`.
3. Click `Сгенерировать превью`.
4. Check iframe attributes in embed-code.

Expected result: Embed-code contains `width="500"` and `height="600"`.

Status: Pass

## TC-007. Generate full width and auto height widget

Priority: Medium

Preconditions: Constructor page is opened.

Steps:
1. Enable `на всю ширину контейнера`.
2. Enable `на всю высоту блока`.
3. Click `Сгенерировать превью`.
4. Check generated embed-code and preview.

Expected result: Embed-code and preview use updated full-size settings consistently.

Status: Fail

## TC-008. Repeat generation after settings change

Priority: High

Preconditions: Preview has already been generated.

Steps:
1. Change theme from turquoise to blue.
2. Change width and height.
3. Click `Сгенерировать превью`.
4. Compare embed-code `src` and preview iframe `src`.

Expected result: Preview iframe is recreated with the same `src` as generated embed-code.

Status: Fail

## TC-009. Edge case: negative size values

Priority: Medium

Preconditions: Constructor page is opened.

Steps:
1. Enter `-1` into width.
2. Enter `-1` into height.
3. Click `Сгенерировать превью`.

Expected result: User sees validation message or invalid values are clearly rejected.

Status: Fail

## TC-010. Responsive layout on mobile

Priority: Medium

Preconditions: Browser viewport can be changed.

Steps:
1. Set viewport to `375x812`.
2. Open constructor page.
3. Check main controls, embed-code block and footer.

Expected result: Page remains usable without critical overlaps or horizontal scrolling.

Status: Pass
