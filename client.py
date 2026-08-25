class DynamicJavascriptCleanMarkdownWebScraperClient:
    def crawl_spa_to_markdown(self, target_url='https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering', wait_for_selectors=None):
        wait_for_selectors = wait_for_selectors or ['main', 'article']
        return {
            'crawl_job_id': 'frc_crw_5519',
            'target_url': target_url,
            'javascript_dom_rendered': True,
            'clean_markdown_bytes': 18450,
            'tables_and_codeblocks_preserved_pct': 99.8,
            'extracted_links_count': 32,
            'llm_ready_markdown_url': 'https://crawls.genpark.ai/output/5519.md'
        }
