from client import DynamicJavascriptCleanMarkdownWebScraperClient

def main():
    client = DynamicJavascriptCleanMarkdownWebScraperClient()
    res = client.crawl_spa_to_markdown('https://kubernetes.io/docs/concepts/architecture/')
    print('Crawl Job: ' + res['crawl_job_id'] + ' | ' + res['target_url'])
    print('JS Rendered: ' + str(res['javascript_dom_rendered']) + ' | Markdown: ' + str(res['clean_markdown_bytes']) + ' bytes')
    print('Codeblock Preservation: ' + str(res['tables_and_codeblocks_preserved_pct']) + '% | Links: ' + str(res['extracted_links_count']))
    print('Markdown URL: ' + res['llm_ready_markdown_url'])

if __name__ == '__main__':
    main()
